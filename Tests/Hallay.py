# p - минимальный парог пропуска
p = 23

# s - студент
s = ['Ivanov', 115, 25]
s1 = ['Petrov', 115, 22]
s2 = ['Sidorov', 115, 21]

x9 = [25, 22, 21]

x = [25]
x1 = [22]
x2 = [21]

name = s
name1 = s1
name2 = s2
for i in x:
    if i <= p:
        print(s)
    else:
        print("no")
for i in x1:
    if i <= p:
        print(s1)
    else:
        print("no")
for i in x2:
    if i <= p:
        print(s2)
    else:
        print("no")
