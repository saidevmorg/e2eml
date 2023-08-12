from setuptools import setup, find_packages

def get_requirements(filepath:str) -> list[str]:
    requirements = []
    with open(filepath) as fobj:
        requirements = fobj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name='e2eml', 
    version='0.0.1',
    author='Projjal Prajna Das',
    author_email='projjalprajna@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')

)