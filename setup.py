from setuptools import setup, find_packages
import re


def readme():
    with open('README.md') as f:
        return f.read()


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


PEP440_PATTERN = r"([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?"  # noqa


def version():
    with open('ddipy/_version.py') as f:
        v = f.read().strip()
        m = re.match(r'^__version__ = "(' + PEP440_PATTERN + ')"$', v)
        if not m:
            msg = ('ddipy/_version.py did not match pattern '
                   '__version__ = "0.1.2"  (see PEP440):\n') + v
            raise Exception(msg)
        return m.group(1)


setup(
    name="ddipy",
    version=version(),
    keywords=["pip", "omicsDI", "WS-client"],
    py_modules=["ddipy"],
    description="Python client for OmicsDI Restful API",
    license='LICENSE',
    url="https://github.com/OmicsDI/ddipy",
    author="OmicsDI Team",
    author_email="ypriverol@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    python_requires='>=3.4',
    long_description_content_type='text/markdown',
    long_description=readme(),
    install_requires=[requirements()],
    entry_points={
        "console_scripts": [
            "omicsdi = ddipy.cli:main"
        ]
    },
)
