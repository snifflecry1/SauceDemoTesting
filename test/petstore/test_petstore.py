import requests
import json
import pytest

BASE_URL ="https://petstore.swagger.io/v2"
class TestPetEntity:

    @pytest.mark.parametrize("pet_id, code", [
        (13, 200),
        ("test", 400),
        (98, 404),
        (13, 405)
    ])
    def test_update_existing_pet(self, pet_id, code):
        """Verify update existing pet functionality"""
    
        url = f"{BASE_URL}/pet"
        data =  {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "testdoggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        resp = requests.put(url, data=data)
        assert resp.status_code==code




    def test_find_pets_status(self):
        """Verify pet search by status"""

        params = {"status":["sold"]}
        url = f"{BASE_URL}/pet/findByStatus"
        resp = requests.get(url, params=params)
        assert resp.status_code==200
        resp_json = json.loads(resp.content)
        assert resp_json[0]['status'] == "sold"
    
    def test_find_pets_invalid_status(self):
        """Verify invalid status gives 400"""

        params = {"status":[""]}
        url = f"{BASE_URL}/pet/findByStatus"
        resp = requests.get(url, params=params)
        assert resp.status_code==400

    @pytest.mark.parametrize("pet_id, code", [
        (13, 200),
        ("test", 404),
        ("", 405)
    ])
    def test_find_pet(self, pet_id, code):
        """Verify finding pet by id"""

        url = f"{BASE_URL}/pet/{pet_id}"
        resp = requests.get(url)
        assert resp.status_code == code
        if pet_id == 13:
            resp_json = json.loads(resp.content)
            assert resp_json["id"] == 13

    @pytest.mark.parametrize("pet_id, pet_name, status, code", [
        (12, "sparky", "available", 200),
        (12, {"testdict":"test"}, "test", 400),
        (1345343453, "test", "test", 404)
    ])
    def test_update_pet_form(self, pet_id, pet_name, status, code):
        """Verify update functionality"""

        form_data = {"name": pet_name, "status":[status]}
        url = f"{BASE_URL}/pet/{pet_id}"
        resp = requests.post(url, data=form_data)
        assert resp.status_code==code
    
    @pytest.mark.parametrize("pet_id, code", [
        (12, 200),
        ("abcde", 400),
        (98, 404)
    ])
    def test_delete_pet(self, pet_id, code):
        url = f"{BASE_URL}/pet/{pet_id}"

        headers = {"api_key":"special-key"}
        resp = requests.delete(url)
        assert resp.status_code==code


    #def test_upload_image_success(self):
    # def test_add_pet_success(self):
    #     url = f"{BASE_URL}/pet"
    #     # Pet data structured as required
    #     pet_data = {
    #         "id": 0,
    #         "category": {
    #             "id": 0,
    #             "name": "string"
    #         },
    #         "name": "doggie",
    #         "photoUrls": [
    #             "string"
    #         ],
    #         "tags": [
    #             {
    #                 "id": 0,
    #                 "name": "string"
    #             }
    #         ],
    #         "status": "available"
    #     }

    #     # Make the POST request to add the pet
    #     response = requests.post(url, data=json.dumps(pet_data), headers={"Content-Type": "application/json"})

    #     print(response)