""" the setup.py file is an essential part of 
pacaking and distrubuting python projects. 
it is used by setuptools (or distutils in
 older python versions) to define the 
 configuration of your project,
such as its meta data,dependencies,and more"""

from setuptools import setup, find_packages
import os
from typing import List

def get_requirements()->List[str]:
    """this function will return a list of requirements"""
    requirement_lst: List[str] = []

    try:
        with open("requirements.txt","r") as file:
            ## read lines from the file
            lines=file.readlines()
            ## processs each line
            for line in  lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement != "-e.":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst               

print(get_requirements())

setup(
    name="networksecurity",
    version="0.0.1",
    author="mohit jadhav",
    author_email="rajemohit330@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)