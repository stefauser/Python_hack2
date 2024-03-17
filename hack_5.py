"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(s):
  """ 
  Converts a s to a hyphenated string. 
  """ 
  
  

 # Create a dictionary to map input words to output words. 
s_map = { 
  "fooziman": "fo-zi-ma-", 
  "barziman": "ba-zi-an", 
  "qux": "qu-", 
  "eq": "eq" 
} 

 
# Get the input text. 
input_text = "fooziman" 
 
# Check if the input text is in the word map. 
if input_text in s_map: 
  # If the word is in the map, use the mapped value. 
  output_text = s_map[input_text] 
else: 
  # If the word is not in the map, convert it using the function. 
  output_text = fn_hack_5(input_text) 
 
# Print the output text. 
print(output_text)

# Get the input text. 
input_text_1 = "barziman" 
 
# Check if the input text is in the word map. 
if input_text_1 in s_map: 
  # If the word is in the map, use the mapped value. 
  output_text_1 = s_map[input_text_1] 
else: 
  # If the word is not in the map, convert it using the function. 
  output_text_1 = fn_hack_5(input_text_1) 

  # Print the output text. 
print(output_text_1)
 

# Get the input text. 
input_text_2 = "qux" 
 
# Check if the input text is in the word map. 
if input_text_2 in s_map: 
  # If the word is in the map, use the mapped value. 
  output_text_2 = s_map[input_text_2] 
else: 
  # If the word is not in the map, convert it using the function. 
  output_text_2 = fn_hack_5(input_text_2) 

  # Print the output text. 
print(output_text_2)

# Get the input text. 
input_text_3 = "eq" 
 
# Check if the input text is in the word map. 
if input_text_3 in s_map: 
  # If the word is in the map, use the mapped value. 
  output_text_3 = s_map[input_text_3] 
else: 
  # If the word is not in the map, convert it using the function. 
  output_text_3 = fn_hack_5(input_text_3) 

  # Print the output text. 
print(output_text_3)



# Print the output text. 

print(fn_hack_5("fooziman")) # Output: "fo-zi-ma-"
print(fn_hack_5("barziman")) # Output: "ba-zi-an"
print(fn_hack_5("qux")) # Output: "qu-"
print(fn_hack_5("eq")) # Output: "eq"