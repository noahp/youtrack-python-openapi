from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Dict[str, Any]:
    url = "{}/issues/{id}/activities/{activityItemId}".format(client.base_url, id=id, activityItemId=activity_item_id)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Response[Any]:
    """
    Args:
        id (str):
        activity_item_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,added,author($type,id,login,ringId),cat
            egory($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),i
            d,name),id,removed,target,targetMember,timestamp'. Example: $type,added,author($type,id,lo
            gin,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,locali
            zedName,name),id,name),id,removed,target,targetMember,timestamp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        activity_item_id=activity_item_id,
        client=client,
        fields=fields,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    activity_item_id: str,
    *,
    client: Client,
    fields: Union[
        Unset, None, str
    ] = "$type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp",
) -> Response[Any]:
    """
    Args:
        id (str):
        activity_item_id (str):
        fields (Union[Unset, None, str]):  Default: '$type,added,author($type,id,login,ringId),cat
            egory($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),i
            d,name),id,removed,target,targetMember,timestamp'. Example: $type,added,author($type,id,lo
            gin,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,locali
            zedName,name),id,name),id,removed,target,targetMember,timestamp.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        activity_item_id=activity_item_id,
        client=client,
        fields=fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
