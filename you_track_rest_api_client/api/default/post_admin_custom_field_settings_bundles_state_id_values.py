from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.state_bundle_element import StateBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Dict[str, Any]:
    url = "{}/admin/customFieldSettings/bundles/state/{id}/values".format(client.base_url, id=id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[StateBundleElement]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StateBundleElement.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[StateBundleElement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Response[StateBundleElement]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement): Represents the state of an issue in YouTrack.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StateBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: str,
    *,
    client: Client,
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Optional[StateBundleElement]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement): Represents the state of an issue in YouTrack.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StateBundleElement]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Response[StateBundleElement]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement): Represents the state of an issue in YouTrack.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StateBundleElement]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        fields=fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: StateBundleElement,
    fields: Union[
        Unset, None, str
    ] = "$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal",
) -> Optional[StateBundleElement]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal'.
            Example:
            $type,color($type,background,foreground,id),id,isResolved,localizedName,name,ordinal.
        json_body (StateBundleElement): Represents the state of an issue in YouTrack.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StateBundleElement]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
