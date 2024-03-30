
from rest_framework import status
from http.client import responses


class validator:
    def __init__(self,age,ph_no) -> None:
        self.age=age
        self.ph_no=ph_no
    def validity_age(self):
        if(self.age>=18 and self.age<=100):
            return True
        else:
            return False
        
    def validity_ph(self):
        
        if(self.ph_no is str ):
            self.ph_no=int(self.ph_no)
            if(self.ph_no >10):
                return False
            else:
                return True                   
        else:
            return True

