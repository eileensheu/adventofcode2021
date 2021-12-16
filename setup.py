from setuptools import setup, find_packages
import re


def get_property(prop, project):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(project + '/__init__.py').read())
    return result.group(1)


setup(
    name="pyaoc",
    version=get_property('__version__', 'pyaoc'),
    description="Scripts and toolings for Advent of Code",
    author="Eileen Sheu",
    url="https://github.com/eileensheu/adventofcode2021",
    zip_safe=False
)
