# hkckan: A Python Wrapper for the HKGOV CKAN API

## Introduction
`hkckan` is a Python library that provides a simple and intuitive interface to interact with the Comprehensive Knowledge Archive Network (CKAN) API. It abstracts away the low-level details of the CKAN API, making it easier to perform common tasks such as searching for datasets, creating and updating organizations, and managing user permissions.

## Installation
You can install `hkckan` using `pip`:

```sh
pip install -i https://test.pypi.org/simple/ hkckan
```

## Usage
To use `hkckan`, you first need to import the library and create a `CKANClient` object:

```python
from hkckan import list_packages, show_package

packages = list_packages(limit=10, offset=0) # Querying first 10 package IDs
package_detail = show_package(packages[0])

```

## Development
We adapt the `pytetst` framework for testing. To setup the testing environment, run:
```sh
pip install -e .
```
in the project root directory.
