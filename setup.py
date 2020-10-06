import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-encrypted-settings",
    version="0.0.1",
    author="Ian Jones",
    description="Django settings encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonesim/django-encrypted-settings",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)