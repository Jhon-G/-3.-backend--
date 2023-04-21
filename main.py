import json
from datetime import datetime


def load_operations(file_name='operations.json') -> list[dict]:
    """
    Функция читает JSON файл и возвращает список словарей с информацией о студентах

    :param file_name: Имя файла.
    :return: List[dict].

    """
    with open(file_name, 'r', encoding='utf-8') as f:
        operations_list = json.load(f)

    return operations_list


def last_5_operations() -> list:
    operations_list = load_operations()
    executed_operations = []

    for operation in operations_list:
        if operation != {} and operation['state'] == 'EXECUTED':

            operation_date = datetime.strptime(operation['date'],
                                               '%Y-%m-%dT%H:%M:%S.%f').date().strftime(
                '%d.%m.%Y')
            operation_description = operation['description']
            card_name = operation.get('from')
            card_or_bill = operation.get('to').split()
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']

            if card_name is not None:
                if card_name.count(' ') == 1:
                    card_name = card_name.split()
                    hide_card_number = f'{card_name[1][0:4]} {card_name[1][4:6]}** **** {card_name[1][-5:-1]}'
                    card_name = f'{card_name[0]}'

                elif card_name.count(' ') == 2:
                    card_name = card_name.split()
                    hide_card_number = f'{card_name[2][0:4]} {card_name[2][4:6]}** **** {card_name[2][-5:-1]}'
                    card_name = f'{card_name[0]} {card_name[1]}'

                operation_info = f'{operation_date} {operation_description}\n' \
                                 f'{card_name} {hide_card_number} -> {card_or_bill[0]} **{card_or_bill[1][-4:]}\n' \
                                 f'{amount} {currency}'
                executed_operations.append(operation_info)

        last_5_operation_sorted_by_date = sorted(executed_operations,
                                                 reverse=True, key=lambda
                x: datetime.strptime(x.split(' ', 1)[0], '%d.%m.%Y'))[:5]

    return last_5_operation_sorted_by_date


def show_last_5_operations():
    for operations in last_5_operations():
        print(operations)
        print()


if __name__ == '__main__':
    show_last_5_operations()
