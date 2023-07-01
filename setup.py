from typing import List

from setuptools import find_packages
from setuptools import setup

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Reads a file containing a list of requirements and returns list.

    Args:
        file_path (str): The path to the file containing the requirements.

    Returns:
        List[str]: A list of requirements read from the file.
    """
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


def get_long_description(file_path: str = "README.md") -> str:
    """Reads the contents of a file and returns it as a string.

    Args:
        file_path (str, optional): The path to the file.
        Defaults to "README.md".

    Returns:
        str: The contents of the file as a string.
    """
    with open(file_path, encoding="utf-8") as f:
        long_description = f.read()
    return long_description


setup(
    name="Passwordometer",
    version="0.0.1",
    author="Karthik Udyawar",
    author_email="karthikajitudy@gmail.com",
    license="MIT",
    description="A package for evaluating password strength",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/KarthikUdyawar/Passwordometer",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)