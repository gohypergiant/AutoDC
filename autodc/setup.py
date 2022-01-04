import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autodc",
    version="1.0.0",
    author="akashanair92",
    author_email="akashanair92@gmail.com.com",
    description="Auto DC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akashanairhg/audtoDC",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)