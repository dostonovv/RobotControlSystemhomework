class Robot:
    """!@!@!"""
    def __init__(self , name , battery , speed , sensor_data):
        """@!@!@!@"""
        self.name = name
        self.__battery = battery
        self.__speed = speed
        self.__sensor_data = sensor_data
    def get_batteryprosent(self , kod):
        if kod == "112":
            return f"{self.name} ning batareya foizi : {self.__battery}"
        else:
            return "Error !"
    def get_speedkm(self , kod):
        if kod == "111":
            return f"{self.name} ning tezlgi (maksimal) : {self.__speed}"
        else:
            return "Error !"
    def get_datasensors(self , kod):
        if kod == "101":
            return f"{self.__sensor_data}"
        else:
            return "Error !"
    def set_batteryprosent(self , prosent):
        self.__battery = prosent
        return f"{self.__battery}"

    def set_speed(self, km):
        self.__speed = km
        return f"{self.__speed}"

    def set_datasensor(self, do):
        self.__sensor_data = do
        return f"{self.__sensor_data}"
    def all_info(self , kod):
        if kod == "dvv12":
            return (f"Robot : {self.name}"
                    f"Batareya : {self.__battery}"
                    f"Tezlik : {self.__speed}"
                    f"Harakati : {self.__sensor_data}")
    def move(self):
        return "Hullas men robotman"

class SecurityRobot(Robot):
    def __init__(self, name, battery, speed, sensor_data, obj : list):
        super().__init__(name, battery, speed, sensor_data)
        self.obj =obj

    def scan(self, area_start, area_stop):
        for i in range(area_start, area_stop):
            if i in self.obj:
                return "Hudud havfli"
        return "Hudud havfsiz bu yerda hammasi toza"

    def move(self):
        return f"{self.name} Men qo'riqlovchi robotman !"


class WarRobot(SecurityRobot):
    def __init__(self , name , battery , speed , sensor_data , obj , mykordinates):
        super().__init__(name , battery , speed , sensor_data , obj)
        self.__mykordinates = mykordinates
        """@!@!@!@"""
    def war(self, area_start, area_stop):
        for i in range(area_start, area_stop):
            if i in self.obj:
                self.__mykordinates = i
                return "Men shu hududlarda urushda bo'laman , chunki u yerda noma'lum object mavjud"
        return "No War"
    def get_kordinates(self , kod):
        if kod == "1112":
            return f"{self.__mykordinates} kordinatalar"
        else:
            return "ERORR 1111"
    def move(self):
        return f"{self.name} Men urushda qatnashuvchi robotman !"

a = WarRobot("B21", 1200, 100, "Active", [5, 10, 15], (50.5, 60.6))


b = SecurityRobot("B21" , 1200 , 100 , "Not Avtive" , [20 , 30 , 40])

print(b.all_info("dvv12"))
print(b.move())








