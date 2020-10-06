import pathlib

from setuptools import find_packages, setup
from typing import List

PARENT = pathlib.Path(__file__).parent


def read_requirements(path: str) -> List[str]:
    file_path = PARENT / path
    with open(file_path) as f:
        return f.read().split("\n")


setup(
        name='SCA11H',
        version='0.1.0',
        description='SCA11H Bed Sensor Helper',
        url='',
        author='Dennis Sitelew',
        author_email='yowidin@gmail.com',
        license='MIT',
        packages=find_packages(exclude=('test',)),
        scripts=[
            'bin/bcg-hostless-api',
        ],
        install_requires=read_requirements("requirements.txt"),
        zip_safe=False,
)
