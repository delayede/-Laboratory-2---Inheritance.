import math
import sys


"""
Завдання 1
1. Створити клас Figure з методами обчислення площі та
периметра, а також методом, що виводить інформацію
про фігуру на екран.
2. Створити похідні класи: Rectangle (прямокутник), Circle
(коло), Triangle (трикутник) зі своїми методами
обчислення площі і периметра.

"""

class Figure(object):
    """
    Generic Shape object
    """
    def area(self):
        """
        Area of shape
        """
        pass

    def perimeter(self):
        """
        Perimeter of shape
        """
        pass


    def info():
        rect = Rectangle(5, 4)
        print("Rectangle(5, 4)")
        print("  Area: " + str(rect.area()))
        print("  Perimeter: " + str(rect.perimeter()))
        
        square = Triangle(4,5,8)
        print("Triangle(4,5,8)")
        print("  Area: " + str(square.area()))
        print("  Perimeter: " + str(square.perimeter()))
       
        circle = Circle(5)
        print("Circle(5)")
        print("  Area: " + str(circle.area()))
        print("  Perimeter: " + str(circle.perimeter()))

class Triangle(Figure):
    """
    Basic square class
    """
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
    	p = (self.a+self.b+self.c) / 2
    	return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5 
             
    
    def perimeter(self):
        return self.a + self.b+self.c

class Rectangle(Figure):
    """
    Basic rectangle class
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return  (self.length +  self.width) *2

class Circle(Figure):

	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius * self.radius

	def perimeter(self):
		return 2 * math.pi * self.radius


"""
Завдання 2
1. Створити клас Function з методом обчислення значення
функції y = f (x) в заданій точці.
2. Створити похідні класи: Line (y = ax + b), Kub (y = ax2 +
bx + c), Hyperbola зі своїми методами обчислення
значення в заданій точці.

"""

class Function(object):
	"""docstring for Function"""
	def __init__(self, x):
		self.x = x

	def calculation():
		pass

	def info():
		line = Line(4,2,2)
		print("Line: " + str(line.calculation_Line()))
		cube = Cube(4,2,2,2)
		print("Cube: " + str(cube.calculation_Cube()))
		hyperbola = Hyperbola(4,2)
		print("Hyperbola: " + str(hyperbola.calculation_Hyperbola()))

class Line(Function):
	def __init__(self, x,a,b):
		Function.__init__(self, x)
		self.a = a
		self.b = b

	def calculation_Line(self):
		return self.x * self.a + self.b



class Cube(Function):
	def __init__(self, x,a,b,c):
		Function.__init__(self, x)
		self.a = a
		self.b = b
		self.c = c

	def calculation_Cube(self):
		return self.a * self.x * self.x +self.b * self.x + self.c

class Hyperbola(Function):
	def __init__(self,x,a):
		Function.__init__(self,x)
		self.a = a
	def calculation_Hyperbola(self):
		return self.a / self.x

"""
Завдання 3
1. Створити клас Видання з методами дозволяє вивести на
екран інформацію про видання.
2. Створити похідні класи: Книга (назва, прізвище автора,
рік видання, видавництво), Стаття (назва, прізвище
автора, назву журналу, його номер і рік видання),
Електронний ресурс (назву, прізвище автора, заслання,
анотація) зі своїми методами виведення інформації на
екран.
"""


class Publish(object):

	def __init__(self,title,author_surname):
		self.title = title
		self.author_surname = author_surname

	def info():
		people = [ Book("Book1\t", "Bob\t", "1999\t", "author \n") ,Article("Book2\t","Sam\t","GG\t","1\t","2000\n"),Electronic_resource("Book3\t","Kate\t","http\t","???")]
		for person in people:
			person.info()


class Book(Publish):
	def __init__(self, title,author_surname, publish_year, publisher ):
		Publish.__init__(self,title,author_surname)
		self.publish_year = publish_year
		self.publisher = publisher

	def info(self):
		print("Title:", self.title, "author Surname:", self.author_surname,"Publish year:", self.publish_year,"publisher:", self.publisher )
		
class Article(Publish):
	def __init__(self, title,author_surname,magazine,number, publish_year):
		Publish.__init__(self,title,author_surname)
		self.magazine = magazine
		self.number = number
		self.publish_year = publish_year

	def info(self):
		print("Title:", self.title, "author Surname:", self.author_surname,"magazine:", self.magazine,"Number:", self.number,"Publish year:", self.publish_year )


class Electronic_resource(Publish):
	def __init__(self, title,author_surname,exile,annotation, ):
		Publish.__init__(self,title,author_surname)
		self.exile = exile
		self.annotation = annotation
		
	def info(self):
		print("Title:", self.title, "author Surname:", self.author_surname,"exile:", self.exile,"annotation:", self.annotation)


"""
Создать класс Trans с методами позволяет вывести на экран информацию о транспортном средстве 
и определить грузоподъемность транспортного средства.
• Создать производные классы: Легковая машина (марка, номер, скорость, грузоподъемность).
• Мотоцикл (марка, номер, скорость, грузоподъемность, наличие коляски, 
	при этом если коляска отсутствует, то грузоподъемность равна 0)
• Грузовик (марка, номер, скорость, грузоподъемность, наличие прицепа,
 при этом если есть прицеп, то грузоподъемность увеличивается в два раза)
  со своими методами вывода информации на экран, и определения грузоподъемности.
"""
class Trans:
	def __init__(self, brand, number, speed):
		self.brand = brand
		self.number = number
		self.speed = speed
       
	def info():
		cars = [Passenger_car("BMW","JO6JY","300m/h","4"),Moto("Honda","O6G3N9","250km/h",4,True),Truck("Ford","FV45ER","120km/h",4,True)]
		for car in cars:
			car.display_info()
		cars[1].stroller = False
		cars[1].display_info()
		cars[2].stroller = True
		cars[2].carrying = 6
		cars[2].display_info()



class Passenger_car(Trans):
	def __init__(self,brand, number, speed,carrying):
		Trans.__init__(self,brand, number, speed)
		self.carrying = carrying

	def display_info(self):
		print("Brand:", self.brand, "\tnumber:", self.number,"\tspeed:", self.speed,"\tcarrying:", self.carrying)


class Moto(Trans):
 
	def __init__(self, brand, number, speed,carrying, stroller):
		Trans.__init__(self,brand, number, speed)
		self.__carrying = carrying
		self.__stroller = stroller  # устанавливаем возраст
 
	@property
	def stroller(self):
		return self.__stroller
 
	@stroller.setter

	def stroller(self, stroller):
		if stroller == True:
			self.__stroller = stroller  
		elif stroller == False:
			self.__carrying = 0
			self.__stroller = stroller
		else:
			print("Недопустимый возраст")        
 
	@property
	def carrying(self):
			return self.__carrying

	@carrying.setter
	
	def carrying(self, carrying):
		self.__carrying = carrying			

	def display_info(self):
		print("Brand:", self.brand, "\tnumber:", self.number,"\tspeed:", self.speed,"\tcarrying:", self.__carrying,"\tstroller:", self.__stroller)
 
 
class Truck(Trans):
	def __init__(self, brand, number, speed,carrying, stroller):
		Trans.__init__(self,brand, number, speed)
		self.__carrying = carrying
		self.__stroller = stroller  # устанавливаем возраст
		
	@property
	def carrying(self):
			return self.__carrying

	@carrying.setter
	
	def carrying(self, carrying):		
		if self.stroller == True:
			self.__carrying = carrying * 2	 
		elif self.stroller == False:
			self.__carrying = 0

	@property
	def stroller(self):
		return self.__stroller
 
	@stroller.setter

	def stroller(self, stroller):
		if stroller == True:
			self.__stroller = stroller  
		elif stroller == False:
			self.__carrying = 0
			self.__stroller = stroller
		else:
			print("Недопустимый возраст")        

	def display_info(self):
		print("Brand:", self.brand, "\tnumber:", self.number,"\tspeed:", self.speed,"\tcarrying:", self.__carrying,"\tstroller:", self.__stroller)
 
"""
Создать абстрактный класс Persona с методами, позволяющим вывести на экран информацию о персоне,
 а также определить ее возраст (на момент текущей даты).

2.Создать производные классы: Абитуриент (фамилия, дата рождения, факультет),
Студент (фамилия, дата рождения, факультет, курс), 
Преподаватель (фамилия, дата рождения, факультет, должность, стаж), 
со своими методами вывода информации на экран, и определения возраста.

"""
from datetime import datetime, date

class Persona(object):
	def __init__(self, family,birth,faculty):
		self.family = family
		self.birth = birth
		self.faculty = faculty

	def calculate_age():
		dt_string = "12/11/2010"
		born = datetime.strptime(dt_string, "%d/%m/%Y")
		today = date.today()
		return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

	def info():
		univer = [Enrollee("Tompson","17/11/2000","251"), Student("Jonsons","17/11/2002" ,"351", "2"), Teacher("Polorised","17/11/1985","555","CEO","5 years") ]
		for stud in univer:
			stud.display_info()

class Enrollee(Persona):
	"""docstring for """
	
	def __init__(self, family,birth,faculty):
		Persona.__init__(self,family,birth,faculty)


	def display_info(self):
		age = Enrollee.calculate_age(self.birth)
		print("Family:", self.family, "\tBirth:", self.birth,"\tFaculty:", self.faculty ,"\tAge:", age )
 

	def calculate_age(birth):
		born = datetime.strptime(birth, "%d/%m/%Y")
		today = date.today()
		age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		return age
		
class Student(Persona):
	"""docstring for """
	
	def __init__(self, family,birth,faculty,course):
		Persona.__init__(self,family,birth,faculty)
		self.course = course

	def display_info(self):

		age = Student.calculate_age(self.birth)
		print("\nFamily:", self.family, "\tBirth:", self.birth,"\tFaculty:", self.faculty ,"\tCource:", self.course,"\tAge:", age )
 

	def calculate_age(birth):
		born = datetime.strptime(birth, "%d/%m/%Y")
		today = date.today()
		age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		return age
		

class Teacher(Persona):
	"""docstring for """
	
	def __init__(self, family,birth,faculty,post,experience):
		Persona.__init__(self,family,birth,faculty)
		self.post = post
		self.experience = experience

	def display_info(self):
		age = Teacher.calculate_age(self.birth)
		print("\nFamily:", self.family, "\tBirth:", self.birth,"\tFaculty:", self.faculty ,"\tPost:", self.post,"\tExperience:", self.experience,"\tAge:", age )
 

	def calculate_age(birth):
		kk = "dfdf"
		born = datetime.strptime(birth, "%d/%m/%Y")
		today = date.today()
		age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		return age
		












Teacher.display_info(kk)

Persona.info()



sys.exit()
Persona.info()
Publish.info()
Trans.info()
Function.info()
Figure.info()
