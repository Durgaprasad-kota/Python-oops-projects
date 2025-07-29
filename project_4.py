from abc import ABC,abstractmethod

class UniversityMember(ABC):
    def __init__(self,name,id,role):
        self._name=name
        self.__id=id
        self.__role=role
    def view_profile(self):
        return f"______PROFILE______\nROLE :{self.__role}\nNAME :{self._name}\nID :{self.__id}"
    @abstractmethod
    def access_system(self):
        pass
class Student(UniversityMember):
    def __init__(self, name, id):
        super().__init__(name, id,'student')
    def access_system(self):
        return f"{self._name} ,you access books and materials 🧑🏻‍🎓"
class Professor(UniversityMember):
    def __init__(self, name, id):
        super().__init__(name, id, 'Professor')
    def access_system(self):
        return f"{self._name} ,you can acces some pens and chalk pieces 🖊️"
def user_entry(user:UniversityMember):
    return  f"{user.view_profile()}\n{user.access_system()}"

if __name__=='__main__' :
    s1=Student("anil","4289")
    p1=Professor("rolex","8989")
    
    print(user_entry(s1))
    print(user_entry(p1))