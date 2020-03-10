import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup, find_packages


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name='image_processing_workshop',
    version='1.0',
    description='Workshop custom tools',
    author='Adam Kolar',
    author_email='',
    url='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=[],
    setup_requires=['pytest-runner'],
    install_requires=[
        'ipywidgets==7.4.2',
        'torch==1.3.0',
        'torchvision==0.4.1',
        'matplotlib==3.0.3',
        'seaborn==0.9.0',
        'tqdm==4.31.1',
        'tensorflow==1.15.0',
        'tb-nightly==1.15.0a20190911',
        'requests==2.21.0'
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    include_package_data=True,
    package_data={},
)
