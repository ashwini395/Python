# Selection Control Structures
"""During check-in process in an airport, the luggage weight of each passenger is checked and in case of over-weight,
they are asked to pay for extra luggage.
Below Python program represents the check-in process. Go through it and guess the output.
Assume luggage weight is always positive. """

ticket_status = "Confirmed"
luggage_weight = 32
weight_limit = 30  # Weight limit for the airline
extra_luggage_charge = 0
if ticket_status == "Confirmed":
    if luggage_weight > 0 and (luggage_weight <= weight_limit):
        print("Check-in cleared")
    elif luggage_weight <= (weight_limit + 10):
        extra_luggage_charge = 300 * (luggage_weight - weight_limit)
    else:
        extra_luggage_charge = 500 * (luggage_weight - weight_limit)
    if extra_luggage_charge > 0:
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")

"""The program you have seen uses various decision control statements for implementing the logic. 
Let’s explore it one by one using scenarios related to check-in process.
One of the first steps during check-in process is checking the passport status. 
Consider the below program written for that. """

# The conditional statement used in this program is known as if-else statement.
passenger_name = "Chan"
passport_status = "valid"
if passport_status == "valid":
    print("Airport security cleared")
else:
    print("Invalid passport")

# The next step in check-in process is checking the luggage weight.
"""The conditional statement in this program is known as the else if ladder .
 The conditions are evaluated from top of the ladder downwards.
  As soon as a true condition is encountered, the statement associated with it is executed. 
  The remaining condition checks in the ladder will be skipped."""

luggage_weight = 30
weight_limit = 30  # Weight limit for the airline
extra_luggage_charge = 0
# below condition can also simplified to if 0 < luggage_weight <= weight_limit:
if luggage_weight > 0 and luggage_weight <= weight_limit:
    print("Check-in cleared")
elif luggage_weight <= (weight_limit + 10):
    extra_luggage_charge = 300 * (luggage_weight - weight_limit)
else:
    extra_luggage_charge = 500 * (luggage_weight - weight_limit)
if extra_luggage_charge > 0:
    print("Extra luggage charge is Rs.", extra_luggage_charge)
    print("Please make the payment to clear check-in")

"""Suppose there are 1000 passengers travelling per day and on an average 
850 of them travel in AirIndia, 100 in Emirates and 50 in British Airways.
 Think about the number of comparisons needed in both the codes. 
 Code 1 needs lesser comparisons and hence better execution time as the most probable condition is written as the first
  condition in elif ladder. This practice is known as ordering of conditions based on frequency."""

# This practice is known as ordering of conditions based on frequency

airline = "AirIndia"
if airline == "AirIndia":
    print("Proceed to Air India check-in counter")
elif airline == "Emirates":
    print("Proceed to Emirates check-in counter")
elif airline == "British Airways":
    print("Proceed to British Airways check-in counter")
else:
    print("Invalid airline")

