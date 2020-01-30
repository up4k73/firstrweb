#############список и цикл for###############
## for magician(вводится новая переменная)
magicians = ['alice', 'david', 'carolina']
for magician in magicians: ## новая переменная magician 
    print(magician) #тут к ней обращается компилятор
    print(magician.title()+"that was a great trick")
    print("i can't wait for your next trick "+magician.title()) 
    #цикл будет работать до последнего значения в списке

my_pizza = ['pepperoni','muchacho','karbonara']
for mylove in my_pizza:
    print(mylove)
    print("I really love "+mylove.title())
print("i really love pizza")
#########функция range()###########
for value in range (1,10):
    print(value)
###################################
numbers = list(range(1,6)) #преобразование в числовой список (массив)
print(numbers)
#########список четных чисел#######
numbers = list(range(2,21,2)) #####здесь третья двойка показывает на число, на которое будет увеличиваться, первая - с какого начинается
print(numbers)
########Возведение в степень и добавление к массиву#########
squares =[]
for value in range(2,21,2):
    square=value**2
    squares.append(square)
print(squares)
#########генератор списка########!!!!!!!!
squares = [value**3 for value in range(2,20,2)]
print(squares)

###задание###
##вывести числа от 1 до 20
chisla = []
for value in range(1,21):
    print(value)
########от 1 до 1кк#######
##chisla = [value for value in range(1,1000001)]
##print(chisla)
##########Суммирование миллиона чисел##########
chisla = [value for value in range(1,1000002)]
print(min(chisla))
print(max(chisla))
print(sum(chisla))

###памятка
#	squares = []
#	for value in range(1,11):
#	 square = value**2
#	 squares.append(square)
#	print(squares)




