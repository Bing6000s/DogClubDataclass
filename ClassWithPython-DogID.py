"""Bingsong Yu, Penn state abington, cmpsc 132"""
"""
Data class assignment based on the dog's 
eligibility to stay in the Bing's club. 
To be eligibl, the dog needs to be in the breed
that I wanted.

At first it will print out the information of the dog, 
then the eligiblity on the dog to be in Bing's club.
"""
from datetime import date

class Dog():
    
    def __init__(self,name ,gender,breed,weight,birth,health,shots,kennelmonths,):

        self.name = name
        self.gender = gender
        self.breed = breed
        self.weight = weight
        self.birth = birth
        self.health = health
        self.hasshot = shots
        self.kennelmonths = kennelmonths

    def doginfo(self):#info for name, gender, weight, breed, birthdate, health, immunization and months in kennel.
        dog_gender = ''
        if self.gender == 1:
            dog_gender = 'Male'
        else:
            dog_gender = 'Female'
        
        doghealth = ''
        if self.health == "1":
            doghealth = 'Very Poor'
        if self.health == "2":
            doghealth = "Poor"
        if self.health == "3":
            doghealth = "Fair"
        if self.health == "4":
            doghealth = "Good"
        if self.health == "5":
            doghealth = "Healthy"
        
        
        immunization = ''
        if self.hasshot == False:
            immunization = ("No Shots")
        if self.hasshot == True:
            immunization = ("Has shots.")

        print("__________________________________")
        print("       Dog's information:")
        print("Name:    ",self.name)
        print("Gender:  ",dog_gender)
        print("Breed:   ",self.breed)
        print("Weight:  ",self.weight)
        print("Birth:   ",self.birth)
        print("Health:  ",doghealth)
        print("Immunization info:    ",immunization)
        print("Months in kennel:    ",self.kennelmonths)
    

    def permission(self):
        acceptedbreed = (list(map(lambda x: x.lower(), ['Bulldog','Chihuahua','Bichon Frise','Siberian Husky','Boxer','Alaskan Malamute'])))
        comparing = self.breed.lower()
        x = 'Not allowed'
        for i in acceptedbreed:
            if (i == comparing):
                x = 'Allowed'
        return x


    def criticalinfo(self): #will calculate weight class, age, and equivalent age in human years, 

        today = date.today()
        age =  today.year - self.birth.year - ((today.month, today.day) < (self.birth.month, self.birth.day))


        weightclass = ''
        '''calculate weight class'''
        '''small: <21, medium: 21-50, large: >50'''
        if self.weight<21:
            weightclass = "Small"
        if self.weight>50:
            weightclass = "Large"
        if 20<self.weight<51:
            weightclass = "Medium" 
        else:
            weightclass = "Unknown"

        '''calculate age'''


        #calculate human year
        smallweight = [15,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80]
        mediumweight = [15,24,28,32,36,42,47,51,56,60,65,69,74,78,83,87]
        largeweight = [15,24,28,32,36,45,50,55,61,66,72,77,82,88,93,120]


        inhumanyears = ''
        if weightclass == "Small":
            inhumanyears = smallweight[age-1]
        if weightclass == "Medium":
            inhumanyears = mediumweight[age-1]
        if weightclass == "Large":
            inhumanyears = largeweight[age-1]

        print("Dog age: ",age)
        print("In human years:  ",inhumanyears )


print("Birth must in (MM,DD,YYYY) format.")


"""We add some dogs to our program"""
dog1 = Dog("Alexander the 100th",0,"Husky",42,(2003,12,24),3,True,11)
dog2 = Dog("Little sicky dog",1,"Husky",29,(1999,11,15),1,False,39)
dog3 = Dog("Macy The Frankford Preacher",1,"Alaskan Malamute",89,(20018,1,1),5,True,20)
dog4 = Dog("The Resouvour Dog",0, 'Bichon Frise',99,(2011,9,19),4,25,5)
"Do I want this dog?"
dog1.doginfo()
print("Does this dog has the permission to stay?", dog1.permission())
dog2.doginfo()
print("Does this dog has the permission to stay?", dog3.permission())
dog3.doginfo()
print("Does this dog has the permission to stay?", dog3.permission())
dog4.doginfo()
print("Does this dog has the permission to stay?", dog3.permission())