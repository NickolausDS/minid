from setuptools import setup, find_packages
import os

version = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'minid', 'version.py')) as f:
    exec(f.read(), {}, version)

# Get the long description from the README file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


setup(
    name='minid',
    version=version['__VERSION__'],
    description='BD2K Minimum Viable Identifier',
    long_description=long_description,
    url='http://minid.bd2k.org/',
    author='Kyle Chard',
    author_email='chard@uchicago.edu',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=[
        'git+https://github.com/fair-research/globus-identifiers-client'
        '#egg=globus-identifiers-client',
    ],
    license='Apache 2.0',
    entry_points={
        'console_scripts': [
            'minid = minid.commands.main:main',
        ]
    }
)
