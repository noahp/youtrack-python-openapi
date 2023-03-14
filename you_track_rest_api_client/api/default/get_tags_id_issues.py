from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    custom_fields: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,created,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tags/{id}/issues".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["customFields"] = custom_fields

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
    *,
    client: Client,
    custom_fields: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,created,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (str):
        custom_fields (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,created,customFields($type,id,name,valu
            e($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,loc
            alizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login
            ,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permi
            ttedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))'. Example: $type,c
            reated,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($t
            ype,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,n
            ame,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,l
            ogin,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($typ
            e,id,login,ringId)).
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        custom_fields=custom_fields,
        fields=fields,
        skip=skip,
        top=top,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    custom_fields: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,created,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        id (str):
        custom_fields (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,created,customFields($type,id,name,valu
            e($type,id,name)),description,id,idReadable,links($type,direction,id,linkType($type,id,loc
            alizedName,name)),numberInProject,project($type,id,name,shortName),reporter($type,id,login
            ,ringId),resolved,summary,updated,updater($type,id,login,ringId),visibility($type,id,permi
            ttedGroups($type,id,name,ringId),permittedUsers($type,id,login,ringId))'. Example: $type,c
            reated,customFields($type,id,name,value($type,id,name)),description,id,idReadable,links($t
            ype,direction,id,linkType($type,id,localizedName,name)),numberInProject,project($type,id,n
            ame,shortName),reporter($type,id,login,ringId),resolved,summary,updated,updater($type,id,l
            ogin,ringId),visibility($type,id,permittedGroups($type,id,name,ringId),permittedUsers($typ
            e,id,login,ringId)).
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        custom_fields=custom_fields,
        fields=fields,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
