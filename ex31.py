print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do oyu do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print(f"Well, doing {bear} is probaly better.")
        print("Bear run away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Bluseberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revovlers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("You stumble around an fall on a knife and die. Good job!")
