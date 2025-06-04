from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .' # This -e . in requirement.txt  will link or connect with setup.py
def get_requirements(file_path:str) -> List[str]: # This mean it will take file Path as string and return it as list of string
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Mridul Mahajan",
    author_email="mridulmahajan16@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)