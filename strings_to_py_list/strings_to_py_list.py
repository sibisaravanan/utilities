with open("strings.txt", "r") as f:
    lines = f.readlines()

list_of_lines = [line.strip() for line in lines]

with open("final.py", "w") as file:
    file.write(str(list_of_lines))
