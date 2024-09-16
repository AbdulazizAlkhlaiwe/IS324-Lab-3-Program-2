def update_dict(dict,subj):
    for i in range(len(dict[subj])):
     dict[subj][i] +=5

original_dict = {'English' : [83, 74, 90], 'Biology' : [86, 89, 92], 'Math' : [74, 84, 91]}
update_dict(original_dict,'Biology')
print(original_dict)

