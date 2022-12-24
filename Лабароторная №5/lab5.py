class Rocket():
    def __init__(self, total_weight, amount_of_fuel, engine_status):        #Инициализатор
        self.total_weight = total_weight
        self.amount_of_fuel = amount_of_fuel
        self.engine_status = engine_status
    def spend_fuel(self, count):               # Метод расходует введённое кол-во топлива, вычисляет оставшееся топливо и общую массу
        self.amount_of_fuel -= count           # Принимает любое число
        self.total_weight -= count             # Выводит True, если топливо осталось, или False, если топливо закончилось
        if self.amount_of_fuel <= 0:
            self.amount_of_fuel = 0
            self.engine_status = False
            return False
        elif self.amount_of_fuel > 0:
            self.engine_status = True
            return True
    def get_fuel_level(self):                                       # Метод позволяет узнать текущее кол-во топлива
        return f'Кол-во топлива: {self.amount_of_fuel}'
    def get_total_weight(self):                                     # Метод позволяет узнать текущую общую массу
        return f'Общая масса: {self.total_weight}'
    def get_is_engine_running(self):                                # Метод позволяет узнать состояние двигателя (True - включен, False - выключен)
        return f'Состояние двигателя: {self.engine_status}'

def main():
    SpaceX = Rocket(15000, 5000, True)
    while SpaceX.amount_of_fuel > 0:
        SpaceX.spend_fuel(1000)
        print(SpaceX.get_fuel_level(), end='; ')
        print(SpaceX.get_total_weight(), end='; ')
        print(SpaceX.get_is_engine_running())
main()