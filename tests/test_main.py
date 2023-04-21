from main import load_operations, last_5_operations, show_last_5_operations


def test_load_json():
    expected_result = [{'date': '2019-08-26T10:50:58.294041',
                        'description': 'Перевод организации',
                        'from': 'Maestro 1596837868705199',
                        'id': 441945886,
                        'operationAmount': {'amount': '31957.58',
                                            'currency': {'code': 'RUB',
                                                         'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 64686473678894779589'},
                       {'date': '2019-07-03T18:35:29.512364',
                        'description': 'Перевод организации',
                        'from': 'MasterCard 7158300734726758',
                        'id': 41428829,
                        'operationAmount': {'amount': '8221.37',
                                            'currency': {'code': 'USD',
                                                         'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 35383033474447895560'},
                       {'date': '2018-06-30T02:08:58.425572',
                        'description': 'Перевод организации',
                        'from': 'Счет 75106830613657916952',
                        'id': 939719570,
                        'operationAmount': {'amount': '9824.07',
                                            'currency': {'code': 'USD',
                                                         'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 11776614605963066702'},
                       {'date': '2018-03-23T10:45:06.972075',
                        'description': 'Открытие вклада',
                        'id': 587085106,
                        'operationAmount': {'amount': '48223.05',
                                            'currency': {'code': 'RUB',
                                                         'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 41421565395219882431'},
                       {'date': '2019-04-04T23:20:05.206878',
                        'description': 'Перевод со счета на счет',
                        'from': 'Счет 19708645243227258542',
                        'id': 142264268,
                        'operationAmount': {'amount': '79114.93',
                                            'currency': {'code': 'USD',
                                                         'name': 'USD'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 75651667383060284188'},
                       {'date': '2019-03-23T01:09:46.296404',
                        'description': 'Перевод со счета на счет',
                        'from': 'Счет 44812258784861134719',
                        'id': 873106923,
                        'operationAmount': {'amount': '43318.34',
                                            'currency': {'code': 'RUB',
                                                         'name': 'руб.'}},
                        'state': 'EXECUTED',
                        'to': 'Счет 74489636417521191160'}]

    assert load_operations(
        file_name='tests/tests_operations.json') == expected_result


def test_last_5_operations():
    expected_result = [('07.12.2019 Перевод организации\n'
                        'Visa Classic 2842 87** **** 8901 -> Счет **3655\n'
                        '48150.39 USD')]

    assert last_5_operations()[0] == expected_result[0]


def test_show_last_5_operations():
    assert show_last_5_operations() is None
