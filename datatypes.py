age = 18 #integer
weight = 78.9  #Float
greeting = "Hello there"   #String
isMammal = True   #Boolean


#Datastructures - Multiple elements in one variable
fruits = [ "Banana", "Mango", "Cherry"]  #List - Is Ordered and Changeable - Different datatypes

Courses = [  "MIT", "DataScience", "Cybersecurity"]#Array - Similar datatypes

Cars = ( "Ford", "G-Wagon", "Mazda", "Mitsubishi") #Tuple - Ordered and Unchangeable

countries = {"Tanzania", "India", "Italy"}  #Set - Unordered  and Unchangeable

Student = {
    "firstname" : "Jeff",
    "Course" : "MIT",
    "Age" : 17,
    "Nationality" : "Kenya"

}#Dictionary - Key value pair



print( "student is", age,"years old")
print( weight)
print("Is animal a mammal ? :", isMammal)
print(fruits)
print(countries)


#Typecasting - Converting one datatype to another

print(float(age))
print(int(weight))


