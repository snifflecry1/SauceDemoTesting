import requests
import json
import pytest
import tempfile
import logging
from datetime import datetime

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://petstore.swagger.io/v2"

class TestPetEntity:

    @pytest.mark.parametrize("pet_id, code", [
        (13, 200),
        ("test", 400),
        (40000002342423423, 404),
        (13, 405)
    ])
    def test_update_existing_pet(self, pet_id, code):
        """Verify update existing pet functionality"""
        logger.info(f"Testing update for pet with ID: {pet_id} expecting status code: {code}")
        url = f"{BASE_URL}/pet"
        data = {
            "id": pet_id,
            "category": {"id": 0, "name": "string"},
            "name": "testdoggie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
        resp = requests.put(url, json=data)
        assert resp.status_code == code

    def test_find_pets_status(self):
        """Verify pet search by status"""
        logger.info("Testing find pets by status with status='sold'")
        params = {"status": ["sold"]}
        url = f"{BASE_URL}/pet/findByStatus"
        resp = requests.get(url, params=params)
        assert resp.status_code == 200
        resp_json = json.loads(resp.content)
        assert resp_json[0]['status'] == "sold"

    def test_find_pets_invalid_status(self):
        """Verify invalid status gives 400"""
        logger.info("Testing find pets by invalid status expecting 400 response")
        params = {"status": [30]}
        url = f"{BASE_URL}/pet/findByStatus"
        resp = requests.get(url, params=params)
        assert resp.status_code == 400

    @pytest.mark.parametrize("pet_id, code", [
        (13, 200),
        ("", 405),
        (121212121212, 404)
    ])
    def test_find_pet(self, pet_id, code):
        """Verify finding pet by id"""
        logger.info(f"Testing find pet by ID: {pet_id}, expecting status code: {code}")
        url = f"{BASE_URL}/pet/{pet_id}"
        resp = requests.get(url)
        assert resp.status_code == code
        if pet_id == 13:
            resp_json = json.loads(resp.content)
            assert resp_json["id"] == 13

    @pytest.mark.parametrize("pet_id, pet_name, status, code", [
        (12, "sparky", "available", 200),
        (12, "test", "test", 400),
        ("test", "test", "test", 404)
    ])
    def test_update_pet_form(self, pet_id, pet_name, status, code):
        """Verify update functionality"""
        logger.info(f"Testing update of pet form data for pet ID: {pet_id} with status: {status}")
        form_data = {"name": pet_name, "status": [status]}
        url = f"{BASE_URL}/pet/{pet_id}"
        resp = requests.post(url, data=form_data)
        assert resp.status_code == code

    @pytest.mark.parametrize("pet_id, code", [
        (12, 200),
        (["abcde"], 400),
        (12112121212, 404)
    ])
    def test_delete_pet(self, pet_id, code):
        logger.info(f"Testing delete pet with ID: {pet_id}, expecting status code: {code}")
        url = f"{BASE_URL}/pet/{pet_id}"
        headers = {"api_key": "special-key"}
        resp = requests.delete(url, headers=headers)
        assert resp.status_code == code

    @pytest.mark.parametrize("pet_id, additional_metadata, expected_code", [
        (13, "Sample metadata", 200),
        (1323497234924426478264826482363428, "Metadata for non-existent pet", 404),
        (13, 68, 200)
    ])
    def test_upload_image(self, pet_id, additional_metadata, expected_code):
        """Test uploading an image to the /pet/{petId}/uploadImage endpoint"""
        logger.info(f"Testing upload image for pet ID: {pet_id} with metadata: {additional_metadata}")
        url = f"{BASE_URL}/pet/{pet_id}/uploadImage"
        
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_file:
            temp_file.write(b"This is a sample image content.")
            temp_file.seek(0)
            files = {"file": temp_file}
            data = {"additionalMetadata": additional_metadata}
            response = requests.post(url, files=files, data=data)
            assert response.status_code == expected_code
            if response.status_code == 200:
                response_data = response.json()
                assert response_data["code"] == 200
                assert isinstance(response_data["type"], str)
                assert isinstance(response_data["message"], str)

    @pytest.mark.parametrize("pet_id, pet_name, code", [
        (2342342342424, "sparks", 200),
        (343552, 36, 400),
    ])
    def test_add_pet_success(self, pet_id, pet_name, code):
        logger.info(f"Testing add pet with ID: {pet_id} and name: {pet_name}")
        url = f"{BASE_URL}/pet"
        pet_data = {
            "id": pet_id,
            "category": {"id": 0, "name": "string"},
            "name": pet_name,
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
        resp = requests.post(url, json=pet_data, headers={"Content-Type": "application/json"})
        assert resp.status_code == code

class TestStoreEntity:

    def test_get_inventory(self):
        logger.info("Testing get store inventory")
        url = f"{BASE_URL}/store/inventory"
        resp = requests.get(url)
        assert resp.status_code == 200
        response_data = resp.json()
        logger.debug(f"Inventory response: {response_data}")

    @pytest.mark.parametrize("order_data, code", [
        ({
            "id": 1,
            "petId": 123,
            "quantity": 2,
            "shipDate": datetime.now().isoformat() + "Z",
            "status": "placed",
            "complete": True
        }, 200),
        ({
            "id": "invalid_id",
            "quantity": "two",
            "shipDate": "invalid_date",
            "status": "unknown_status",
            "complete": "yes"
        }, 400),
        ({
            "id": 12311243423423423,
            "petId": 12311243423423423,
            "quantity": 2,
            "shipDate": datetime.now().isoformat() + "Z",
            "status": "placed",
            "complete": True
        }, 404),
    ])
    def test_create_order(self, order_data, code):
        logger.info(f"Testing create order with data ID: {order_data['id']} expecting status code: {code}")
        url = f"{BASE_URL}/store/order"
        response = requests.post(url, json=order_data)
        assert response.status_code == code

    @pytest.mark.parametrize("order_id, code", [
        (5, 200),
        (0, 404),
        ("abc", 400)
    ])
    def test_get_order_id(self, order_id, code):
        logger.info(f"Testing get order by ID: {order_id} expecting status code: {code}")
        url = f"{BASE_URL}/store/order/{order_id}"
        resp = requests.get(url)
        assert resp.status_code == code

    @pytest.mark.parametrize("order_id, code", [
        (5, 200),
        (0, 404),
        ("abc", 400)
    ])
    def test_delete_order(self, order_id, code):
        logger.info(f"Testing delete order with ID: {order_id} expecting status code: {code}")
        url = f"{BASE_URL}/store/order/{order_id}"
        resp = requests.get(url)
        assert resp.status_code == code

class TestUserEntity:
    
    @pytest.mark.parametrize("user_data, code", [
        ([
            {
                "id": 1,
                "username": "testuser1",
                "firstName": "Test",
                "lastName": "User",
                "email": "testuser1@example.com",
                "password": "password123",
                "phone": "1234567890",
                "userStatus": 1
            },
            {
                "id": 2,
                "username": "testuser2",
                "firstName": "Another",
                "lastName": "User",
                "email": "testuser2@example.com",
                "password": "password456",
                "phone": "0987654321",
                "userStatus": 1
            }
        ], 200),
        ([
            {
                "id": "invalid_id",
                "username": "",
                "email": "invalidemail",
                "userStatus": "active"
            }
        ], 400)
    ])
    def test_create_user_with_list(self, user_data, code):
        logger.info(f"Testing create user with list with expected status code: {code}")
        url = f"{BASE_URL}/user/createWithList"
        response = requests.post(url, json=user_data)
        assert response.status_code == code

    @pytest.mark.parametrize("username, code", [
        ("string", 200),
        ("dsfafasdasd", 404),
        (43, 400),
    ])
    def test_get_user(self, username, code):
        logger.info(f"Testing get user by username: {username} expecting status code: {code}")
        url = f"{BASE_URL}/user/{username}"
        resp = requests.get(url)
        assert resp.status_code == code

    @pytest.mark.parametrize("username, user_data, code", [
        ("testuser", {
            "id": 1,
            "username": "testuser",
            "firstName": "UpdatedFirstName",
            "lastName": "UpdatedLastName",
            "email": "updatedemail@example.com",
            "password": "newpassword123",
            "phone": "1234567890",
            "userStatus": 1
        }, 200),
        ("testuser2", {
            "id": 2424243122313123123123,
            "username": "testuser",
            "firstName": "UpdatedFirstName",
            "lastName": "UpdatedLastName",
            "email": "updatedemail@example.com",
            "password": "newpassword123",
            "phone": "1234567890",
            "userStatus": 1
        }, 404),
        ("testuser3", {
            "id": 1,
            "username": 36,
            "firstName": "UpdatedFirstName",
            "userStatus": 1
        }, 400)
    ])
    def test_update_user(self, username, user_data, code):
        logger.info(f"Testing update user with username: {username}")
        url = f"{BASE_URL}/user/{username}"
        response = requests.put(url, json=user_data)
        assert response.status_code == code

    @pytest.mark.parametrize("username, code", [
        ("string", 200),
        ("dfdfgdfbdfgdfg", 404),
        ("</script></script", 400)
    ])
    def test_delete_user(self, username, code):
        logger.info(f"Testing delete user with username: {username}")
        url = f"{BASE_URL}/user/{username}"
        response = requests.delete(url)
        assert response.status_code == code

    @pytest.mark.parametrize("username, password, code", [
        ("validuser", "validpassword", 200),
        (39, 37, 401)
    ])
    def test_user_login(self, username, password, code):
        logger.info(f"Testing user login for username: {username}")
        url = f"{BASE_URL}/user/login"
        params = {"username": username, "password": password}
        response = requests.get(url, params=params)
        assert response.status_code == code
        logger.debug(f"Headers: {response.headers}")
        if response.status_code == 200:
            expires_after = response.headers.get("X-Expires-After")
            rate_limit = response.headers.get("X-Rate-Limit")
            assert expires_after is not None, "X-Expires-After header is missing"
            assert rate_limit is not None, "X-Rate-Limit header is missing"

    def test_user_logout(self):
        logger.info("Testing user logout")
        url = f"{BASE_URL}/user/logout"
        resp = requests.get(url)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert resp_json == {'code': 200, 'type': 'unknown', 'message': 'ok'}, f"Unexpected response body: {resp_json}"

    @pytest.mark.parametrize("user_data, code", [
        ([
            {
                "id": 1,
                "username": "testuser1",
                "firstName": "Test",
                "lastName": "User",
                "email": "testuser1@example.com",
                "password": "password123",
                "phone": "1234567890",
                "userStatus": 1
            },
            {
                "id": 2,
                "username": "testuser2",
                "firstName": "Another",
                "lastName": "User",
                "email": "testuser2@example.com",
                "password": "password456",
                "phone": "0987654321",
                "userStatus": 1
            }
        ], 200),
        ([
            {
                "id": "invalid_id",
                "username": "",
                "email": "invalidemail",
                "userStatus": "active"
            }
        ], 400)
    ])
    def test_create_user_with_array(self, user_data, code):
        logger.info(f"Testing create users via /user/createWithArray expecting status code: {code}")
        url = f"{BASE_URL}/user/createWithArray"
        response = requests.post(url, json=user_data)
        assert response.status_code == code

    @pytest.mark.parametrize("user_details, code", [
        ({
            "id": 1,
            "username": "testuser1",
            "firstName": "Test",
            "lastName": "User",
            "email": "testuser1@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }, 200),
    ])
    def test_create_user_logged_in(self, user_details, code):
        logger.info("Attempting to create a user after logging in.")
        login_url = f"{BASE_URL}/user/login"
        params = {
            "username": "testuser1",
            "password": "password123"
        }
        resp = requests.get(login_url, params=params)
        assert resp.status_code == 200, f"Login failed with status code {resp.status_code}"

        url = f"{BASE_URL}/user"
        headers = {"Content-Type": "application/json"}  
        resp2 = requests.post(url, json=user_details, headers=headers)

        logger.debug(f"Response content: {resp2.json() if resp2.status_code != code else 'Success'}")
        assert resp2.status_code == code, f"Expected {code}, but got {resp2.status_code}"  
