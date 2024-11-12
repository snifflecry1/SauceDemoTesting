# Bug Report

## B-01

**Title:**
Invalid response findByStatus endpoint

**Description:**
When searching for a pet using an invalid status value, response gives incorrect status code 200 instead of 400

**Environment:** Pytest

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_find_pets_invalid_status
2. Checkout output using 38 as a status value

**Expected Result:**
Response should give invalid status code 400

**Actual Result:**
Response is empty with status code of 200

**Severity:**
Minor, could be slightly misleading if users rely on status codes to validate inputs and are expecting 400s but does not impact data integrity, application stability, or security

**Priority:**
P3, The priority level of P3 fits if we consider that this bug doesn’t prevent core functionality and is not likely to significantly disrupt the user experience

## B-02

**Title:**
Invalid status code find by invalid pet ID

**Description:**
When searching for a pet using an invalid pet id, response gives incorrect status code 404

**Environment:** Pytest

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_find_pet from file test_petstore.py

**Expected Result:**
Response should be invalid with status code 400

**Actual Result:**
Response status code is 404

**Severity:**
Minor, Returning 404 for an invalid pet ID may cause minor confusion for users expecting a 400 for malformed input, but it doesn't affect the actual operation or integrity of the service.

**Priority:**
P3, This is primarily a usability and consistency issue

## B-03

**Title:**
Invalid status code update pet by form

**Description:**
When updating a pet from form data using invalid data the requests completes successfully 

**Environment:** Pytest

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_update_pet_form from file test_petstore.py

**Expected Result:**
Response should be empty with a status code of 400

**Actual Result:**
Response is successful with status code of 200

**Severity:**
Moderate, If the server accepts invalid form data without error, it could potentially lead to silent data issues or incorrect records being saved if not caught by the client

**Priority:**
P2, Developers relying on the API would expect it to reject invalid data, and if the server silently accepts this data, it could cause errors in downstream systems or require additional client-side validation as a workaround

## B-04

**Title:**
Update existing pet functionality incorrect

**Description:**
When updating an existing pet using an id that shouldn't exist, since the endpoint is set to use a put request, any non existent id can be used and will be created if it doesn't exist 


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. In the pet section of the api click "try it out" beside "update an existing pet"
2. In the body field try a long integer that doesn't exist on the db for the "id" field
3. Press execute

**Expected Result:**
Response should be a 404

**Actual Result:**
Response is successful with status code of 200, object is created

**Severity:**
Major, This could lead to data integrity issues if users or client applications unknowingly create new records by sending incorrect or non-existent IDs

**Priority:**
P1, Developers using the API may assume that invalid PUT requests won’t alter the system state, so addressing this promptly is critical to avoid unintended side effects

## B-05

**Title:**
Update existing pet functionality unhandled exception

**Description:**
When sending an invalid data type (string) for the pet_id field using automated tests, the server returns a 500 Internal Server Error instead of a 400 Bad Request. This discrepancy occurs even though the Swagger interface correctly prevents sending invalid types with client-side validation.

**Environment:** Pytest

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_update_existing_pet
2. Check output of test using "test" as the pet_id

**Expected Result:**
Response status code should be a 400 invalid data type

**Actual Result:**
Response return status code 500

**Severity:**
Minor, This bug is an error-handling issue rather than a functional failure that impacts data or application logic

**Priority:**
P3, This is primarily a usability improvement. API clients expect well-handled errors

## B-06

**Title:**
Delete endpoint invalid id status code

**Description:**
Deleting a pet using an invalid status code gives a 404 response instead of a 400

**Environment:** Pytest

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_delete_pet
2. Check output of test using "[abcde]" as the pet_id

**Expected Result:**
Response status code should be a 400 invalid data type

**Actual Result:**
Response return status code 500

**Severity:**
Moderate, This could lead to client applications spending unnecessary time troubleshooting resource existence issues rather than identifying formatting problems

**Priority:**
P2, It could disrupt client workflows by causing users to misinterpret the status code, potentially leading to extra troubleshooting efforts

## B-07

**Title:**
Create pet with non format data

**Description:**
When creating a pet using data that does not follow the expected format, the response should return a 400

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_add_pet_success
2. Check output of test that uses 343552 as an id

**Expected Result:**
Response status code should be a 400 invalid data type

**Actual Result:**
Response returns status code 200

**Severity:**
Moderate, Indicates that the API accepts malformed or incorrect data without proper validation

**Priority:**
P2, Prompt correction is necessary to prevent malformed data from entering the system

## B-08

**Title:**
Unhandled exception with inventory order

**Description:**
When making an inventory order on endpoint /store/order using invalid data, the response triggers a 500 server error

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_create_order
2. Check output of 2nd test thats using invalid data

**Expected Result:**
Response status code should be a 400 invalid data type

**Actual Result:**
Response returns status code 500

**Severity:**
Minor, does not impact core functionality of API

**Priority:**
P4, Low priority only improving API usability 

## B-09

**Title:**
Incorrect status code on non existent 

**Description:**
When making an inventory order on endpoint /store/order using a petID that doesn't exist, the response is a 200 even though no new order is added to the database

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_create_order
2. Check output of 3rd test thats using invalid data

**Expected Result:**
Response status code should be a 404 

**Actual Result:**
Response returns status code 200

**Severity:**
Moderate, Affects the accuracy of the response without directly disrupting core functionality

**Priority:**
P2, Fixing this to return the correct status code would improve the API’s reliability and help developers handle non-existent data scenarios correctly

## B-10

**Title:**
Incorrect status code on invalid id

**Description:**
When searching for an order based on an id thats not an integer, the server returns a 404

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_get_order_id
2. Check output of 3rd test thats using invalid data

**Expected Result:**
Response status code should be a 400

**Actual Result:**
Response returns status code 404

**Severity:**
Minor, Only impacts the accuracy of the status code without affecting the core functionality or data integrity

**Priority:**
P4, This is a lower-priority usability fix

## B-11

**Title:**
Incorrect status code on invalid id

**Description:**
When deleting an order based on an id thats not an integer, the server returns a 404

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_delete_order_id
2. Check output of 3rd test thats using invalid data

**Expected Result:**
Response status code should be a 400

**Actual Result:**
Response returns status code 404

**Severity:**
Minor, This bug is primarily an error-handling issue and doesn’t affect core functionality, data integrity, or user workflows

**Priority:**
P4,  Correcting the error code would improve usability and help developers interpret the API’s responses accurately, but it’s not urgent and doesn’t impact critical workflows

## B-12

**Title:**
Server error on invalid data when creating user

**Description:**
When creating a user using invalid data, there is an internal server error 500

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_create_user_with_list
2. Check output of 2nd test thats using invalid data

**Expected Result:**
Response status code should be a 400

**Actual Result:**
Response returns status code 500

**Severity:**
Minor, Issue is related to error handling rather than a functional breakdown

**Priority:**
P3, Addressing bug would improve the API’s usability and provide more informative feedback to clients

## B-13

**Title:**
Invalid data when retrieving users returns wrong status code

**Description:**
When retrieving a user using invalid data, the response is a 404

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_get_user
2. Check output of 2nd test thats using invalid data

**Expected Result:**
Response status code should be a 400 using an integer

**Actual Result:**
Response returns status code 404

**Severity:**
Minor, This bug relates to error feedback accuracy rather than core functionality or data integrity

**Priority:**
P3, Resolving this bug isn’t urgent, as it doesn’t hinder functionality or require immediate attention, but it does contribute to a better developer experience by making error handling more consistent

## B-14

**Title:**
Invalid status code when updating a user with invalid data

**Description:**
When updating a user using invalid data, the response is a 200

**Environment:** Pytest

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_update_user
2. Check output of 3rd test thats using invalid data

**Expected Result:**
Response status code should be a 400 using an integer

**Actual Result:**
Response returns status code 200

**Severity:**
Moderate, This can mislead developers into thinking the data was accepted as valid

**Priority:**
P3, This would improve the API’s reliability by ensuring data validation is properly enforced

## B-15

**Title:**
Invalid status code when updating a user with large integer data

**Description:**
When updating a user using an very large id number, we get a 500 server error

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_update_user
2. Check output of 2nd test thats using a large integer for the id value

**Expected Result:**
Response status code should be a 400 status code

**Actual Result:**
Response returns status code 500

**Severity:**
Moderate, Indicates that the server is failing to handle an invalid input gracefully

**Priority:**
P1, If this endpoint is used frequently or exposed to various client applications, having it return a consistent and expected error response would enhance the stability of the API and reduce the risk of additional server load from unhandled errors

## B-16

**Title:**
Invalid status code during login with invalid username and password

**Description:**
When logging in using an integer for username and password, the server returns a 200 response

**Environment:** Pytest


**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_user_login
2. Check output of 2nd test thats using integers as username and password

**Expected Result:**
Response status code should be a 400 status code

**Actual Result:**
Response returns status code 200

**Severity:**
Moderate, Incorrect handling of input validation for login credentials, a critical operation in any API

**Priority:**
P1, Incorrect handling of login data types should be a priority issue in APIs where accurate and secure authentication is required