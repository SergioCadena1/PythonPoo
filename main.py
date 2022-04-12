from car import Car
from account import Account

if __name__ == "__main__":
    print("hola gono")
    car = Car ("LKJ021", Account("Sergio","12233"))
    car2 = Car("SKA542",Account("Laura","564653"))
    print(vars(car.driver))   
    print(vars(car2.driver))