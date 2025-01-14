
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(name='mlospp',
      version='0.0.1',
      description='mlops practice project',
      author='vaibhav',
      author_email='hellovaibt@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      )

## command:  python setup.py install (automatically create build,dist $ .egg-info) files
## pip install -r requirements.txt   (automatically create only .egg-info) file