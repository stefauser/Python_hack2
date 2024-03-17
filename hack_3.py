"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s): 
    result = s 
    dict = { 
 
    "a" : "@", 
    "e" : "3", 
    "i" : "¡", 
    "o" : "0", 
    "u" : "v", 
    "f" : "F", 
    "n" : "N", 
    "q" : "Q", 
    "x" : "X", 
    "b" : "B", 
    "z" : "z", 
    "m" : "m", 
    "r" : "r", 
    "3" : "3" 
 
    } 
 
    change = [] 
 
    for txt in result:#"fooziman" 
     change.append(dict.get(txt)) 
 
    
 
    result = "".join(change) 
 
    
 
    return result 
 
 
 
 
 
 
 
 
r_1=fn_hack_3("fooziman") 
r_2=fn_hack_3("barziman") 
r_3=fn_hack_3("3q") 
r_4=fn_hack_3("qu") 
r_5=fn_hack_3("qux") 
 
 
print(f"{r_1} / {r_2} {r_3} {r_4} {r_5} ")
