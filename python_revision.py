from functools import reduce

ages = [5,12, 17,18,24,32]
def myFunc(x):
    if x <18: 
        return False
    else:
        return True


adults = list(filter(myFunc, ages))
print(adults)


adults_using_lambda = list(filter(lambda x: x>=18, ages))
print(adults_using_lambda)

numbers = [5,12,17,18,24,32]
even = list(filter(lambda x:  {x%2 == 0}, numbers))
print(even)

odd = list(filter(lambda x: not x%2 == 0, numbers))
print(odd)

print("*"*20)
print(adults)
print([x for x in map(lambda x:{'age':x}, adults)])


print("-"*30)
student_details = ['name:piyush','age:26','gender:male','marital_status:single']
print(student_details)