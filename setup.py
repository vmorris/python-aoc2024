from setuptools import setup, find_packages

dependencies = [
    "wheel",
    "Jinja2",
    "Click",
    # "anytree",
    "sortedcontainers",
    "numpy",
    "networkx",
    "matplotlib",
]
tests_dependencies = [
    "pytest",
    "pytest_cov",
]
extras = {"test": tests_dependencies}

setup(
    name="aoc2024",
    version="0.0.1",
    description="Advent of Code 2024 Solutions",
    author="Vance Morris",
    author_email="vmorris@us.ibm.com",
    packages=find_packages(),
    install_requires=dependencies,
    tests_require=tests_dependencies,
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "newday = newday.newday:newday",
        ],
    },
)
