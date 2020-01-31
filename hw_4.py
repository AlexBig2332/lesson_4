import random

name = 'Lana Den Bill Anna Lara Piter Lo Mike Genry Emmy Nikol Sasha Masha Kirill Platon Filipp Kate Nora Nikolay Jhon'
name_list = name.split()
N = int(input('Введите число имен: '))
name_rand = random.choices(name_list, k=N)
print(name_rand)


print()
print('     2. Напишите функцию вывода самого частого имени из списка на выходе функции F')
def F_max(name_rand):
    return max(name_rand, key = name_rand.count)
print('Самое часте именя из списка: ', F_max(name_rand))


print()
print('     3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F')
def F_min(name_rand):
    min_letter = list(map(lambda x: x[0], name_rand))
    return min(min_letter, key = min_letter.count)
print('Самая редкая буква, с которой начинается имя: ', F_min(name_rand))


print()
print('  PRO   4.  В файле с логами найти дату самого позднего лога (по метке времени)')
with open('time.log') as f:
    line = f.readlines()
line.sort()
print('Самый поздний лог: ',  line[-1])

# Пока не разобрался как по метке времени