slovarb = {1: 'Сусемь', 2: 'Старфайтер', 3: 'Спитфайр Пивовоз', 4: 'Танк('}
key = int(input('Введи число от 1 до 4 и узнай какой самолет ты сегодня: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(slovarb)