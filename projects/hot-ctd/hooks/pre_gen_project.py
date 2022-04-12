import sys


def validate():
    creator = '{{cookiecutter.first_name}}'

    if not creator.strip():
        print("ERROR FAILED(1): You must specify a creator to use this template")
        return 1

    if creator.lower().strip() == 'your name':
        print("ERROR FAILED(2): You must specify a creator to use this template")
        return 2

    return 0


if __name__ == '__main__':
    sys.exit(validate())
