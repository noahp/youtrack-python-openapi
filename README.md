[![GitHub](https://img.shields.io/badge/GitHub-noahp/youtrack--python--openapi-8da0cb?style=for-the-badge&logo=github)](https://github.com/noahp/youtrack-python-openapi)
[![PyPI
version](https://img.shields.io/pypi/v/youtrack-python-openapi.svg?style=for-the-badge&logo=PyPi&logoColor=white)](https://pypi.org/project/youtrack-python-openapi/)
[![PyPI
pyversions](https://img.shields.io/pypi/pyversions/youtrack-python-openapi.svg?style=for-the-badge&logo=python&logoColor=white&color=ff69b4)](https://pypi.python.org/pypi/youtrack-python-openapi/)
<!-- [![GitHub Workflow Status](https://img.shields.io/github/workflow/status/dtrx-py/dtrx/main-ci/master?logo=github-actions&logoColor=white&style=for-the-badge)](https://github.com/dtrx-py/dtrx/actions) -->

# Youtrack Python Openapi

This was auto-generated using the open api generator here:

https://github.com/openapi-generators/openapi-python-client

```bash
❯ openapi-python-client generate --url https://youtrack.jetbrains.com/api/openapi.json
```

The remainder of this readme is from the output of that script.

---

# you-track-rest-api-client
A client library for accessing YouTrack REST API

## Usage
First, create a client:

```python
from you_track_rest_api_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from you_track_rest_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from you_track_rest_api_client.models import MyDataModel
from you_track_rest_api_client.api.my_tag import get_my_data_model
from you_track_rest_api_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from you_track_rest_api_client.models import MyDataModel
from you_track_rest_api_client.api.my_tag import get_my_data_model
from you_track_rest_api_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False
)
```

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info.

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `you_track_rest_api_client.api.default`

## Building / publishing this Client
This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:
1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:
1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
