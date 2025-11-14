from setuptools import setup, find_packages
from typing import list


HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)-> list:
    '''This function will return the list of requirements'''
    with open(file_path)as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
                requirements.remove('-e .') 

        return requirements

setup(
    name= "My_Package",
    version= "0.0.1",
    author= "Indu",
    author_email="indugautam1023@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
) 