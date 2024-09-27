import sys

from output_utilities import OutputUtils


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main():
    msg = f'Python version: {get_python_version()}'
    print(msg)
    OutputUtils.display_message(msg, 'Python Version')

if __name__ == '__main__':
    main()