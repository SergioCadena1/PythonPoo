from car import Car

if __name__ == "__main__":
    print("hola gono")
    car = Car()
    car.licence = "ALS512"
    car.driver = "Nicolle"
    print(vars(car))

    car2 = Car()
    car2.licence="OKS021"
    car2.driver= "Alexander"
    car2.passengers= 3
    print(vars(car2))
