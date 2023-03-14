from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.issue_count_response import IssueCountResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: IssueCountResponse,
    fields: Union[Unset, None, str] = "$type,count,id",
) -> Dict[str, Any]:
    url = "{}/issuesGetter/count".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[IssueCountResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IssueCountResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[IssueCountResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: IssueCountResponse,
    fields: Union[Unset, None, str] = "$type,count,id",
) -> Response[IssueCountResponse]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,count,id'. Example: $type,count,id.
        json_body (IssueCountResponse): Represents the number of issues in a search result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueCountResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: IssueCountResponse,
    fields: Union[Unset, None, str] = "$type,count,id",
) -> Optional[IssueCountResponse]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,count,id'. Example: $type,count,id.
        json_body (IssueCountResponse): Represents the number of issues in a search result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueCountResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: IssueCountResponse,
    fields: Union[Unset, None, str] = "$type,count,id",
) -> Response[IssueCountResponse]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,count,id'. Example: $type,count,id.
        json_body (IssueCountResponse): Represents the number of issues in a search result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueCountResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: IssueCountResponse,
    fields: Union[Unset, None, str] = "$type,count,id",
) -> Optional[IssueCountResponse]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,count,id'. Example: $type,count,id.
        json_body (IssueCountResponse): Represents the number of issues in a search result.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IssueCountResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
