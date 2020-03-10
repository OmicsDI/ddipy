from setuptools import setup, find_packages

setup(
    name="ddipy",
    version="0.0.1",
    keywords=["pip", "omicsDI", "WS-client"],
    py_modules=["ddipy"],
    description="web-service client of omicsDI API",
    license="Apache 2",
    url="https://github.com/OmicsDI/ddipy",
    author="Xpon",
    author_email="ypriverol@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests"]
)
