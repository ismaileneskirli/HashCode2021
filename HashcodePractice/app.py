#UTKU USLU VERSION 1
file = open("a_example.txt","r")
#file = open("b_little_bit_of_everything.txt","r")
#file = open("c_many_ingredients.in","r")
#file = open("d_many_pizzas.in","r")
#file = open("e_many_teams.in","r")

lines = []
first_line = file.readline().split() #Reads the first line.
for line in file:
    line = line.rstrip() #stripping by spaces lines from file.
    lines.append(line) # appending every line to lines array.
file.close()
#CONTROL
#print(first_line)
#print(lines)

pizza_number = int(first_line[0])#How many pizza do we have ?
two_groups = int(first_line[1]) # How many groups there are with 2 people ?
three_groups = int(first_line[2]) # 3 people 
four_groups = int(first_line[3]) # 4 people

for i in range(len(lines)):
    lines[i] = str(i) + " " + lines[i]

#print(lines)
lines.sort(key = len) # Sort arrray according to character length in each index.
lines.reverse() # By default sort function sorts from shortest to longest, by reversing we got pizzas which have more ingredient at the top.
#print(lines)

# Start distributing pizzas.
no_teams_given = 0
given_pizzas = []
exit = 0
while pizza_number != 0:

    if pizza_number >= 4 and four_groups > 0: 
        a = "4"
        team_pizzas = []
        for i in range(4):
            pizza_no = lines[0].split()
            a = a + " " + pizza_no[0]
            lines.pop(0)
            pizza_number = pizza_number - 1
        four_groups = four_groups - 1   
        no_teams_given = no_teams_given + 1
        given_pizzas.append(a)
    elif pizza_number >= 3 and three_groups > 0:
        a = "3"
        for i in range(3):
            pizza_no = lines[0].split()
            a = a + " " + pizza_no[0]
            lines.pop(0)
            pizza_number = pizza_number - 1
        three_groups = three_groups - 1 
        no_teams_given = no_teams_given + 1
        given_pizzas.append(a)
    elif pizza_number >= 2 and two_groups > 0:
        a = "2"
        for i in range(2):
            pizza_no = lines[0].split()
            a = a + " " + pizza_no[0]
            lines.pop(0)
            pizza_number = pizza_number - 1
        two_groups = two_groups -1
        no_teams_given = no_teams_given + 1
        given_pizzas.append(a)
    else:
        break

f = open("a.txt", "w")
#f = open("b.txt", "w")
#f = open("c.txt", "w")
#f = open("d.txt", "w")
#f = open("e.txt", "w")

given_pizzas.insert(0,str(no_teams_given))

for line in given_pizzas:
     f.write(line + "\n")
f.close()


print(sorted_list)