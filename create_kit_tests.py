import sender_stand_request
import data
import string
import random

def get_random_string(length):
    letter_set = string.ascii_letters
    rand_string = ''.join(random.choice(letter_set) for i in range(length))
    print(rand_string)
    return rand_string

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    print(current_body)
    return current_body

def get_user_token(user_body):
    user_response = sender_stand_request.post_new_user(user_body)
    # str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
    #            + user_body["address"] + ",,," + user_response.json()["authToken"]
    print(user_response.json()["authToken"])
    return user_response.json()["authToken"]

name_string = get_random_string(10)
body = get_user_body(name_string)
authToken = get_user_token(body)
headers = data.headers.copy()
headers["Authorization"] = "Bearer " + authToken



#1
def test_one_symbol_kit_name():
    positive_create_kit_assert("a")
#2
def test_511_symbols_kit_name():
    positive_create_kit_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
                               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
                               "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                               "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
                               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#3
def test_zero_symbols_kit_name():
    negative_create_kit_assert("")

#4
def test_512_symbols_kit_name():
    negative_create_kit_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
                               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"\
                               "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"\
                               "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"\
                               "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"\
                               "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#5
def test_eng_symbols_kit_name():
    positive_create_kit_assert("QWErty")

#6
def test_rus_symbols_kit_name():
    positive_create_kit_assert("Мария")

#7
def test_spec_symbols_kit_name():
    positive_create_kit_assert("\"№%@\",")

#8
def test_space_symbol_kit_name():
    positive_create_kit_assert("Человек и КО ")

#9
def test_numbers_kit_name():
    positive_create_kit_assert("123")

#10
def test_not_deliver_kit_name_field():
    negative_create_kit_assert(None)

#11
def test_number_data_type_kit_data():
    negative_create_kit_assert(123)

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def positive_create_kit_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_kit(kit_body)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_create_kit_assert(name=None):
    kit_body = get_kit_body(name)
    if name is None:
        kit_body.pop("name")
    kit_response = sender_stand_request.post_new_kit(kit_body)

    assert kit_response.status_code == 400
