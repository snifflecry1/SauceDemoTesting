# Test Strategy

## Overview

### SauceDemo website

Is a commerce website that allows user to purchase items in a cart to be paid for via a payment card

### Purpose

This document outlines the test strategy for ensuring the quality and stability of the SauceDemo user interface. The primary objective is to verify that core functionalities work as expected across different browsers and devices, providing a smooth and reliable experience for end-users.

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

A section of this testing will be dedicated to exploring how features work on SauceDemo followed by suitable functional testing on noted areas afterwards

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

# Test Plans









# Decisions and Reasons

