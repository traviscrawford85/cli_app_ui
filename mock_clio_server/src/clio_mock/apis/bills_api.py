# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.bills_api_base import BaseBillsApi
import clio_mock.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from clio_mock.models.extra_models import TokenModel  # noqa: F401
from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.bill_update_request import BillUpdateRequest
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/bills/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Bills"],
    summary="Delete or void a Bill",
    response_model_by_alias=True,
)
async def bill_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """This endpoint will transition a bill to either its deleted or voided state. A bill can only be deleted or voided if it has no payments recorded and its current state is one of the following: * Draft * Pending Approval * Unpaid  A bill will automatically be moved to a deleted or void state based on its current state. The mappings for this are: * Draft -&gt; Deleted * Pending Approval -&gt; Deleted * Unpaid -&gt; Void """
    if not BaseBillsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillsApi.subclasses[0]().bill_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/bills.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Bills"],
    summary="Return the data for all Bills",
    response_model_by_alias=True,
)
async def bill_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    client_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.", alias="client_idquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    currency_idquery: Annotated[Optional[StrictInt], Field(description="Filter Bill records to those of a specific currency.")] = Query(None, description="Filter Bill records to those of a specific currency.", alias="currency_idquery"),
    custom_field_valuesquery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")] = Query(None, description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; ", alias="custom_field_valuesquery"),
    due_afterquery: Annotated[Optional[date], Field(description="Filter Bill records to those that have a `due_date` after the one provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Bill records to those that have a &#x60;due_date&#x60; after the one provided (Expects an ISO-8601 date).", alias="due_afterquery"),
    due_atquery: Annotated[Optional[date], Field(description="Filter Bill records to those that have a specific `due_date` (Expects an ISO-8601 date).")] = Query(None, description="Filter Bill records to those that have a specific &#x60;due_date&#x60; (Expects an ISO-8601 date).", alias="due_atquery"),
    due_beforequery: Annotated[Optional[date], Field(description="Filter Bill records to those that have a `due_date` before the one provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Bill records to those that have a &#x60;due_date&#x60; before the one provided (Expects an ISO-8601 date).", alias="due_beforequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    issued_afterquery: Annotated[Optional[date], Field(description="Filter Bill records to those that have an `issue_date` after the one provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Bill records to those that have an &#x60;issue_date&#x60; after the one provided (Expects an ISO-8601 date).", alias="issued_afterquery"),
    issued_beforequery: Annotated[Optional[date], Field(description="Filter Bill records to those that have an `issue_date` before the one provided (Expects an ISO-8601 date).")] = Query(None, description="Filter Bill records to those that have an &#x60;issue_date&#x60; before the one provided (Expects an ISO-8601 date).", alias="issued_beforequery"),
    last_sent_end_datequery: Annotated[Optional[date], Field(description="Filter Bill records for those whose bills have been sent before the specified date")] = Query(None, description="Filter Bill records for those whose bills have been sent before the specified date", alias="last_sent_end_datequery"),
    last_sent_start_datequery: Annotated[Optional[date], Field(description="Filter Bill records for those whose bills have been sent after the specified date")] = Query(None, description="Filter Bill records for those whose bills have been sent after the specified date", alias="last_sent_start_datequery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="matter_idquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    originating_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="originating_attorney_idquery"),
    overdue_onlyquery: Annotated[Optional[StrictBool], Field(description="Filter Bill records to those that are overdue.")] = Query(None, description="Filter Bill records to those that are overdue.", alias="overdue_onlyquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="responsible_attorney_idquery"),
    statequery: Annotated[Optional[StrictStr], Field(description="Filter Bill records to those in a given state.")] = Query(None, description="Filter Bill records to those in a given state.", alias="statequery"),
    statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")] = Query(None, description="Filter Activity records to those that are draft, billed, unbilled or non-billable.", alias="statusquery"),
    typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")] = Query(None, description="Filter Activity records to those of a specific type.", alias="typequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Bills"""
    if not BaseBillsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillsApi.subclasses[0]().bill_index(x_api_versio_nheader, client_idquery, created_sincequery, currency_idquery, custom_field_valuesquery, due_afterquery, due_atquery, due_beforequery, fieldsquery, idsquery, issued_afterquery, issued_beforequery, last_sent_end_datequery, last_sent_start_datequery, limitquery, matter_idquery, orderquery, originating_attorney_idquery, overdue_onlyquery, page_tokenquery, queryquery, responsible_attorney_idquery, statequery, statusquery, typequery, updated_sincequery)


@router.get(
    "/bills/{id}/preview.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Bills"],
    summary="Returns the pre-rendered html for the Bill",
    response_model_by_alias=True,
)
async def bill_preview(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
) -> ActivityList:
    """This endpoint returns a pre-rendered HTML object that you can use to view a preview of your bills. The HTML provided contains all of the CSS rules it requires to show the bill correctly, as well as the DOCTYPE setting it requires. It&#39;s best to use an iframe, or similar object, to render the results of this endpoint. """
    if not BaseBillsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillsApi.subclasses[0]().bill_preview(idpath)


@router.get(
    "/bills/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Bills"],
    summary="Return the data for a single Bill",
    response_model_by_alias=True,
)
async def bill_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    navigation_nextquery: Annotated[Optional[StrictInt], Field(description="The id of the next *Bill* available for viewing")] = Query(None, description="The id of the next *Bill* available for viewing", alias="navigation.nextquery"),
    navigation_previousquery: Annotated[Optional[StrictInt], Field(description="The id of the previous *Bill* available for viewing")] = Query(None, description="The id of the previous *Bill* available for viewing", alias="navigation.previousquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Bill"""
    if not BaseBillsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillsApi.subclasses[0]().bill_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, fieldsquery, navigation_nextquery, navigation_previousquery)


@router.patch(
    "/bills/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Bills"],
    summary="Update a single Bill",
    response_model_by_alias=True,
)
async def bill_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    bill_update_request: Annotated[Optional[BillUpdateRequest], Field(description="Request Body for Bills")] = Body(None, description="Request Body for Bills"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Bill"""
    if not BaseBillsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillsApi.subclasses[0]().bill_update(idpath, if_matc_hheader, x_api_versio_nheader, fieldsquery, bill_update_request)
