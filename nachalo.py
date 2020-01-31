first_name = "Eric"
question = ", would you like to learn some Python today?"
print(first_name.upper() +question)
my_14 = 14
print("Мое л число " + str(my_14)) #str - приводит число к строковому виду, сначала пишется str(), а в скобках указывается переменная

#списки
#Называть списки во множественном числе cycleS
#имя переменной cycles = потом квадратные скобки, в которых перечисляется состав списка напр:
#cycles = ['trek', 'redline']
cycles = ['trek', 'redline', 'cannon']
print(cycles)
#обращение к элементам списка начинается с 0 print(cycles[0])
print(cycles[0])
print(cycles[0].title()) #добавление метода title (Вывод с большой буквы)
print(cycles[-1].upper()) #если запросить -1, то выведет последний элемент из списка-2 предпоследний (добавил методо Upper) 
print("Мой первый велосипед был "+cycles[-1].upper()+".") #пример вытаскивания из списка и засовывания в сообщение
#изменение элемента в списке
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'yokohama' #перед переменной ставится номер элемента
print(motorcycles[0])
#добавление элемента в конец списка
motorcycles.append('ducatti')
print(motorcycles)
#построение списка добавлением
motorcycles = []
motorcycles.append('gnoy')
motorcycles.append('cherv')
print(motorcycles)
#вставка - асафка в список метод insert(0 - позиция,)
motorcycles = ['honda', 'suzuki', 'yoko']
motorcycles.insert(0, 'ducatti')
print(motorcycles)
#удаление из списка
del motorcycles[2]
print(motorcycles)
#удаление с дальнейшим использованием, метод pop - убирает, но не удаляет из списка элемент (последний)
motorcycles = ['honda', 'suzuki', 'ducatti']
motorcycles_popped = motorcycles.pop() 
print(motorcycles)
print(motorcycles_popped)
#удаление по ЗНАЧЕНИЮ элемента
motorcycles = ['honda', 'suzuki', 'bmw']
motorcycles.remove('suzuki')
print(motorcycles)
#удаление по значение с использованием
motorcycles = ['honda', 'suzuki', 'bmw']
print(motorcycles[0].title())
too_expensive = 'bmw'
motorcycles.remove(too_expensive)
print("\nA " +too_expensive.title()+" для педиков")
#задание
gosti = ['masha', 'petya','klava','ivan']
print(gosti)
priglashenie = "Всем быстро собраться"
print(priglashenie+" " +gosti[0].title())
print(priglashenie+" " +gosti[1].title())
print(priglashenie+" " +gosti[2].title())
ne_prishla = 'ivan'
gosti.remove(ne_prishla)
print(gosti)
print(ne_prishla)
gosti.append('volodya')
print(gosti)
gosti.insert(0, 'begemot')
gosti.insert(3, 'shalava')
gosti.append('gnome')
print(gosti)
###Сортировка переменная.sort()
gosti.sort()
print(gosti)
###Обратная сортировка .sort(reverse=true)
gosti.sort(reverse=True)
print(gosti)
###Временная сортировка(БЕЗ ИЗМЕНЕНИЯ СПИСКА)
print(sorted(gosti,reverse=True))
###Метод len - для определения количества объестов в списке
print(len(gosti))

############Задание#############
strany = ['tunis', 'turciya', 'canada', 'belgiya', 'germaniya']
strany.sort()
print(strany)    



