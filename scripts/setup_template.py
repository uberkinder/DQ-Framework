import setuptools
from setuptools import setup


with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='pure-data',
    version = '0.1.6.6',
    author='BOGDAN PECHENKIN',
    author_email='uberkinder@yandex.com',
    description='Pure Data Framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        'GitHub': 'https://github.com/SimulatorML/Pure-Data',
        'Documentation': 'https://pure-data.readthedocs.io/en/latest/index.html',
    },
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires='>=3.10',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
