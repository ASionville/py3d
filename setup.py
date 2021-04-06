import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py3d-lib",
    version="1.0.0",
    description="Un module python en français, qui vise à simplifier les programmes utilisants de la géométrie 2D ou 3D",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ASionville/py3d",
    author="Aubin SIONVILLE",
    author_email="aubinsionville@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["py3d"],
    include_package_data=True,
    install_requires=["matplotlib", "numpy"]
)
