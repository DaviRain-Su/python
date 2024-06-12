# with keyword closes the file once access to it is no longer needed
with open("../data/pi_digits.txt") as file_object:
    #contents = file_object.read()
    #print(contents.rstrip())
    for line in file_object:
        print(line.rstrip()) # rstrip() removes the extra blank line that is created by print function

print("----------------------------")

filename = "../data/pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
