from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

requirements = [
    "requests>=2.22.0", "python-dotenv>=0.12.0"
]


setup(
    name="greekwordnet",
    version="0.0.5",
    packages=find_packages(),
    url="https://greekwordnet.chs.harvard.edu",
    license="GNU General Public License v3.0",
    author="William Michael Short",
    author_email="w.short@exeter.ac.uk",
    description="A light-weight Python wrapper for the Greek WordNet API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    test_suite="tests",
)
