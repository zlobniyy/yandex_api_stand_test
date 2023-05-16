import sender_stand_request
import data


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Ааааааааааааааа")

def test_create_user_eng_letters_in_first_name_get_success_response():
    positive_assert("QWErty")

def test_create_user_rus_letters_in_first_name_get_success_response():
    positive_assert("Мария")

#Negative tests

def test_create_user_1_letter_in_first_name_get_negatove_response():
    negative_assert("A")

def test_create_user_16_letter_in_first_name_get_negatove_response():
    negative_assert("Аааааааааааааааa")

def test_create_user_number_in_first_name_get_negatove_response():
    negative_assert("123")

def test_create_user_no_space_symbol_in_first_name_get_negatove_response():
    negative_assert("Человек и Ко")

def test_create_user_no_spec_symbols_in_first_name_get_negatove_response():
    negative_assert("№%@")

def test_create_user_not_defined_first_name_get_negatove_response():
    negative_assert(None,"Не все необходимые параметры были переданы")

def test_create_user_not_populated_first_name_get_negatove_response():
    negative_assert("","Не все необходимые параметры были переданы")

def test_create_user_wrong_data_type_in_first_name_get_negatove_response():
    negative_assert(12)

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    users_table_response = sender_stand_request.get_user_model_data()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    assert users_table_response.text.count(str_user) == 1

def negative_assert(first_name,message="Имя пользователя введено некорректно. Имя может содержать только русские или латинские буквы, длина должна быть не менее 2 и не более 15 символов"):
    user_body = get_user_body(first_name)
    if first_name is None:
        user_body.pop("firstName")
        print(user_body)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400, "error in status code"
    assert user_response.reason == "Bad Request"
    assert user_response.json()["message"] == message, "error in text"