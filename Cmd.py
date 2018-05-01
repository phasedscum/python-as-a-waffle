#file = open("commands.txt" , "r")
#for line in file:
#    print(line)


with open("commands.txt") as file:
    line = [l.strip() for l in file]
    print(line)