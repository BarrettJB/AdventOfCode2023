file = 'input.txt'
res = 0
debug = False

with open(file) as input:
    for line in input.readlines():
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
            print(f"{line[:-1]}:{calib_val}")
        res += calib_val

print("===================")
print(f"Answer: {res}")
print("===================")
