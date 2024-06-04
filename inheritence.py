import os
os.system('cls')

class Orang:
    def __init__(self,pekerjaan,makan):
        self.pekerjaan = pekerjaan
        self.makan = makan
    
    def output(self):
        print(f' Pekerjaan : {self.pekerjaan} \n Nama : {self.makan}   \n Email : {self.email}')
class Genz(Orang):
    def __init__(self,pekerjaan,makan,email):
        super().__init__(pekerjaan,makan)
        self.email = email

    def output(self):
        print(f' Pekerjaan : {self.pekerjaan} \n Nama : {self.makan}   \n Email : {self.email}')

petani = Orang('Petani','nasi')
dokter = Genz('Dokter', 'nasi','dokterganteng123@gmail.com')
programmer = Genz('Programmer','Lapa-Lapa','irfansangprogrammer@gmail.com') 

petani.output()
print()
dokter.output()
print()
programmer.output()
print()
        



