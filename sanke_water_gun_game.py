import random

print("\t\t#### THIS IS A GAME ####")
i=0
l=["w","s","g"]
c=0
u=0
while i<10:
    me=input("\n\t\t\ts: snake\n\t\t\tw: water\n\t\t\tg: gun\n\tENTER:")
    com=random.choice(l)
    if com=="g" and me=="w":
        print(f"com is win com choice {com}")
        c=c+1
    
    elif com=="g" and me=="g":
        print(f"both are same com={com}:you={me}")
        print(f"point: com={c}   you={u}")
    
    elif com=="w" and me=="w":
        print(f"both are same com={com}:you={me}")
        print(f"point: com={c}   you={u}")
    
    elif com=="s" and me=="s":
        print(f"both are same com={com}:you={me}")
        print(f"point: com={c}   you={u}")
        
    elif com=="g" and me=="s":
        print(f"com is win com={com}:you={me}")
        print(f"point: com={c}   you={u}")
        c=c+1
    
    elif me=="s" and com=="w":
        print(f"you are win com={com}:you={me}")
        print(f"point: com={c}   you={u}")
        u=u+1
    
    elif com=="s" and me=="w":
        print(f"com is win com={com}:you={me}")
        print(f"point: com={c}   you={u}")
        c=c+1
    
    elif me=="g" and com!="g":
        print(f"you are win com={com}:you={me}")
        print(f"point: com={c}   you={u}")
        u=u+1
    
    elif me!="w" or me!="s" or me!="g":
        print("you are input wrong charecter or empty")
    
        
    i=i+1

if c>u:
    print(f"\n\ncomputer is win computer score is {c}")
else:
    print(f"\n\nyou are win your score is {u}")
