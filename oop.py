class Human():
    def __init__(self,nm,age,h,w,g,cntry): # constructor 
        self.name = nm
        self.age = age 
        self.height = h
        self.weight = w
        self.gender = g
        self.country = cntry

    def show(self):
        print(f'Name: {self.name}')    
        print(f'Age: {self.age}')    
        print(f'Height: {self.height}')    
        print(f'Weight: {self.weight}')    
        print(f'Gender: {self.gender}')    
        print(f'Country: {self.country}')    

# making objects
        
h1 = Human('Ram', 23, 5.6, 67, 'M', 'Nepal')
h2 = Human('Osama', 23, 5.8, 23, 'M', 'Pakistan')

print(h1)
print(h2)

print(h1.name)
print(h2.name)

h1.show() # zyada infromation show karta hai.
print('-'*15)
h2.show()