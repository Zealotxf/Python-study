def number_append(a):
    i = 0
    numbers = []
    while i < int(a):
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now :", numbers)
        print(f"At the bottom i is {i}")

count = input("列表项数==>")
number_append(count)


#print("The numbers: ")

#for num in numbers:
#    print(num)
def number_append_1(a):
    numbers = []
    for i in range(0,int(a)):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now :", numbers)
        print(f"At the bottom i is {i}")

number_append_1(count)
