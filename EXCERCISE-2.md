# EXERCISE-2.md

## Overview of the Test Approach
For this exercise, the objective was to implement automated REST API tests for the [Petstore API](https://petstore.swagger.io/), focusing on validating API functionality for creating, updating, retrieving, and deleting data. Tests were designed to cover:
- **Basic CRUD operations** across various endpoints, such as `/pet`, `/store/order`, and `/user`.
- **Validation of HTTP status codes** for both expected and unexpected inputs, ensuring that the API responds correctly with `200 OK`, `400 Bad Request`, `404 Not Found`, etc.
- **Input validation**, including correct and incorrect data types, formats, and edge cases (e.g., very large integers or invalid strings).
  
## Structure of Test Cases
Test cases are organized to cover the following main categories:
- **Pet Entity Tests**: Tests for endpoints related to the `Pet` entity, including updating pet details, searching by status, handling invalid statuses, and deleting pets. These tests validate that responses match the expected status codes and handle incorrect inputs gracefully.
- **Store Entity Tests**: Tests related to order management in the store. Cases include creating orders with valid and invalid data, checking the inventory, and deleting orders.
- **User Entity Tests**: Tests for user-related endpoints, including creating users (individually and with a list), updating user details, retrieving users, and login/logout functionalities. Special attention was given to handling incorrect input types and missing fields.

## Assumptions and Constraints
Some assumptions and constraints influenced the test design:
- **Authentication**: Since the Petstore API does not require authentication for most endpoints, tests were written without token-based authorization. If implemented, additional tests for secured endpoints would be needed.
- **Invalid Data Handling**: In cases where the API did not handle certain invalid inputs as expected, such as returning a `500 Internal Server Error` instead of a `400 Bad Request`, I noted these behaviors in the bug reports (e.g., using very large integers or strings where the API expected integers).
- **Lack of Documentation for Edge Cases**: Certain edge case behaviors, like specific error responses for invalid data types, were not fully documented. Where necessary, assumptions were made about expected behavior, such as the API returning a `400 Bad Request` for malformed requests.

## Test Execution Instructions
See PetShop section of README.md for setup and running instructions
