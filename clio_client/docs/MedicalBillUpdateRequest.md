# MedicalBillUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MedicalBillUpdateRequestData**](MedicalBillUpdateRequestData.md) |  | 

## Example

```python
from clio_sdk.models.medical_bill_update_request import MedicalBillUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MedicalBillUpdateRequest from a JSON string
medical_bill_update_request_instance = MedicalBillUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MedicalBillUpdateRequest.to_json())

# convert the object into a dict
medical_bill_update_request_dict = medical_bill_update_request_instance.to_dict()
# create an instance of MedicalBillUpdateRequest from a dict
medical_bill_update_request_from_dict = MedicalBillUpdateRequest.from_dict(medical_bill_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


