import time

x = input('Введите дату рождения (ДД/ММ/ГГГГ): ')
then = time.mktime(time.strptime(x,'%d/%m/%Y'))
now = time.mktime(time.localtime())
print("Поздравляю! Вы прожили " + str((now-then)//86400) + " дней!")