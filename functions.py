# conversion calculator
#by:

# user input regarding the length to convert
# get the unit from the user
#convert unit to the correct unit
#output the answer to the user

user_number = float(input ("What number would you like too convert? "))
user_unit = input ("What unit is your number? ")

#convert inches to mm --> in X 25.4
#to convert mm to in --> mm / 25.4

#user gives in unit
if (user_unit =='in'):
    conv_num = user_number * 25.4
    conv_unit = 'mm'
elif (user_unit == 'mm'):
# user gies mm unit
    conv_num = user_number / 25.4
    conv_unit = 'in'
else:
    print('That is not a valid unit')
    
print (conv_num, conv_unit)
