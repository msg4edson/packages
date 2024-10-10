from setuptools import setup, find_packages

setup(
    name="words",
    version="1.0.0",
    description="Helper library for generating random words",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
