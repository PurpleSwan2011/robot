class robot:
    name = "Sophia-The Robot"
    
    def introduction(self):
        print("Hi I am a robot")
        
    def details(self):
        print("My name is", self.name)
    
ob = robot()
ob.introduction()
ob.details()