# Test Strategy

## Overview

### SauceDemo website

Is a commerce website that allows user to purchase items in a cart to be paid for via a payment card

### Purpose

This document outlines the test strategy for ensuring the quality and stability of the SauceDemo user interface. The primary objective is to verify that core functionalities work as expected on the chosen browser providing a smooth and reliable experience for end-users.

## Scope

The set of features that will be included for testing will be:
- Log in
- Product search
- Filtering
- Cart
- Checkout

#### Note

For the purpose of this projects since access is limited to the UI any backend features will be out of scope for this project

#### Browser

Testing will be carried out using Chrome

## Types of testing

#### Exploratory testing

A section of each test plan will be dedicated to exploring how that feature works on SauceDemo followed by a suite of tests per feature

 Other testing to be included in this project:


- Functional testing
    - Integration testing
    
        Testing whole features comes under this type of testing
    - Note (unit testing)

        Unit testing will be out of scope for this project with no access to the codebase
        
- End to end testing

    Testing here will include from logging in to finishing a purchase of items in the cart on SauceDemo


## Tools and Frameworks

**Framework** 

Pytest with selenium will be used for its ease of use to make requests to SauceDemo and can structure the test libraries in a clear and concise manner

**Driver**: ChromeDriver

**Test Reporting**: Pytest HTML report

**CI/CD Integration**: Docker with Jenkins

## Test Execution 

**CI-Based Execution**

 *Needs to be filled in at the end explaining exactly how jenkins will be set up in a docker container to run the tests* 

###  Test Prioritization 

*Possible piece on prioritization of tests ? Critical paths, High, Medium, Low Priority tests*

### Bug Reporting

Any bugs found during the testing process will be documented in [BUGREPORT-1.md](/BUGREPORT-1.md) in the following format:

 - Bug ID
 - Title
 - Description
 - Steps to reproduce
 - Expected Result
 - Actual Result
 - Severity
 - Priority
 - Attachments

# Test Plans

## Log in

### Overview

The objective here is to verify the core functionality of the log in mechanism and documenting any bugs found in the process

### Test Scope

Tests that will be in scope will be predictable tests like testing with valid/invalid/empty credentials as well as time to log in

Tests that will be out of scope will include any load testing with the login mechanism to keep in line with functional verification primarily

### Test types

- Functional
- Negative
- Exploratory 

### Exploratory Testing Findings
 During testing, it was discovered that the system implements a user lockout mechanism, restricting access from logging in. This was added as a test case (TC-03) as a result

### Test Cases

**Index**

1. [TC-01-Verify successful login with valid credentials](#tc-01)
2. [TC-02-Verify invalid login with invalid credentials](#tc-02)
3. [TC-03-Verify locked user](#tc-03)

<a name="tc-01"></a>
**Test Case ID:** TC-01

**Title**: Verify successful login with valid credentials

**Objective:** Ensure users can log in with valid username and password

**Preconditions:** User had valid account, user on login page

**Steps:**

1. Enter valid username (Refer to Test Data Section)
2. Enter valid password (Refer to Test Data Section)
3. Click login

![alt text](screenshots/image.png)

**Expected Result:**

User redirected to site homepage without delay

![alt text](screenshots/image-1.png)

<a name="tc-02"></a>
**Test Case ID:** TC-02

**Title**: Verify invalid login with invalid credentials

**Objective:** Ensure users can't log in with invalid username and password

**Preconditions:** User on login page

**Steps:**

1. Enter invalid username
2. Enter invalid password
3. Click login

![alt text](screenshots/image-3.png)

**Expected Result:**

User gets invalid login error

![alt text](screenshots/image-4.png)

<a name="tc-03"></a>
**Test Case ID:** TC-03

**Title**: Verify locked user

**Objective:** Verify a user can't log in if they're a locked user

**Preconditions:** User has account that is locked account, User on login page

**Steps:**

1. Enter valid username (Refer to Test Data section)
2. Enter valid password (Refer to Test Data section)
3. Click login

![alt text](screenshots/image-5.png)

**Expected Result:**

User gets locked out error

![alt text](screenshots/image-6.png)

### Test Data

**Valid Login - TC-01**

Username: standard_user

Password: secret_sauce

**Locked Login - TC-03**

Username: locked_out_user

Password: secret_sauce

# Decisions and Reasons

