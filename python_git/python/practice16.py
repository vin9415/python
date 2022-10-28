#do it your self

a = int(input("year:"))
b = int(input("salary:",))

if a>=10:
 bonus = b*0.1
 total=b+bonus
 print("this is your total:", total)

elif 6<=a>10:
    bonus= b*0.8
    total=b+bonus
    print("this your salary:",total)

elif a<6:
    bonus=b*0.5
    total=b+bonus
    print("this is your salary:",total)



   



