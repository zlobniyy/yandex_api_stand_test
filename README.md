# Тесты на проверку параметра firstName при создании пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- Тесты для создания пользователя запускаются командой pytest create_user_tests

# Тесты на проверку параметра name при создании набора под пользователем в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest
- Тесты для создания набора под пользователем запускаются командой pytest create_kit_tests

# Описание интерфейсных рфункций:
 - sender_stand_request.get_random_string(length) - возвращает случайную строки(ascii) заданной длины length
 - sender_stand_request.get_user_body(name_string) - возвращает тело(json) запроса для создания нового пользователя c firstName = name_string
 - sender_stand_request.get_user_token(body) - возвращает authToken из ответа создания нового пользователя(body - тело запроса на создания нового пользователя)
 - sender_stand_request.post_new_user(user_body) - создание(POST) нового пользователя с телом user_body
 - sender_stand_request.post_new_kit(kit_body) - создание(POST) нового набора с телом kit_body
 - create_kit_tests.get_kit_body(name) - возвращает тело для запроса создания набора с именем name под пользователем
 - create_kit_tests.positive_create_kit_assert() - проверка успешного(200) ответа запроса на создание набора под пользователем
 - negative_create_kit_assert(name=None) - проверка отрицательного(400) ответа запроса создания набора под пользователем
# Описание тестовых функций для проверки создания набора под пользователем:
- create_kit_tests.test_one_symbol_kit_name - Допустимое количество символов (1)
- create_kit_tests.test_511_symbols_kit_name - Допустимое количество символов (511)
- create_kit_tests.test_zero_symbols_kit_name - Количество символов меньше допустимого (0)
- create_kit_tests.test_512_symbols_kit_name - Количество символов больше допустимого (512)
- create_kit_tests.test_eng_symbols_kit_name - Разрешены английские буквы
- create_kit_tests.test_rus_symbols_kit_name - Разрешены русские буквы
- create_kit_tests.test_spec_symbols_kit_name - Разрешены спецсимволы
- create_kit_tests.test_space_symbol_kit_name - Разрешены пробелы
- create_kit_tests.test_numbers_kit_name - Разрешены цифры
- create_kit_tests.test_not_deliver_kit_name_field - Параметр не передан в запросе
- create_kit_tests.test_number_data_type_kit_data - Передан другой тип параметра (число)