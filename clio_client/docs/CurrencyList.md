# CurrencyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Currency]**](Currency.md) | Currency List Response | 

## Example

```python
from clio_sdk.models.currency_list import CurrencyList

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyList from a JSON string
currency_list_instance = CurrencyList.from_json(json)
# print the JSON string representation of the object
print(CurrencyList.to_json())

# convert the object into a dict
currency_list_dict = currency_list_instance.to_dict()
# create an instance of CurrencyList from a dict
currency_list_from_dict = CurrencyList.from_dict(currency_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


