# clio_sdk.BankTransactionsApi

All URIs are relative to *https://app.clio.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_transaction_index**](BankTransactionsApi.md#bank_transaction_index) | **GET** /bank_transactions | Return the data for all BankTransactions
[**bank_transaction_show**](BankTransactionsApi.md#bank_transaction_show) | **GET** /bank_transactions/{id} | Return the data for a single BankTransaction


# **bank_transaction_index**
> BankTransactionList bank_transaction_index(x_api_version=x_api_version, bank_account_id=bank_account_id, client_id=client_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, type=type, updated_since=updated_since)

Return the data for all BankTransactions

Outlines the parameters, optional and required, used when requesting the data for all BankTransactions

### Example


```python
import clio_sdk
from clio_sdk.models.bank_transaction_list import BankTransactionList
from clio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.clio.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = clio_sdk.Configuration(
    host = "https://app.clio.com/api/v4"
)


# Enter a context with an instance of the API client
with clio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clio_sdk.BankTransactionsApi(api_client)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    bank_account_id = 56 # int | The unique identifier for a single BankAccount. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property. (optional)
    client_id = 56 # int | The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property. (optional)
    created_since = '2013-10-20T19:20:30+01:00' # datetime | Filter BankTransaction records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)
    ids = 56 # int | Filter BankTransaction records to those having the specified unique identifiers. (optional)
    limit = 56 # int | A limit on the number of BankTransaction records to be returned. Limit can range between 1 and 200. Default: `200`. (optional)
    matter_id = 56 # int | The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property. (optional)
    order = 'order_example' # str | Orders the BankTransaction records by the given field. Default: `id(asc)`. (optional)
    page_token = 'page_token_example' # str | A token specifying which page to return. (optional)
    type = 'type_example' # str | Filter BankTransaction records to those having a specific type. (optional)
    updated_since = '2013-10-20T19:20:30+01:00' # datetime | Filter BankTransaction records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp). (optional)

    try:
        # Return the data for all BankTransactions
        api_response = api_instance.bank_transaction_index(x_api_version=x_api_version, bank_account_id=bank_account_id, client_id=client_id, created_since=created_since, fields=fields, ids=ids, limit=limit, matter_id=matter_id, order=order, page_token=page_token, type=type, updated_since=updated_since)
        print("The response of BankTransactionsApi->bank_transaction_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transaction_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **bank_account_id** | **int**| The unique identifier for a single BankAccount. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property. | [optional] 
 **client_id** | **int**| The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property. | [optional] 
 **created_since** | **datetime**| Filter BankTransaction records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 
 **ids** | **int**| Filter BankTransaction records to those having the specified unique identifiers. | [optional] 
 **limit** | **int**| A limit on the number of BankTransaction records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;. | [optional] 
 **matter_id** | **int**| The unique identifier for a single Matter. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property. | [optional] 
 **order** | **str**| Orders the BankTransaction records by the given field. Default: &#x60;id(asc)&#x60;. | [optional] 
 **page_token** | **str**| A token specifying which page to return. | [optional] 
 **type** | **str**| Filter BankTransaction records to those having a specific type. | [optional] 
 **updated_since** | **datetime**| Filter BankTransaction records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp). | [optional] 

### Return type

[**BankTransactionList**](BankTransactionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_transaction_show**
> BankTransactionShow bank_transaction_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)

Return the data for a single BankTransaction

Outlines the parameters, optional and required, used when requesting the data for a single BankTransaction

### Example


```python
import clio_sdk
from clio_sdk.models.bank_transaction_show import BankTransactionShow
from clio_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.clio.com/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = clio_sdk.Configuration(
    host = "https://app.clio.com/api/v4"
)


# Enter a context with an instance of the API client
with clio_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clio_sdk.BankTransactionsApi(api_client)
    id = 56 # int | The unique identifier for the BankTransaction.
    if_modified_since = '2013-10-20' # date | The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). (optional)
    if_none_match = 'if_none_match_example' # str | The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed. (optional)
    x_api_version = 'x_api_version_example' # str | The [API minor version](#section/Minor-Versions). Default: latest version. (optional)
    fields = 'fields_example' # str | The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). (optional)

    try:
        # Return the data for a single BankTransaction
        api_response = api_instance.bank_transaction_show(id, if_modified_since=if_modified_since, if_none_match=if_none_match, x_api_version=x_api_version, fields=fields)
        print("The response of BankTransactionsApi->bank_transaction_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BankTransactionsApi->bank_transaction_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique identifier for the BankTransaction. | 
 **if_modified_since** | **date**| The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp). | [optional] 
 **if_none_match** | **str**| The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed. | [optional] 
 **x_api_version** | **str**| The [API minor version](#section/Minor-Versions). Default: latest version. | [optional] 
 **fields** | **str**| The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields). | [optional] 

### Return type

[**BankTransactionShow**](BankTransactionShow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests |  -  |
**304** | Not Modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

