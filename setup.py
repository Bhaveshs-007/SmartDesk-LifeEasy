from setuptools import find_packages, setup

setup(
    name="smartdesk",
    version="0.1.0",
    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,
    install_requires=[
        "typer[all]",
        "rich",
        "pandas",
        "matplotlib",
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "smartdesk=smartdesk.cli:main",
        ]
    },
)
