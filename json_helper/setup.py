import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="json-to-pandas-James-Kocher",
    version="0.0.1",
    author="James Kocher",
    author_email="jkocher13",
    description="takes your json files downloaded from and api and puts them in a pandas dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JKocher13/PythonFundamentals.Labs.PipModule",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
