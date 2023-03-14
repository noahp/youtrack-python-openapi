from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Dict[str, Any]:
    url = "{}/activitiesPage".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["categories"] = categories

    params["reverse"] = reverse

    params["start"] = start

    params["end"] = end

    params["author"] = author

    params["issueQuery"] = issue_query

    params["cursor"] = cursor

    params["activityId"] = activity_id

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
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Response[Any]:
    """
    Args:
        categories (Union[Unset, None, str]):
        reverse (Union[Unset, None, bool]):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        issue_query (Union[Unset, None, str]):
        cursor (Union[Unset, None, str]):
        activity_id (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,activities($type,added,author($type,id,
            login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,loca
            lizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCurso
            r,hasAfter,hasBefore,id'. Example: $type,activities($type,added,author($type,id,login,ring
            Id),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,
            name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter
            ,hasBefore,id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Client,
    categories: Union[Unset, None, str] = UNSET,
    reverse: Union[Unset, None, bool] = UNSET,
    start: Union[Unset, None, str] = UNSET,
    end: Union[Unset, None, str] = UNSET,
    author: Union[Unset, None, str] = UNSET,
    issue_query: Union[Unset, None, str] = UNSET,
    cursor: Union[Unset, None, str] = UNSET,
    activity_id: Union[Unset, None, str] = UNSET,
    fields: Union[
        Unset, None, str
    ] = "$type,activities($type,added,author($type,id,login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter,hasBefore,id",
) -> Response[Any]:
    """
    Args:
        categories (Union[Unset, None, str]):
        reverse (Union[Unset, None, bool]):
        start (Union[Unset, None, str]):
        end (Union[Unset, None, str]):
        author (Union[Unset, None, str]):
        issue_query (Union[Unset, None, str]):
        cursor (Union[Unset, None, str]):
        activity_id (Union[Unset, None, str]):
        fields (Union[Unset, None, str]):  Default: '$type,activities($type,added,author($type,id,
            login,ringId),category($type,id),field($type,customField($type,fieldType($type,id),id,loca
            lizedName,name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCurso
            r,hasAfter,hasBefore,id'. Example: $type,activities($type,added,author($type,id,login,ring
            Id),category($type,id),field($type,customField($type,fieldType($type,id),id,localizedName,
            name),id,name),id,removed,target,targetMember,timestamp),afterCursor,beforeCursor,hasAfter
            ,hasBefore,id.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        categories=categories,
        reverse=reverse,
        start=start,
        end=end,
        author=author,
        issue_query=issue_query,
        cursor=cursor,
        activity_id=activity_id,
        fields=fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
