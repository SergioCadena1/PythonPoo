class Car:
    id = int
    licence = str
    driver = str
    passengers = int

    def __init__(self, license, driver):
        self.licence=license
        self.driver=driver
        