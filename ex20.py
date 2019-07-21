from sys import argv

script, input_file = argv

def print_all(f):                                                               #打印文件f
    print(f.read())

def rewind(f):                                                                  #返回文件f第一行
    f.seek(0)

def print_a_line(line_count,f):                                                 #打印行
    print(line_count,f.readline(),end = "")                                     #readline(P61)-读取文件f的一行，然后将“光标”移动至\n后面
                                                                                #readline会获取\n,为避免打印多一行，添加end = ""
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind,kind of like a tape.")

rewind(current_file)

print("Let's print three lines")

current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
