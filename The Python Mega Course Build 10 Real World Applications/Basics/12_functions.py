def calculate_age(year):
    age = 2018 - year
    return age

print(calculate_age(1990))

#diff between return and print
#while using pring we can reuse the output in the code. It returns the type of the object depends on the output
#whereas using the print is allowed to reuse the output in the code. It returns the None type.



#Functions with more than one parameter
def km_to_m(km, coefficient = 0.6214):
    return km * coefficient

print(km_to_m(10))