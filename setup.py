from setuptools import setup, find_packages
from typing import List


def get_requirements_list() -> List[str]:
    # Returns List of elements in requirements.txt
    with open('requirements.txt') as requirements_file:
        # Exclude any lines containing '-e .'
        return [line.strip() for line in requirements_file if '-e .' not in line]


# Declaring variables for setup Function
Project_Name = 'Housing_Price_Predictor'
Version = '0.0.3'
Author = 'DharmaTeja'
Description = 'One Of The ML Project-Practice'

setup(
    name=Project_Name,
    version=Version,
    author=Author,
    description=Description,
    packages=find_packages(),
    install_requires=get_requirements_list(),
)

if __name__ == "__main__":
    print(get_requirements_list())

    