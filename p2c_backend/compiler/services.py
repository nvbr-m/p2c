import multiprocessing
import os
import uuid
from pathlib import Path
import docker
import shutil


def compile_code(code, user_input='', test_input=[]):
    """This function create docker container and run user code inside it"""
    # getting docker client from env vars (same as default docker CLI client)
    client = docker.from_env()

    # manager provide a way to share data between processes
    manager = multiprocessing.Manager()

    # this dict collect results of processes
    result_dict = manager.dict()

    container_name = get_container_name()
    # create file with code and dir to share with gcc-container (dir name = container name)
    create_file(code, container_name)

    process = multiprocessing.Process(target=runner,
                                      args=(
                                          client, container_name, result_dict, user_input, test_input))
    process.start()
    # arg set timeout for process
    process.join(10)

    if process.is_alive():
        process.terminate()
        process.join()
        result_dict['result'] = 'Time limit Exceeded.'

    running_containers = client.containers.list(filters={'name': container_name}, all=True)
    if running_containers:
        running_containers[0].remove(force=True)

    # remove dir even with files
    shutil.rmtree(Path('/app/compiler_volume/' + container_name), ignore_errors=True)

    return result_dict


def get_container_name():
    return str(uuid.uuid4().hex)


def create_file(code, container_name):
    os.mkdir('/app/compiler_volume/' + container_name)
    file_path = Path('/app/compiler_volume/' + container_name + '/prog.c')
    with file_path.open("w") as f:
        f.write(code)


def runner(client, container_name, result_dict, user_input, test_input):
    try:
        # this path should be absolute HOST path (not containers)
        file_path = '/Users/nvbr/2021/p2c/p2c_backend/compiler_volume/' + container_name  # TODO get this path from env
        container_file_path = '/home/' + container_name
        compile_container = client.containers.create("gcc:9.4.0-buster",
                                                     "sleep 100",
                                                     name=container_name,
                                                     volumes={file_path: {
                                                         'bind': container_file_path,
                                                         'mode': 'rw'}
                                                     })
        compile_container.start()
        status = compile_container.exec_run("gcc prog.c",
                                            workdir=container_file_path)
        # status is a tuple. 0 element is exit code, 1 element is result
        if status[0]:
            result_dict['result'] = status[1]
            return
        if test_input:
            for test_case in test_input:
                result_dict[test_case] = compile_container.exec_run(
                    f"/bin/bash -c 'echo {test_case} | ./a.out'",
                    workdir=container_file_path)[1]
            return
        result_dict['result'] = compile_container.exec_run(
            f"/bin/bash -c 'echo {user_input} | ./a.out {user_input}'",
            workdir=container_file_path)[1]

    # TODO delete this later
    except Exception:
        result_dict['result'] = "Error. Try later."
