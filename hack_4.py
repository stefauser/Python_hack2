"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s): 
    result = s 
    change = [] 
 
    for txt in result: 
        if txt !="f" and txt != "n" and txt != "b": 
            change.append(txt) 
            
        result = "".join(change) 
         
    return result 
 
r_1=fn_hack_4("fooziman") 
r_2=fn_hack_4("barziman") 
r_3=fn_hack_4("qux") 
 
print(f"{r_1} / {r_2} {r_3}")
