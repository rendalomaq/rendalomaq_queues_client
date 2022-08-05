from setuptools import find_packages, setup

VERSION = "0.0.1"
DESCRIPTION = "Queues client"
LONG_DESCRIPTION = "Queues client"

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="queues_client",
    version=VERSION,
    author="Sebastían Díaz",
    author_email="<kziete@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["boto3"],
    keywords=["python", "queue", "sqs"],
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
