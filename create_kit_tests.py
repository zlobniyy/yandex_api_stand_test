import create_user_tests
import sender_stand_request
import data
import configuration

# user_data_response = sender_stand_request.post_new_user(data.user_body)
# print(type(user_data_response))
# auth_token = user_data_response.json()["authToken"]
# print(user_data_response.text)
# print(auth_token)

# response = sender_stand_request.post_new_kit()
# print(response.content)
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
    # print(kit_response.json()["name"])

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_body["name"]

def negative_create_kit_assert(name=None):
    kit_body = get_kit_body(name)
    if name is None:
        kit_body.pop("name")
    kit_response = sender_stand_request.post_new_kit(kit_body)
    # print(kit_response.content)

    assert kit_response.status_code == 400