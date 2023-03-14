from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.appearance_settings import AppearanceSettings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Dict[str, Any]:
    url = "{}/admin/globalSettings/appearanceSettings".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fields"] = fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[AppearanceSettings]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AppearanceSettings.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[AppearanceSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Response[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppearanceSettings]
    """

    kwargs = _get_kwargs(
        client=client,
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
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Optional[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppearanceSettings]
    """

    return sync_detailed(
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Response[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppearanceSettings]
    """

    kwargs = _get_kwargs(
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,dateFieldFormat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation)",
) -> Optional[AppearanceSettings]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,dateFieldFormat($type,datePattern,id,pa
            ttern,presentation),id,timeZone($type,id,offset,presentation)'. Example: $type,dateFieldFo
            rmat($type,datePattern,id,pattern,presentation),id,timeZone($type,id,offset,presentation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppearanceSettings]
    """

    return (
        await asyncio_detailed(
            client=client,
            fields=fields,
        )
    ).parsed
