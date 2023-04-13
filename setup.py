from setuptools import setup

setup(
    name='foopackage',
    version='0.0.1',
    packages=["foopackage"],
    entry_points={
        "console_scripts": [
            "foopackage = foopackage.__main__:main"
        ]
    },
)
