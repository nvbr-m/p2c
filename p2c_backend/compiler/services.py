import multiprocessing
import os
import uuid
from pathlib import Path
import docker


def compile_code(code):
    """This function create docker container and run user code inside it"""

    # getting docker client from env vars (same as default docker CLI client)
    client = docker.from_env()

    # manager provide a way to share data between processes
    manager = multiprocessing.Manager()

    # this dict collect results of processes
    result_dict = manager.dict()

    container_name = get_container_name()
    file_name = container_name + ".c"
    output_file_name = file_name + 'omp'
    create_file(code, file_name)

    process = multiprocessing.Process(target=runner, args=(client, file_name, container_name, result_dict,output_file_name))
    process.start()

    process.join(5)

    if process.is_alive():
        process.terminate()
        process.join()
        result_dict['result'] = 'Time limit Exceeded'

    running_containers = client.containers.list(filters={'name': container_name}, all=True)
    if running_containers:
        running_containers[0].remove(force=True)

    os.remove(Path('/app/compiler_volume/' + file_name))
    if os.path.exists('/app/compiler_volume/' + output_file_name):
        os.remove(Path('/app/compiler_volume/' + output_file_name))
    return result_dict


def get_container_name():
    return str(uuid.uuid4().hex)


def create_file(code, file_name):
    file_path = Path('/app/compiler_volume/' + file_name)
    with file_path.open("w") as f:
        f.write(code)


def runner(client, file_name, container_name, result_dict, output_file_name):

    try:
        file_path = str(Path('/Users/nvbr/2021/p2c/p2c_backend/compiler_volume'))
        container_file_path = str(Path('/home'))
        compile_container = client.containers.run("gcc:9.4.0-buster",f'/bin/bash -c "gcc /home/{file_name} -o /home/{output_file_name} && ./home/{output_file_name}"',
                                                  name=container_name, remove=True,
                                                  volumes={file_path: {
                                                      'bind': container_file_path,
                                                      'mode': 'rw'}
                                                  })
        result_dict['123']=compile_container

    except docker.errors.ContainerError as e:
        # error_mes = str(e).replace()
        result_dict['cont'] = str(e)

    except Exception as e:
        result_dict['result'] = str(e)
