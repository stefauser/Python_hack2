"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

def fn_hack_2(s): 
    result = s 
    vowels = ["a","e","i","o","u"] 
    _str = [] 
     
    for txt in result: 
        if txt not in vowels: 
          _str.append(txt)   
           
    result = "".join(_str) 
    return result    
 
r_1=fn_hack_2("fooziman") 
r_2=fn_hack_2("barziman") 
r_3=fn_hack_2("qux") 
 
print(f"{r_1} / {r_2} {r_3}")
