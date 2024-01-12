file = 'test2.txt'
debug = True
res = 0

with open(file) as input:
    for line in input.readlines():
        #str replace option
        #this lets us reuse most of the code from part 1
        #this was my first thought but I don't like it
        orig_line = line
        line = line.replace("zero","0")
        line = line.replace("one","1")
        line = line.replace("two","2")
        line = line.replace("three","3")
        line = line.replace("four","4")
        line = line.replace("five","5")
        line = line.replace("six","6")
        line = line.replace("seven","7")
        line = line.replace("eight","8")
        line = line.replace("nine","9")
        first_num = -1
        last_num = -1
        for char in line:
            try:
                val = int(char)
                first_num = val
                #found it get out of here
                break
            except ValueError:
                #move along nothing but non ints here
                continue
        for char in reversed(line):
            try:
                val = int(char)
                last_num = val
                #found it get out of here
                break
            except ValueError:
                #move along nothing but non ints here
                continue
        if(first_num == -1 or last_num == -1):
            print("ERROR: Failed to find numbers in line")
            print(line)
            exit(1)
        calib_val = 10*first_num+last_num
        if(debug):
            print(f"{orig_line[:-1]}:{calib_val}")
        res += calib_val

print("===================")
print(f"Answer: {res}")
print("===================")
