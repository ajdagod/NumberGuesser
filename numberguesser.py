guess=input(" Guess The Number(1-9) ")
number=random.randint(1,9)

if (guess>number):
    print(" Try a little lower ")
if (guess<number):
    print(" Try a little higher ")
if (guess=number):
    print("YOU ARE RIGHT")

