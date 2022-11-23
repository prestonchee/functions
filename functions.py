# Conversion Calculator
# By: Scott Hadzik

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the answer to the user
vaild_data = True

def user_parser(user_input):
# Do something
# Separate the number from unit
    global valid_data
    valid_data = True
    #Todo address input from user without space
    values = user_input.rsplit(" ")
    number = values[0]

    if number.isdigit():
        number = float(number)
    else:
        print("That is not a valid number ")

    unit = values[1]
    if unit != 'in' and unit != 'mm' and unit != 'ft':
        print("That is not a valid unit")
        valid_data = False

    return number, unit
def print_results(user_input, user_number, conv_number, conv_unit):
    result = ("{:.2f} {} is equal to {:.2f} {}")
    print (result user_number, user_unit, conv_number,conv_unit)

while True: # continue progra until user exits
    while True: #check for valid data
        user_input = input("number and unit to convert ")
        user_number, user_unit = user_parser(user_input)
    
     #check for invaild messages

        if valid_data:
            break

    #perform calculations
    if(user_unit == 'in'):
       # perform in to mm
        conv_number = user_number * 25.4
        conv_unit = 'mm'
        
    elif(user_unit == 'mm'):
       # perform mm to in
        conv_number = user_number / 25.4
        conv_unit = 'in'
    elif(user_unit == 'ft'):
        #perform ft to in
        conv_number = user_number * 12
        
        conv_unit = 'in'
    print_results (user_number, user_unit, conv_number, conv_unit)
    #create a function that prints out the answer formatted to 2 decimal places
    #Give the original value and unit and the conv number and unit

    # 12.00 ft is equal to 144.00 in

        






# while True:
# user_number = input("What number to convert? ")
# if user_number.isdigit():
# user_number = float(user_number)
# break
# else:
# print ('please use a number')
# user_unit = input("What unit is your number?")


# print(conv_number, conv_unit)
