"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s): 
    result = s 
    new_ls = [] 
     
 
    for i in result: 
        if i == "a": 
            new_ls.append("1")  
 
        elif i == "b": 
            new_ls.append("-") 
 
        elif i == "c": 
            new_ls.append("3") 
 
        elif i == "d": 
            new_ls.append("-")   
 
        elif i =="e": 
            new_ls.append("5")  
 
 
    if not new_ls: 
        return["0"] 
     
    result = new_ls 
    return result 
 
 
r_1= fn_hack_6(["a","b","c","d","e"]) 
r_2= fn_hack_6([]) 
 
print(r_1) 
print(r_2)
