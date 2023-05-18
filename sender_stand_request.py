import configuration
import data
import requests

def get_docs():
    return requests.get(configuration.URL_SERVICE+configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE+configuration.LOG_PATH,params={"count":20}).headers

def get_user_model_data():
    return requests.get(configuration.URL_SERVICE + configuration.USER_MODEL_PATH)

def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE+configuration.CREATE_USER_PATH, json=user_body, headers=data.headers)

def post_products_kits():
    return requests.post(configuration.URL_SERVICE+configuration.PRODUCTS_KITS_PATH,json=data.product_ids,headers=data.headers)

def post_new_kit(kit_body):
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH,json=kit_body,headers=data.headers)
# response = post_products_kits()
#
# print(response.status_code)
# print(response.json())