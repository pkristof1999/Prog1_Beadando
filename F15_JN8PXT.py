def rendezes(lst):
    lst = sorted(lst)
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