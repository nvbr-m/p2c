import multiprocessing
import os
import uuid
from pathlib import Path
import docker
import shutil


def compile_code(code, user_input):
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
                                          client, container_name, result_dict, user_input))
    process.start()

    process.join(10)

    if process.is_alive():
        process.terminate()
        process.join()
        result_dict['result'] = 'Time limit Exceeded.'

    running_containers = client.containers.list(filters={'name': container_name}, all=True)
    if running_containers:
        running_containers[0].remove(force=True)

    shutil.rmtree(Path('/app/compiler_volume/' + container_name), ignore_errors=True)

    return result_dict


def get_container_name():
    return str(uuid.uuid4().hex)


def create_file(code, container_name):
    os.mkdir('/app/compiler_volume/' + container_name)
    file_path = Path('/app/compiler_volume/' + container_name + '/prog.c')
    with file_path.open("w") as f:
        f.write(code)


def runner(client, container_name, result_dict, user_input):
    try:
        file_path = '/Users/nvbr/2021/p2c/p2c_backend/compiler_volume/' + container_name
        container_file_path = '/home/' + container_name
        compile_container = client.containers.create("gcc:9.4.0-buster",
                                                     f' /bin/bash -c "gcc {container_file_path}/prog.c -o {container_file_path}/a.out && sleep 100"',
                                                     name=container_name, detach=True,
                                                     volumes={file_path: {
                                                         'bind': container_file_path,
                                                         'mode': 'rw'}
                                                     })
        compile_container.start()
        result_dict['result']=compile_container.exec_run(f"/bin/bash -c 'echo {user_input} | ./a.out'",
                                   workdir=container_file_path)

    except docker.errors.ContainerError as e:
        # error_mes = str(e).replace()
        result_dict['cont'] = str(e)

    except Exception as e:
        result_dict['132'] = str(e)
