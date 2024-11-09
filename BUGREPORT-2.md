# Bug Report

## B-01

**Title:**
Invalid response findByStatus endpoint

**Description:**
When searching for a pet using an invalid status value, response gives incorrect status code 200

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_find_pets_invalid_status from file test_petstore.py

**Expected Result:**
Response should be empty with a status code of 400

**Actual Result:**
Response is empty with status code of 400

**Severity:**
Minor

**Priority:**
P3

## B-02

**Title:**
Invalid status code find by invalid pet ID

**Description:**
When searching for a pet using an invalid pet id, response gives incorrect status code 404

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_find_pet from file test_petstore.py

**Expected Result:**
Response should be empty with a status code of 404

**Actual Result:**
Response is empty with status code of 400

**Severity:**
Minor

**Priority:**
P3

## B-03

**Title:**
Invalid status code update pet by form

**Description:**
When updating a pet from form data using invalid data the requests completes successfully 

**Prerequisite:** User should have access https://petstore.swagger.io/ to see API behaviour

**Steps to reproduce**

1. Run test test_update_pet_form from file test_petstore.py

**Expected Result:**
Response should be empty with a status code of 400

**Actual Result:**
Response is successful with status code of 200

**Severity:**
Moderate

**Priority:**
P2