#!/usr/bin/env python3
import subprocess


def create_check_remove_file(file_name="frompython.txt"):
    """
    This function will create a file called as frompython.txt
    equivalent linux commands
    1. touch frompython.txt
    2. ls
    3. rm frompython.txt
    """
    # subprocess.call(["touch", file_name])
    capture_output(["touch", file_name])
    print(f"created file {file_name}")
    # subprocess.call(["ls"])
    capture_output(["ls"])
    print("listed the files")
    # subprocess.call(["rm", file_name])
    capture_output(["rm", file_name])
    print(f"removed the file {file_name}")
    capture_output(["ls"])
    pass


def capture_output(commands):
    """
    This command will capture the return code of the commands executed
    and the stdout
    :param commands: commands to be executed
    """
    result = subprocess.run(commands, stdout=subprocess.PIPE)
    print(f"return code: {result.returncode}")
    command = " ".join(commands)
    print(f"output from the {command} executed are {result.stdout.decode('utf-8')}")


if __name__ == "__main__":
    create_check_remove_file()
