"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
 output = {}
 for key, value in s.items():
  if "foo" in key:
   output[key.capitalize()] = value.capitalize().replace("k","")
 return output
   
     
text = {"foo": "fookziman", "bar": "barziman"}
print(fn_hack_9(text)) # Output: {"Foo": "Fooziman"}  
 


 
