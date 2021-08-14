import multiprocessing
import uuid
from pathlib import Path
import docker


def compile_code(code, user_input):
    """This function create docker container and run user code inside it"""

    # getting docker client from env vars (same as default docker CLI client)
    client = docker.from_env()

    # manager provide a way to share data between processes
    manager = multiprocessing.Manager()

    # this dict collect results of processes
    result_dict = manager.dict()

    container_name = get_container_name()
    file_name = container_name + ".c"
    create_file(code, file_name)


def get_container_name():
    return str(uuid.uuid4().hex)


def create_file(code, file_name):
    file_path = Path('/app/compiler_volume/' + file_name)
    with file_path.open("w") as f:
        f.write(code)
