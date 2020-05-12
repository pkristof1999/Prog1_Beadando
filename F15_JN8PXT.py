def rendezes(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j][0] > lst[j+1][0]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j+1] = tmp
            elif lst[j][0] == lst[j+1][0]:
                if lst[j][1] < lst[j+1][1]:
                    tmp = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j+1] = tmp

    for i in range(0, len(lst)):
        print(f"{lst[i]}")
        
t = ()
lst = []
while True:
    a = input("Adjon meg egy nevet, egy életkort és egy magasságot (név, életkor, magasság)! ")
    if a == "0":
        break
    a, b, c = a.split(", ")
    t += (a, b, c)
    lst.append(t)
    t = ()

rendezes(lst)
