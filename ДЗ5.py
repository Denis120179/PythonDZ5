#Напишите программу, удаляющую из текста все слова, содержащие "абв".

'''
text = input("Введите текст:  ")
text = text.split()

def Del(w): return False if 'абв' in w else True
text = list(filter(Del, text))
print(" ".join(text))
'''

# Создайте программу для игры с конфетами человек против человека. Реализовать игру в терминале. 
# Первый ход определяется жеребьевкой. В конце объявляется победитель

'''
import random
name1 = input("Введите имя первого игрока:  ")
name2 = input("Введите имя второго игрока:  ")
sweets = int(input("Введите количество конфет:  "))

n = random.randrange(1,3)
if n == 1:
    print("Первый ход делает", name1)
else:
    print("Первый ход делает", name2)

player = name1 if n == 1 else name2

while sweets > 0:
    print(f"Ваш ход {player}")
    a = int(input("Сколько конфет берете?: "))
    if a > 28: print("Вы взяли больше 28 конфет")
    else: 
        sweets = sweets - a 
        player = name2 if player == name1 else name1
        if sweets > 0: 
            print("Конфет осталось:", sweets)            
        else: 
            print("Игра закончена")
winner = name2 if player == name1 else name1
print(f"Победитель {winner}")                
'''    

# Реализуйте RLE алгоритм: модуль сжатия и восстановления данных
'''
def rle_encode(data):
    encoding = " "
    prev_char = data[0]
    count = 0
    for char in data:
        if char != prev_char:
            encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    encoding += str(count) + prev_char
    return encoding

def rle_decode(data):
    decode = " "
    count = " "
    for char in data:
        if char.isdigit():
            count += char            
        else:
            decode += int(count)*char 
            count = " "           
    return decode

text1 = input("Введите строку:  ")
print(rle_encode(text1)) 
text2 = rle_encode(text1)
print(text2)
print(rle_decode(text2))
'''

