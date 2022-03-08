import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_version(rel_path):
    with open(rel_path, "r") as fh:
        for line in fh.readlines():
            if line.startswith("__version__"):
                return line.split('"')[1]
        else:
            raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="autodc",
    version="1.0.7",
    author="@zacqoo",
    author_email="zacqoo@gmail.com",
    description="AutoDC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hypergiant/autodc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[
        "opencv-python==4.5.3.56",
        "scikit-learn==0.24.2",
        "numpy==1.19.5",
        "matplotlib==3.4.3",
        "python-magic-bin==0.4.14",
        "augly==0.2.1",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)