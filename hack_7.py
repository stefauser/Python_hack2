"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""

def fn_hack_7(s): 
    result = s 
    new_ls = [] 
     
 
    for i in result: 
        if i == "a": 
            new_ls.append("1")  
 
        elif i == "b": 
            new_ls.append(2) 
 
        elif i == "c": 
            new_ls.append("3") 
 
        elif i == "d": 
            new_ls.append(4)   
 
        elif i =="e": 
            new_ls.append("5")  
 
 
    if not new_ls: 
        return[0] 
     
    result = new_ls 
    return result 
 
 
r_1= fn_hack_7(["a","b","c","d","e"]) 
r_2= fn_hack_7([]) 
 
print(r_1) 
print(r_2)
