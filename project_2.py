from abc import ABC,abstractmethod
class Doctor:
    def __init__(self, name, spec):
        self._name=name
        self._spec=spec
    def get_doctor_details(self):
        return f"{self._name}({self._spec})"
class Patient(ABC):
    def __init__(self,name,age,id,doctor:Doctor):
        self.__name=name
        self.__id=id
        self._age=age
        self._doctor=doctor
    @abstractmethod
    def calculate_bill(self):
        pass
    @abstractmethod
    def checkup(self):
        pass
    def get_details(self):
        return f"""
       🛌🏻 Name  :{self.__name}
       🆔 Id    :{self.__id}
       🎂 Age   :{self._age}
       🧑🏻‍⚕️ Doctor:{self._doctor.get_doctor_details()}"""
class Inpatient(Patient):
    def __init__(self, name, age, id,doctor, days):
       super().__init__(name, age, id,doctor)
       self._days=days
    def calculate_bill(self):
        return f"Total Bill :${5000+(self._days)*1000} "
    def checkup(self):
        return f"🏥 Regular checkup under admission"
class Outpatient(Patient):
    def __init__(self, name, age, id,doctor, days):
       super().__init__(name, age, id,doctor)
       self._days=days
    def calculate_bill(self):
        return f"Total Bill :${ 600*self._days} "
    def checkup(self):
        return f"🏩 Outpatient quick checkup done "
class EmergencyPatient(Patient):
    def __init__(self, name, age, id,doctor):
       super().__init__(name, age, id,doctor)
    def calculate_bill(self):
        return f"Total Bill :$12000 "
    def checkup(self):
        return f"☎️ Emergency cases observe first "
def show_details(p:Patient):
    print(p.get_details())
    print(p.calculate_bill())
    print(p.checkup())
    print("-"*90)
d=Doctor("murali","cardiology")
d2=Doctor("Vraun","neuralogy")
d3=Doctor("vijay",'RMP')

p1=Inpatient('anil',18,4289,d,days=3)
p2=Outpatient('raghu',19,4218,d2,days=4)
p3=EmergencyPatient('vinay',20,4275,d3)


show_details(p1)
show_details(p2)
show_details(p3)
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   ***