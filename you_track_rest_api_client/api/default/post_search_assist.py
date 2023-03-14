from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.search_suggestions import SearchSuggestions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: SearchSuggestions,
    fields: Union[
        Unset, None, str
    ] = "$type,id,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Dict[str, Any]:
    url = "{}/search/assist".format(client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[SearchSuggestions]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchSuggestions.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[SearchSuggestions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SearchSuggestions,
    fields: Union[
        Unset, None, str
    ] = "$type,id,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Response[SearchSuggestions]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,id,suggestions($type,caret,completionEn
            d,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)'.
            Example: $type,id,suggestions($type,caret,completionEnd,completionStart,description,id,mat
            chingEnd,matchingStart,option,prefix,suffix).
        json_body (SearchSuggestions): Represents the list of search suggestions for the currently
            entered search query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSuggestions]
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
    json_body: SearchSuggestions,
    fields: Union[
        Unset, None, str
    ] = "$type,id,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Optional[SearchSuggestions]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,id,suggestions($type,caret,completionEn
            d,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)'.
            Example: $type,id,suggestions($type,caret,completionEnd,completionStart,description,id,mat
            chingEnd,matchingStart,option,prefix,suffix).
        json_body (SearchSuggestions): Represents the list of search suggestions for the currently
            entered search query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSuggestions]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SearchSuggestions,
    fields: Union[
        Unset, None, str
    ] = "$type,id,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Response[SearchSuggestions]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,id,suggestions($type,caret,completionEn
            d,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)'.
            Example: $type,id,suggestions($type,caret,completionEnd,completionStart,description,id,mat
            chingEnd,matchingStart,option,prefix,suffix).
        json_body (SearchSuggestions): Represents the list of search suggestions for the currently
            entered search query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSuggestions]
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
    json_body: SearchSuggestions,
    fields: Union[
        Unset, None, str
    ] = "$type,id,suggestions($type,caret,completionEnd,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)",
) -> Optional[SearchSuggestions]:
    """
    Args:
        fields (Union[Unset, None, str]):  Default: '$type,id,suggestions($type,caret,completionEn
            d,completionStart,description,id,matchingEnd,matchingStart,option,prefix,suffix)'.
            Example: $type,id,suggestions($type,caret,completionEnd,completionStart,description,id,mat
            chingEnd,matchingStart,option,prefix,suffix).
        json_body (SearchSuggestions): Represents the list of search suggestions for the currently
            entered search query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchSuggestions]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            fields=fields,
        )
    ).parsed
