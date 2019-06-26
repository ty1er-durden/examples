"""
Write a program to prompt the user for hours and rate per hour using input to
compute gross pay.  DONE

Use 35 hours and a rate of 2.75 per hour to test the program
(the pay should be 96.25). You should use input to read a string and float() to
 convert the string to a number. Do not worry about error checking or bad user
 data.
"""
hours = input("How many hours have you worked? ")

hours = float(hours)

# print(hours)
# print(type(hours))
rate_of_pay = input("How much are you paid per hour? ")
rate_of_pay = float(rate_of_pay)
# # print(rate_of_pay)
weeks_pay = hours * rate_of_pay
print("You were paid", weeks_pay, "pound(s)")
