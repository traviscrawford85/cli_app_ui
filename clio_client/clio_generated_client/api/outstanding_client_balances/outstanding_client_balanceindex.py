import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.outstanding_client_balance_list import OutstandingClientBalanceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    last_paid_end_date: Union[Unset, datetime.date] = UNSET,
    last_paid_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    newest_bill_due_end_date: Union[Unset, datetime.date] = UNSET,
    newest_bill_due_start_date: Union[Unset, datetime.date] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_api_version, Unset):
        headers["X-API-VERSION"] = x_api_version

    params: dict[str, Any] = {}

    params["contact_id"] = contact_id

    params["fields"] = fields

    json_last_paid_end_date: Union[Unset, str] = UNSET
    if not isinstance(last_paid_end_date, Unset):
        json_last_paid_end_date = last_paid_end_date.isoformat()
    params["last_paid_end_date"] = json_last_paid_end_date

    json_last_paid_start_date: Union[Unset, str] = UNSET
    if not isinstance(last_paid_start_date, Unset):
        json_last_paid_start_date = last_paid_start_date.isoformat()
    params["last_paid_start_date"] = json_last_paid_start_date

    params["limit"] = limit

    json_newest_bill_due_end_date: Union[Unset, str] = UNSET
    if not isinstance(newest_bill_due_end_date, Unset):
        json_newest_bill_due_end_date = newest_bill_due_end_date.isoformat()
    params["newest_bill_due_end_date"] = json_newest_bill_due_end_date

    json_newest_bill_due_start_date: Union[Unset, str] = UNSET
    if not isinstance(newest_bill_due_start_date, Unset):
        json_newest_bill_due_start_date = newest_bill_due_start_date.isoformat()
    params["newest_bill_due_start_date"] = json_newest_bill_due_start_date

    params["originating_attorney_id"] = originating_attorney_id

    params["page_token"] = page_token

    params["responsible_attorney_id"] = responsible_attorney_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/outstanding_client_balances",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, OutstandingClientBalanceList]]:
    if response.status_code == 200:
        response_200 = OutstandingClientBalanceList.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, OutstandingClientBalanceList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    last_paid_end_date: Union[Unset, datetime.date] = UNSET,
    last_paid_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    newest_bill_due_end_date: Union[Unset, datetime.date] = UNSET,
    newest_bill_due_start_date: Union[Unset, datetime.date] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, OutstandingClientBalanceList]]:
    """Return the data for all OutstandingClientBalances

     Outlines the parameters, optional and required, used when requesting the data for all
    OutstandingClientBalances

    Args:
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        last_paid_end_date (Union[Unset, datetime.date]):
        last_paid_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        newest_bill_due_end_date (Union[Unset, datetime.date]):
        newest_bill_due_start_date (Union[Unset, datetime.date]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, OutstandingClientBalanceList]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        fields=fields,
        last_paid_end_date=last_paid_end_date,
        last_paid_start_date=last_paid_start_date,
        limit=limit,
        newest_bill_due_end_date=newest_bill_due_end_date,
        newest_bill_due_start_date=newest_bill_due_start_date,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        responsible_attorney_id=responsible_attorney_id,
        x_api_version=x_api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    last_paid_end_date: Union[Unset, datetime.date] = UNSET,
    last_paid_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    newest_bill_due_end_date: Union[Unset, datetime.date] = UNSET,
    newest_bill_due_start_date: Union[Unset, datetime.date] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, OutstandingClientBalanceList]]:
    """Return the data for all OutstandingClientBalances

     Outlines the parameters, optional and required, used when requesting the data for all
    OutstandingClientBalances

    Args:
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        last_paid_end_date (Union[Unset, datetime.date]):
        last_paid_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        newest_bill_due_end_date (Union[Unset, datetime.date]):
        newest_bill_due_start_date (Union[Unset, datetime.date]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, OutstandingClientBalanceList]
    """

    return sync_detailed(
        client=client,
        contact_id=contact_id,
        fields=fields,
        last_paid_end_date=last_paid_end_date,
        last_paid_start_date=last_paid_start_date,
        limit=limit,
        newest_bill_due_end_date=newest_bill_due_end_date,
        newest_bill_due_start_date=newest_bill_due_start_date,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        responsible_attorney_id=responsible_attorney_id,
        x_api_version=x_api_version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    last_paid_end_date: Union[Unset, datetime.date] = UNSET,
    last_paid_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    newest_bill_due_end_date: Union[Unset, datetime.date] = UNSET,
    newest_bill_due_start_date: Union[Unset, datetime.date] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, OutstandingClientBalanceList]]:
    """Return the data for all OutstandingClientBalances

     Outlines the parameters, optional and required, used when requesting the data for all
    OutstandingClientBalances

    Args:
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        last_paid_end_date (Union[Unset, datetime.date]):
        last_paid_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        newest_bill_due_end_date (Union[Unset, datetime.date]):
        newest_bill_due_start_date (Union[Unset, datetime.date]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, OutstandingClientBalanceList]]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        fields=fields,
        last_paid_end_date=last_paid_end_date,
        last_paid_start_date=last_paid_start_date,
        limit=limit,
        newest_bill_due_end_date=newest_bill_due_end_date,
        newest_bill_due_start_date=newest_bill_due_start_date,
        originating_attorney_id=originating_attorney_id,
        page_token=page_token,
        responsible_attorney_id=responsible_attorney_id,
        x_api_version=x_api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    contact_id: Union[Unset, int] = UNSET,
    fields: Union[Unset, str] = UNSET,
    last_paid_end_date: Union[Unset, datetime.date] = UNSET,
    last_paid_start_date: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = UNSET,
    newest_bill_due_end_date: Union[Unset, datetime.date] = UNSET,
    newest_bill_due_start_date: Union[Unset, datetime.date] = UNSET,
    originating_attorney_id: Union[Unset, int] = UNSET,
    page_token: Union[Unset, str] = UNSET,
    responsible_attorney_id: Union[Unset, int] = UNSET,
    x_api_version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, OutstandingClientBalanceList]]:
    """Return the data for all OutstandingClientBalances

     Outlines the parameters, optional and required, used when requesting the data for all
    OutstandingClientBalances

    Args:
        contact_id (Union[Unset, int]):
        fields (Union[Unset, str]):
        last_paid_end_date (Union[Unset, datetime.date]):
        last_paid_start_date (Union[Unset, datetime.date]):
        limit (Union[Unset, int]):
        newest_bill_due_end_date (Union[Unset, datetime.date]):
        newest_bill_due_start_date (Union[Unset, datetime.date]):
        originating_attorney_id (Union[Unset, int]):
        page_token (Union[Unset, str]):
        responsible_attorney_id (Union[Unset, int]):
        x_api_version (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, OutstandingClientBalanceList]
    """

    return (
        await asyncio_detailed(
            client=client,
            contact_id=contact_id,
            fields=fields,
            last_paid_end_date=last_paid_end_date,
            last_paid_start_date=last_paid_start_date,
            limit=limit,
            newest_bill_due_end_date=newest_bill_due_end_date,
            newest_bill_due_start_date=newest_bill_due_start_date,
            originating_attorney_id=originating_attorney_id,
            page_token=page_token,
            responsible_attorney_id=responsible_attorney_id,
            x_api_version=x_api_version,
        )
    ).parsed
