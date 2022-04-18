import sys
from datetime import datetime


def convert_date(cruise_date):

    return datetime.fromisoformat(cruise_date).strftime('%B %d, %Y')


def validate():
    creator = '{{cookiecutter.processor_first_name}}'

    if not creator.strip():
        print("ERROR FAILED(1): You must specify a creator to use this template")
        return 1

    if creator.lower().strip() == 'your first name':
        print("ERROR FAILED(2): You must specify a creator to use this template")
        return 2

    return 0


if __name__ == '__main__':
    new_cruise_date_start = convert_date('{{cookiecutter.cruise_date_start}}')
    sys.exit(validate())
