"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    new_list=[]
    contador= 1

    for _ in result:
        nuevo_diccionario={}
        nuevo_diccionario[str(contador)]= str(contador + 1)
        contador += 2

        new_list.append(nuevo_diccionario)

    return new_list
    
r_1= fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]) 

 
print(r_1) 
