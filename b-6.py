import random

men_num = int(input("サイコロの面の数は?: "))
nankai = int(input("何回振りますか?: "))
kekka_list = []
for i in range(nankai):
    kekka = random.randint(1, men_num)
    kekka_list.append(kekka)
print(kekka_list)
