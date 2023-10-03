from setuptools import setup, find_packages

setup(
    name='my_python_project',
    version='0.1.0',
    description='My Python Project',
    author='Hricha',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
)
