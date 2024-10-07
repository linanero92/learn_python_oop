class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price.keys():
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            price = self.__item_price.get(item)
            total.append(price)
        if len(total) > 10:
            total_price = sum(total) * 0.9
        else:
            total_price = sum(total)
        return total_price

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price.get(item))
        tax_20 = sum(total) * 0.2
        if len(total) > 10:
            tax_20 *= 0.9
        return tax_20

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price.get(item))
        tax_10 = sum(total) * 0.1
        if len(total) > 10:
            tax_10 *= 0.9
        return tax_10

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'


online_cash_register = OnlineSalesRegisterCollector()

try:
    print(online_cash_register.add_item_to_cheque(name=''))
    print(online_cash_register.add_item_to_cheque(name='qwertyuioplkjhgfdsazxc67vbnmlkjhgwertyiuhf1'))

except ValueError as ecs:
    print(ecs)

try:
    print(online_cash_register.add_item_to_cheque(name='хлеб'))
except NameError as e:
    print(e)

print("------------")
online_cash_register.add_item_to_cheque(name='кола')
online_cash_register.add_item_to_cheque(name='чипсы')
print(f"Товары в чеке: {online_cash_register.name_items}")
print(f"Кол-во товаров: {online_cash_register.number_items}")
print(f"Cумма: {online_cash_register.check_amount()}")

print("------------")
online_cash_register.delete_item_from_check(name='чипсы')
print(f"Товары в чеке: {online_cash_register.name_items}")
print(f"Кол-во товаров: {online_cash_register.number_items}")
print(f"Cумма: {online_cash_register.check_amount()}")

print("------------")
online_cash_register.add_item_to_cheque(name='молоко')
online_cash_register.add_item_to_cheque(name='кефир')
online_cash_register.add_item_to_cheque(name='кола')
print(f"Товары в чеке: {online_cash_register.name_items}")
print(f"Общий НДС 20%: {online_cash_register.twenty_percent_tax_calculation()}")

print("------------")
online_cash_register.add_item_to_cheque(name='кефир')
online_cash_register.add_item_to_cheque(name='чипсы')
online_cash_register.add_item_to_cheque(name='молоко')
print(f"Товары в чеке: {online_cash_register.name_items}")
print(f"Общий НДС 10%: {online_cash_register.ten_percent_tax_calculation()}")
print(f"Общий НДС: {online_cash_register.total_tax()}")

print("------------")
print("Проверка валидации номера телефона:")
try:
    print(online_cash_register.delete_item_from_check(name='сыр'))
except NameError as e:
    print(e)

try:
    print(online_cash_register.get_telephone_number('test'))
    print(online_cash_register.get_telephone_number('9345673344'))
except ValueError as esc:
    print(esc)

try:
    print(online_cash_register.get_telephone_number(9345673344))
    print(online_cash_register.get_telephone_number(90123456789))
except ValueError as e:
    print(e)
