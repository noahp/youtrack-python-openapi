from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.build_bundle_element import BuildBundleElement
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/admin/customFieldSettings/bundles/build/{id}/values".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params["$skip"] = skip

    params["$top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["BuildBundleElement"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BuildBundleElement.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["BuildBundleElement"]]:
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
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["BuildBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BuildBundleElement']]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        fields=fields,
        skip=skip,
        top=top,
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
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["BuildBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BuildBundleElement']]
    """

    return sync_detailed(
        id=id,
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[List["BuildBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BuildBundleElement']]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        fields=fields,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    fields: Union[Unset, None, str] = "$type,assembleDate,color($type,background,foreground,id),id,name,ordinal",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[List["BuildBundleElement"]]:
    """
    Args:
        id (str):
        fields (Union[Unset, None, str]):  Default:
            '$type,assembleDate,color($type,background,foreground,id),id,name,ordinal'. Example:
            $type,assembleDate,color($type,background,foreground,id),id,name,ordinal.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['BuildBundleElement']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            fields=fields,
            skip=skip,
            top=top,
        )
    ).parsed
