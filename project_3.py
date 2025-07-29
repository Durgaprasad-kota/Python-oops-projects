from abc import ABC,abstractmethod
class Student(ABC):
    def __init__(self,name,id,rank,cource):
          self.__name=name
          self.__id=id
          self._rank=rank
          self._cource=cource.lower()
    @abstractmethod
    def enroll_in_cource(self):
        pass
    @abstractmethod
    def calculate_fee(self):
        pass
    def get_details(self):
        return f"""🧑🏻‍🎓|_______Student Profile________|
    Student :{self.__name}
    Id :{self.__id}
    Rank:{self._rank}"""
class UndergraduateStudent(Student):
    def __init__(self, name,  id,rank,cource):
        super().__init__(name, id,rank,cource)
        self.c=0
    def enroll_in_cource(self):
        if self._cource =="aiml" or self._cource== "aids" or self._cource == "iot" or self._cource =="cyber":
            if  30000 > self._rank :
                self.c=1
                return f"📘 Undergradute  students Enrolled in :{self._cource}"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
        elif  self._cource =="ece" or self._cource=="eee":
            if  50000 > self._rank :
                self.c=2
                return f"📗 Undergradute  students Enrolled in :{self._cource}"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
        elif self._cource =='mec' or self._cource =='civil':
            if 75000>self._rank:
                self.c=3
                return f"📙 Undergradute  students Enrolled in :{self._cource}"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
    
    def calculate_fee(self):
        if self.c==1:
            return f"💰 Total Fee is 70,000 rupees"
        elif self.c==2:
            return f"💰 Total Fee is 50,000 rupees"
        elif self.c==3:
            return f"💰 Total Fee is 25,000 rupees"
        else :
            return f"Sorry we can't accomodate for fee,because you cann't get a seat in our college "
class PostgraduateStudent(Student):
    def __init__(self, name,  id,rank,cource):
        super().__init__(name, id,rank,cource)
        self.c=0
    def enroll_in_cource(self):
        if self._cource =="aiml" or self._cource== "aids" or self._cource == "iot" or self._cource =="cyber":
            if  30000 > self._rank :
                self.c=1
                return f"📘 Postgraduate  students Enrolled in :{self._cource}"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
        elif  self._cource =="ece" or self._cource=="eee":
            if  50000 > self._rank :
                self.c=2
                return f"📗 Postgraduate  students Enrolled in :{self._cource}"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
        elif self._cource =='mec' or self._cource =='civil':
            if 75000>self._rank:
                self.c=3
                return f"📙 Postgraduate  students Enrolled in :{self._cource}"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
    
    def calculate_fee(self):
        if self.c==1:
            return f"💰 Total Fee is 70,000 rupees"
        elif self.c==2:
            return f"💰 Total Fee is 50,000 rupees"
        elif self.c==3:
            return f"💰 Total Fee is 25,000 rupees"
        else :
            return f"Sorry we can't accomodate for fee,because you cann't get a seat in our college "
        
class Diploma(Student):
    def __init__(self, name,  id,rank,cource):
        super().__init__(name, id,rank,cource)
        self.c=0
    def enroll_in_cource(self):
        if self._cource =="aiml" or self._cource== "aids" or self._cource == "iot" or self._cource =="cyber":
            if  30000 > self._rank :
                self.c=1
                return f"📘 Diploma  students Enrolled in :{self._cource} Engineering"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
        elif  self._cource =="ece" or self._cource=="eee":
            if  50000 > self._rank :
                self.c=2
                return f"📗 Diploma  students Enrolled in :{self._cource} Engineering"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
        elif self._cource =='mec' or self._cource =='civil':
            if 75000>self._rank:
                self.c=3
                return f"📙 Diploma  students Enrolled in :{self._cource} Engineering"
            else:
                return f"Sorry {self._cource} cource dosen't come for your rank"
    
    def calculate_fee(self):
        if self.c==1:
            return f"💰 Total Fee is 70,000 rupees"
        elif self.c==2:
            return f"💰 Total Fee is 50,000 rupees"
        elif self.c==3:
            return f"💰 Total Fee is 25,000 rupees"
        else :
            return f"Sorry we can't accomodate for fee,because you cann't get a seat in our college "   
def Show_details(user:Student):
   print( user.get_details()) 
   print(user.enroll_in_cource()) 
   print(user.calculate_fee())
   print()
   
u=UndergraduateStudent("anil",'@4289',23000,'aiml')
p=PostgraduateStudent('vijay','@7372',4900,'cyber')
d=Diploma('pavan',"27B1",9900,'mechanical')
print(Show_details(u))
print(Show_details(p))
print(Show_details(d))