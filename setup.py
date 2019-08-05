import io
import re

from setuptools import setup

with io.open("geolocation/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="geolocation",
    version=version,
    description="A set of Python tools using geolocation coordinates."
)
