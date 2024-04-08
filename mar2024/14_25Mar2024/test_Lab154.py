#API request  - HTTP request

import pytest
import requests
import allure

@allure.title("Create Booking CRUD")
@allure.description("TC#1 - verify the create Booking")
@pytest.mark.curd
def test_create_booking_positive():
    # Request
    # UrL
    # Method
    # Headers
    # Payload / Data / Body
    # Auth(No
    # Auth in post)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url+base_path
    headers = {"content-Type" : "application/json"}
    payload = {
    "firstname" : "Hari",
    "lastname" : "Gulla",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-04-06",
        "checkout" : "2024-04-07"
    },
    "additionalneeds" : "Breakfast"
}
    response = requests.post(url=URL, headers=headers, json=payload)

    #Response body verfication
    #Headers
    #Status code
    #Json schema validation
    #Time Response

    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    firstname = response_json["booking"]["firstname"]
    assert firstname == "Hari"
    checkin = response_json["booking"]["bookingdates"]["checkin"]
    assert checkin == "2024-04-06"

@allure.title("Create Booking CRUD")
@allure.description("TC#1 - verify Booking is not created with {} data")
@pytest.mark.curd
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    #Assertions
    assert response.status_code == 500