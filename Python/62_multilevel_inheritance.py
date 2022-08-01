class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes i dance {self.dance} no of times"

class Grandson(Son):

    dance = 6
    def isdance(self):
        return f"Jackson yeeah! yes i ance very swesomely {self.dance} no of times"

ram = Dad()
shayam = Son()
Rohit = Grandson()

print(ram.basketball)