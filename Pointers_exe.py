num1 = 11
num2 = num1


print("value of num 1 is " ,num1 )
print("location of num 1 is " ,id(num1) )


print("\nvalue of num 2 is " ,num2 )
print("location of num 2 is " ,id(num2) )

num2 = 22

print("\n After the num2 value update")

print("\nvalue of num 2 is " ,num2 )
print("location of num 2 is " ,id(num2) )


dict1 ={
    'value': 11 
}

print("\n\nvalue of dict1 is " ,dict1['value'] )
print("value of dict1 location is  " ,id(dict1['value']) )


dict2 = dict1

print("\nvalue of dict2 is " ,dict2['value'] )
print("value of dict2 location is  " ,id(dict2['value']) )

dict2['value'] = 22

print("\n After the dist2 value update")

print("\nvalue of dict2 is " ,dict2['value'] )
print("value of dict2 location is  " ,id(dict2['value']) )

print("\nvalue of dict1 is " ,dict1['value'] )
print("value of dict1 location is  " ,id(dict1['value']) )


dict3 ={
    'value': 33
}

dict2 = dict3
print("\n After the dist2 value update")

print("\nvalue of dict1 is " ,dict1['value'] )
print("value of dict1 location is  " ,id(dict1['value']) )

print("\nvalue of dict2 is " ,dict2['value'] )
print("value of dict2 location is  " ,id(dict2['value']) )

print("\nvalue of dict3 is " ,dict3['value'] )
print("value of dict3 location is  " ,id(dict3['value']) )