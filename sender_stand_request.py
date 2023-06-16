import configuration
import data
import requests
import create_kit_tests
import string
import random

def get_random_string(length):
    letter_set = string.ascii_letters
    rand_string = ''.join(random.choice(letter_set) for i in range(length))
    return rand_string

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def get_user_token(user_body):
    user_response = post_new_user(user_body)
    print("authToken = " + user_response.json()["authToken"])
    return user_response.json()["authToken"]


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH, json=user_body)

def get_docs():
    return requests.get(configuration.URL_SERVICE+configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE+configuration.LOG_PATH,params={"count":20}).headers

def get_user_model_data():
    return requests.get(configuration.URL_SERVICE + configuration.USER_MODEL_PATH)

def post_products_kits():
    return requests.post(configuration.URL_SERVICE+configuration.PRODUCTS_KITS_PATH,json=data.product_ids,headers=create_kit_tests.headers)

def post_new_kit(kit_body):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,json=kit_body,headers=create_kit_tests.headers)

