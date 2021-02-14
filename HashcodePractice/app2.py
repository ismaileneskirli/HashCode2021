import operator
import random
from collections import OrderedDict
from operator import itemgetter
file = open("e_many_teams.in","r")
lines = []
given_pizzas = []

def sortindex(index):
    def key_func(item):
        key, value = item
        return (value[index], key)
    return key_func

def Cloning(li1): 
    li_copy = [] 
    li_copy.extend(li1) 
    return li_copy 


first_line = file.readline().split()
pizza_number = int(first_line[0])#How many pizza do we have ?
two_groups = int(first_line[1]) # How many groups there are with 2 people ?
three_groups = int(first_line[2]) # 3 people 
four_groups = int(first_line[3]) # 4 people
no_teams_given = 0
i = 0
for line in file:
    line = line.rstrip() #stripping by spaces lines from file.
    ingredient_nbr=int(line.split()[0]) # first element of stripped line is number of ingredients.
    ingredients = line.split()[1:] # the rest of the array is ingredients.
    #lines[i] = ingredient_nbr,ingredients
    lines.append([i,ingredient_nbr,ingredients])
    i += 1

    
sorted_list = Cloning(lines)
sorted_list.sort(key= itemgetter(1), reverse=True)
#print(sorted_list)
#Sorting list according to nbr of ingredints from higher to lower.
#sorted_list = sorted(lines.items(), key=sortindex(0),reverse=True)
#Testing if its all good
#for i in range (5):
#    print(sorted_list[i+1][1][0])

#print(sorted_list)

#Usage of compare function
#pizza1=["onion","egg"]
#pizza2=["tomato","garlic"]
#pizza3=["sausage","onion"]
#pizza4=["mushroom,tomato"]
#Compare function takes 
   
def compare (pizza1,pizza2, pizza3 = [],pizza4 =[]):  # 2 optional parameters. 
    pizza=pizza1+pizza2+pizza3+pizza4
    pizza = set(pizza)
    seen = set()
    result = []
    for item in pizza:
        if item not in seen:
            seen.add(item)
            result.append(item)    
    return len(result)


def distribute(groupSize): # This function finds the optimal pizzas to distribute in 100 tries.
    #generate four distinct int between 0-20
    randomArr = []
    max = 0
    keystoPop = [] 
    global two_groups
    global three_groups
    global four_groups
    global no_teams_given
    for i in range (100):   # find the max nbr of ingredients in 100 epoques
        randomArr.clear()
        # generate groupSize different numbers in range 1-6
        #print(randomArr)
        if groupSize == 4:
            randomArr= random.sample(range(-1,int(len(sorted_list))), groupSize)
            if max < compare(sorted_list[randomArr[0]][2],
            sorted_list[randomArr[1]][2],sorted_list[randomArr[2]][2],
            sorted_list[randomArr[3]][2]):
                keystoPop.clear()
                max = compare(sorted_list[randomArr[0]][2],
                sorted_list[randomArr[1]][2],sorted_list[randomArr[2]][2],
                sorted_list[randomArr[3]][2])
                keystoPop = Cloning(randomArr) 
        if groupSize == 3:
            randomArr= random.sample(range(-1,int(len(sorted_list))), groupSize)            
            if max < compare(sorted_list[randomArr[0]][2],
            sorted_list[randomArr[1]][2],sorted_list[randomArr[2]][2]):
                keystoPop.clear()
                max = compare(sorted_list[randomArr[0]][2],sorted_list[randomArr[1]][2],sorted_list[randomArr[2]][2])
                keystoPop = Cloning(randomArr)     
        if groupSize == 2:
            randomArr= random.sample(range(-1,len(sorted_list)), groupSize)            
            if max < compare(sorted_list[randomArr[0]][2],sorted_list[randomArr[1]][2]):
                max = compare(sorted_list[randomArr[0]][2],sorted_list[randomArr[1]][2])
                keystoPop.clear()
                keystoPop = Cloning(randomArr) 
    #TODO:max olduğu zamanki pizzaları dağıt, sonra listden çıkar.,
    if groupSize == 4 :       
        distribution = "4"
        distribution = distribution + " " + str(sorted_list[keystoPop[0]][0])+" "+ str(sorted_list[keystoPop[1]][0])+" "+str(sorted_list[keystoPop[2]][0])+" "+str(sorted_list[keystoPop[3]][0])
        given_pizzas.append(distribution)
        #print(given_pizzas)
        four_groups -= 1
        #TODO pop given pizzas from sorted_list
        keystoPop.sort(reverse=True)
        #print(keystoPop)
        for item in keystoPop:
            sorted_list.pop(item)

    if groupSize == 3 :       
        #print(keystoPop)
        distribution = "3"
        distribution = distribution + " " + str(sorted_list[keystoPop[0]][0])+" "+ str(sorted_list[keystoPop[1]][0])+" "+str(sorted_list[keystoPop[2]][0])
        given_pizzas.append(distribution)
        #print(given_pizzas)
        three_groups -= 1
        keystoPop.sort(reverse=True)        
        for item in keystoPop:
            sorted_list.pop(item)    
    if groupSize == 2 :       
        #print(keystoPop)
        distribution = "2"
        distribution = distribution + " " + str(sorted_list[keystoPop[0]][0])+" "+ str(sorted_list[keystoPop[1]][0])
        given_pizzas.append(distribution)
        #print(given_pizzas)
        two_groups -= 1
        keystoPop.sort(reverse=True)
        #print(two_groups)
        for item in keystoPop:
            sorted_list.pop(item)
    no_teams_given +=1

while len(sorted_list) != 0:
    if len(sorted_list)  >= 4 and four_groups > 0: 
            distribute(4)
    elif len(sorted_list) >= 3 and three_groups > 0:
            distribute(3) 
    elif len(sorted_list)  >= 2 and two_groups > 0:
            distribute(2)
    else:
        break



f = open("e.txt", "w")
given_pizzas.insert(0,str(no_teams_given))
for line in given_pizzas:
     f.write(line + "\n")
f.close()
