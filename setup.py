# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.1'
name = 'literature_analysis_jp'
short_description = ''
author = 'Kensuke Mitsuzawa'
author_email = 'kensuke.mit@gmail.com'
url = ''
license = 'MIT'


with open('README.md') as f:
    readme = f.read()


install_requires = [
    'DocumentFeatureSelection',
    'JapaneseTokenizer',
    'knp-utils',
    'jaconv',
    'six'
]
dependency_links = []

setup(
    name=name,
    version=version,
    description='',
    long_description=readme,
    author=author,
    author_email=author_email,
    install_requires=install_requires,
    dependency_links=dependency_links,
    url=url,
    license=license,
    packages=find_packages(),
    test_suite='module_tests', #added
    include_package_data=True,
    zip_safe=False
)
