try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
   name='NITT-Results-Scraper',
   version='1.0.0',
   description='Simple python tool to check any NITT student CGPA with their Octa credentials.',
   long_description=long_description,
   author='Bharath Kumar R',
   author_email='bharathkumarravichandran@gmail.com',
   url='https://github.com/BharathKumarRavichandran/NITT-Results-Scraper',
   packages=['NITT-Results-Scraper'],
   install_requires=requirements,
    license='BSD'
)