from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()
def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name="ddipy",
    version="0.0.5",
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
