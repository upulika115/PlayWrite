# Count number of lines in file1.txt

line_count = 0

with open("file1.txt", "r") as file:
    for _ in file:
        line_count += 1

print("Total number of lines: {}".format(line_count))
