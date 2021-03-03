import sys

file_dict = {
0:["a.txt","a_submission.txt"],
1:["b.txt","b_submission.txt"],
2:["c.txt","c_submission.txt"],
3:["d.txt","d_submission.txt"],
4:["e.txt","e_submission.txt"],
5:["f.txt","f_submission.txt"]
}


file_choice = int(sys.argv[1])
f = open(file_dict[file_choice][0],"r")
street_dict = {}
inter_dict = {}
car_dict = {}

info = f.readline().strip().split()
time = int(info[0])
inter_count = int(info[1])
street_count = int(info[2])
car_count = int(info[3])
bonus = int(info[4])
streets = []
for i in range(inter_count):
    inter_dict[i]=[]

for i in range(street_count):
    line = f.readline().strip().split()
    inter_dict[int(line[1])].append(line[2])
    streets.append(line[2])
for street in streets:
    street_dict[street]=0
for i in range(car_count):
    line = f.readline().strip().split()
    car_dict[i]=line[1:]
for car in car_dict:
    for j in range(len(car_dict[car])):
        street_dict[car_dict[car][j]]+=1

#street_dict =dict(sorted(street_dict.items(), key=lambda item: item[1],reverse=True))
 
# print(inter_dict)
# print(street_dict)

result_dict = {}
for i in range(inter_count):
    result_dict[i] = []

for inter in inter_dict:
    temp_dict = {}
    total=0
    for street in inter_dict[inter]:
        print(inter,street)
        temp_dict[street] = street_dict[street]
        total +=street_dict[street]
    temp_dict =dict(sorted(temp_dict.items(), key=lambda item: item[1],reverse=True))
    for street in temp_dict:
        if total==0:
            ratio=1
        else:
            ratio = int((temp_dict[street]/total)*10)
            if ratio>time:
                ratio=time
        if ratio==0:
            ratio=1
        temp_dict[street] = ratio
    for street in temp_dict:
        result_dict[inter].append([street,temp_dict[street]])
# print(inter_dict)
# print(result_dict)
result_text = str(inter_count)+"\n"
for inter in result_dict:
    result_text = result_text+str(inter)+"\n"
    result_text = result_text+str(len(result_dict[inter]))+"\n"
    for street in result_dict[inter]:
        result_text=result_text+str(street[0])+" "+str(street[1])+"\n"
#print(result_text)

f = open(file_dict[file_choice][1],"w")
f.write(result_text)



