from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT="-e."
def get_requirements(file_path)->List[str]:
    reqirements=[]
    with open(file_path) as file_obj:
        reqirements=file_obj.readlines()
        reqirements=[req.replace("\n","") for req in reqirements]
        reqirements=[req for req in reqirements if req != HYPEN_E_DOT]
    return reqirements 

setup(
    name="my_package",
    version="0.0.1",
    packages=find_packages(),
    author="prashant",
    author_email="<prashantnagasai@gmail.com>",
    description="A sample Python package",
    install_requires=get
    _requirements("requirements.txt"),
)