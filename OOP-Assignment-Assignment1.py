# Creating a class called Smarphone 
class Smarphone:  
    def __init__(self, brand, model, price):
        """This is the constructor to initilize the phone details"""  # Typo in "initialize"
        self.brand = brand  
        self.model = model  
        self.price = price  

    def show_details(self):
        """Displays the phone details"""
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")  

# Inheritance example - A gaming phone 
class GamingPhone(Smarphone):  
    def __init__(self, brand, model, price, gpu):
        """Initlizing gaming phone with extra gpu"""  # Spelling mistake "Initlizing"
        super().__init__(brand, model, price)
        self.gpu = gpu  

    def show_details(self):
        """Overriding the method to include GPU details"""
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, GPU: {self.gpu}")  

# Creating objects
phone1 = Smarphone("Samsung", "Galaxy S22", 999)  
phone2 = GamingPhone("Asus", "ROG Phone 6", 1299, "Adreno 730")  

# Showing details
phone1.show_details()  
phone2.show_details()  
