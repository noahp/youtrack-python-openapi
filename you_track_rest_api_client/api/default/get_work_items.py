import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,ringId),created,creator($type,id,login,ringId),date,duration($type,id),id,text,updated",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workItems".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["query"] = query

    json_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat() if start_date else None

    params["startDate"] = json_start_date

    json_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat() if end_date else None

    params["endDate"] = json_end_date

    params["start"] = start

    params["end"] = end

    params["createdStart"] = created_start

    params["createdEnd"] = created_end

    params["updatedStart"] = updated_start

    params["updatedEnd"] = updated_end

    params["author"] = author

    params["creator"] = creator

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
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,ringId),created,creator($type,id,login,ringId),date,duration($type,id),id,text,updated",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        query (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.date]):
        end_date (Union[Unset, None, datetime.date]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):
        created_start (Union[Unset, None, int]):
        created_end (Union[Unset, None, int]):
        updated_start (Union[Unset, None, int]):
        updated_end (Union[Unset, None, int]):
        author (Union[Unset, None, str]):
        creator (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,author($type,id,login,ringId),created,c
            reator($type,id,login,ringId),date,duration($type,id),id,text,updated'. Example: $type,aut
            hor($type,id,login,ringId),created,creator($type,id,login,ringId),date,duration($type,id),
            id,text,updated.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        query=query,
        start_date=start_date,
        end_date=end_date,
        start=start,
        end=end,
        created_start=created_start,
        created_end=created_end,
        updated_start=updated_start,
        updated_end=updated_end,
        author=author,
        creator=creator,
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
    *,
    client: Client,
    query: Union[Unset, None, str] = UNSET,
    start_date: Union[Unset, None, datetime.date] = UNSET,
    end_date: Union[Unset, None, datetime.date] = UNSET,
    start: Union[Unset, None, int] = UNSET,
    end: Union[Unset, None, int] = UNSET,
    created_start: Union[Unset, None, int] = UNSET,
    created_end: Union[Unset, None, int] = UNSET,
    updated_start: Union[Unset, None, int] = UNSET,
    updated_end: Union[Unset, None, int] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    creator: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,author($type,id,login,ringId),created,creator($type,id,login,ringId),date,duration($type,id),id,text,updated",
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Any]:
    """
    Args:
        query (Union[Unset, None, str]):
        start_date (Union[Unset, None, datetime.date]):
        end_date (Union[Unset, None, datetime.date]):
        start (Union[Unset, None, int]):
        end (Union[Unset, None, int]):
        created_start (Union[Unset, None, int]):
        created_end (Union[Unset, None, int]):
        updated_start (Union[Unset, None, int]):
        updated_end (Union[Unset, None, int]):
        author (Union[Unset, None, str]):
        creator (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,author($type,id,login,ringId),created,c
            reator($type,id,login,ringId),date,duration($type,id),id,text,updated'. Example: $type,aut
            hor($type,id,login,ringId),created,creator($type,id,login,ringId),date,duration($type,id),
            id,text,updated.
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        query=query,
        start_date=start_date,
        end_date=end_date,
        start=start,
        end=end,
        created_start=created_start,
        created_end=created_end,
        updated_start=updated_start,
        updated_end=updated_end,
        author=author,
        creator=creator,
        fields=fields,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
