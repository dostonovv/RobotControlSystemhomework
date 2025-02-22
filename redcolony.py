# |||||||||||||||||||||
# other planet for live





from abc import ABC, abstractmethod
import uuid




class Humans(ABC):
    """Human ota bosh klassi !!!  no 212"""
    def __init__(self , name , ids1 , year , level):
        self.name = name
        self.year = year
        self.__ids1 = uuid.uuid4()
        self.__level = level
    def info(self , code):
        """foydalanuvchiga barcha ko'rishi bilishi mumkin bo'lgan ma'lumotlarni ko'rsatadi"""
        if isinstance(code , str):
            if code == "colonycode01":
                return (f"Name : {self.name}\n"
                        f"Year : {self.year}\n"
                        f"id : {self.__ids1}\n"
                        f"level : {self.__level}\n")
            return (f"Name : {self.name}\n"
                        f"Year : {self.year}\n")
        return "shunchaki birorta matn yozing bo'ldi dasturdagi ma'lumotlarni ko'rasiz !!!"
    def set_level(self , level):
        self.__level = level
        return "Level o'zgartirildi"
class Astrnout(Humans):
    """Astranavt bu uchuvchi degan ma'noni anglatadi ! ! !"""
    def __init__(self , name , ids1 , year , level , rocket):
        super().__init__(name , ids1 , year , level)
        self.__rocket = rocket
        self.set_level(2)
    def get_rocket_num(self , code):
        if isinstance(code , str):
            if code == "colonycode02":
                return (f"astranout rocket : {self.__rocket} ")
            return "KOD XATO ! ! !"
        return "ERROR CODE TYPE"
    def set_rocket_num(self , code , new_num):
        if isinstance(code , str):
            if code == "colonycode02":
                self.__rocket = new_num
                return (f"astranout rocket : {self.__rocket} ")
            return "KOD XATO ! ! !"
        return "ERROR CODE TYPE"
class Scientist(Humans):
    def __init__(self , name , ids1 , year , level , type):
        super().__init__(name , ids1 , year , level)
        self.__type = type
        self.set_level(3)
    def get_type(self , code):
        if isinstance(code , str):
            if code == "colonycode02":
                return (f"Scientist type : {self.__type} ")
            return "KOD XATO ! ! !"
        return "ERROR CODE TYPE"
    def set_type(self , code , new_type):
        if isinstance(code , str):
            if code == "colonycode02":
                self.__type = new_type
                return (f"Scientist type : {self.__type} ")
            return "KOD XATO ! ! !"
        return "ERROR CODE TYPE"
class Colony:
    def __init__(self , colonyname , cordinates , population , water, workers = 0 , rocket = 0):
        self.colonyname = colonyname
        self.__cordinates = cordinates
        self.__population = population
        self.__water = water
        self.__workers = workers
        self.__rocket = rocket
    def colony_info(self , code):
        """colonyqa haiqda malumot"""
        if isinstance(code, str):
            if code == "colonycode03":
                return (f"colony name : {self.colonyname}\n"
                        f"colony cordinates : {self.__cordinates}\n"
                        f"population : {self.__population}\n"
                        f"water : {self.__water}\n"
                        f"workers : {self.__workers}\n"
                        f"Worked rockets : {self.__rocket}")

            return (f"colony name : {self.colonyname}\n"
                        f"population : {self.__population}\n")
        return "shunchaki birorta matn yozing bo'ldi dasturdagi ma'lumotlarni ko'rasiz !!!"
    def set_rocketsnum(self , code , num):
        if isinstance(code , str):
            if code == "colonycode04":
                if isinstance(num , int):
                    self.__rocket = num
                    return "O'zgartirish kiritildi"
                return "Type error"
            return "ERROR"
        return "Type error"
    def get_rocketsnum(self , code):
        if isinstance(code , str):
            if code == "colonycode04":
                return f"worket rockets : {self.__rocket}"
            return "Error"
        return "Type error"
    def set_water(self , code , kub):
        if isinstance(code , str):
            if code == "colonycode05":
                if isinstance(kub , int):
                    self.__water = kub
                    return "O'zgartirish kiritildi"
                return "Type error"
            return "ERROR"
        return "Type error"
    def get_water(self , code):
        if isinstance(code , str):
            if code == "colonycode05":
                return f"water : {self.__water}"
            return "Error"
        return "Type error"
    def set_population(self , code , num):
        if isinstance(code , str):
            if code == "colonycode06":
                if isinstance(num , int):
                    self.__population = num
                    return "O'zgartirish kiritildi"
                return "Type error"
            return "ERROR"
        return "Type error"
    def get_populationnum(self , code):
        if isinstance(code , str):
            if code == "colonycode06":
                return f"water : {self.__population}"
            return "Error"
        return "Type error"
    def set_cordinates(self , code , num):
        if isinstance(code , str):
            if code == "colonycode07":
                if isinstance(num , int):
                    self.__cordinates = num
                    return "O'zgartirish kiritildi"
                return "Type error"
            return "ERROR"
        return "Type error"
    def get_cordinates(self , code):
        if isinstance(code , str):
            if code == "colonycode07":
                return f"water : {self.__cordinates}"
            return "Error"
        return "Type error"
class Rockets:
    def __init__(self , rocketname , type , cordinates , work = True):
        self.rocketname = rocketname
        self.__type = type
        self.__cordinates1 = cordinates
        self.__work = work
    def Rockets_info(self , code):
        """colonyqa haiqda malumot"""
        if isinstance(code, str):
            if code == "colonycode03":
                return (f"rocket name : {self.rocketname}\n"
                        f"cordinates : {self.__cordinates1}\n"
                        f"state : {self.__work}\n"
                        f"Type : {self.__type}")

            return (f"colony name : {self.rocketname}")
        return "shunchaki birorta matn yozing bo'ldi dasturdagi ma'lumotlarni ko'rasiz !!!"
    def set_rockettype(self , code , type):
        if isinstance(code , str):
            if code == "colonycode08":
                if isinstance(type , str):
                    self.__type = type
                    return "O'zgartirish kiritildi"
                return "Type error"
            return "ERROR"
        return "Type error"
    def get_rockettype(self , code):
        if isinstance(code , str):
            if code == "colonycode08":
                return f"rocket type : {self.__type}"
            return "Error"
        return "Type error"
    def set_rocketcordinates(self , code , cordinates):
        if isinstance(code , str):
            if code == "colonycode09":
                if isinstance(type , str):
                    self.__cordinates1 = cordinates
                    return "O'zgartirish kiritildi"
                return "Type error"
            return "ERROR"
        return "Type error"
    def get_rocketcordinates(self , code):
        if isinstance(code , str):
            if code == "colonycode09":
                return f"rocket type : {self.__cordinates1}"
            return "Error"
        return "Type error"
    def rocketstate(self , code , state):
        if isinstance(code , str):
            if code == "colonycode10":
                if isinstance(state , str):
                    if state == "10":
                        self.__work = True
                        return "O'zgartirildi"
                    elif state == "01":
                        self.__work = False
                        return "O'zgartirildi"
                    return "Xato"
                return "Type error"
            return "Code error"
        return "Type error"
    def get_rocketstate(self , code):
        if isinstance(code , str):
            if code == "colonycode10":
                return f"Holat : {self.__work}"
            return "Code Error"
        return "Type error"



astronaut1 = Astrnout("John Carter", None, 2035, 2, "Apollo-X")
astronaut2 = Astrnout("Sarah Bright", None, 2036, 2, "Orion-7")

scientist1 = Scientist("Dr. Alan Grant", None, 2030, 3, "Biologist")
scientist2 = Scientist("Dr. Emily Rose", None, 2032, 3, "Engineer")


mars_colony = Colony("Mars Alpha", "23.4N, 45.6E", 50, 1000, workers=10, rocket=5)


rocket1 = Rockets("Falcon 9", "Cargo", "23.4N, 45.6E")
rocket2 = Rockets("Starship", "Passenger", "23.5N, 45.7E")

print(astronaut1.info("colonycode01"))
print(scientist1.info("colonycode01"))
print(mars_colony.colony_info("colonycode03"))
print(rocket1.Rockets_info("colonycode03"))









# print(12)