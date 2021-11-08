from setuptools import setup, find_packages

setup(
    name="elk_json_formatter",
    version="0.0.2",
    description="",
    url="www.informatik.tu-darmstadt.de/ukp",
    author="UKP",
    author_email="baumgaertner@ukp.informatik.tu-darmstadt.de",
    packages=find_packages(),
    install_requires=["python-json-logger==2.0.1"]
)
