dict= {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
new_dict={}
val = dict.values()
val=set(val)
val = list(val)
Final={}

print(dict)

key = list(dict.keys())

for i in range (len(val)):
    for j in range (len(key)):
         if val[i]==list(dict.values())[j]:             
              new=[key[j]]
              if val[i] in Final:
                Final[val[i]].append(key[j])
              else:
                Final[val[i]]=new
print(Final)
   
