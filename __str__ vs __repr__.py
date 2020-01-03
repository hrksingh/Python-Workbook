
class Car:
     
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


    def __str__(self):
        return f'a {self.color} car'


    def __repr__(self):
        return f'a {self.color} car with {self.mileage} of mileage'
            


my_car = Car('black', 35956)

print(my_car)
print( )
print(f'Using __str__ : {my_car!s}\n')
print(f'Using __repr__ : {my_car!r}')


 
        

