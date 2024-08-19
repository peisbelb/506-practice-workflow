# 506-practice-workflow
This assignment is a primer for 504/507 Fall semester classes to practice a basic development workflow. 
# 506 Practice Workflow

## Variables
- **Number Variable**: An integer with the value 42.
- **String Variable**: A string with the value "Hello, World!".
- **List Variable**: A list containing [1, 2, 3, 4, 5].
- **Dictionary Variable**: A dictionary with keys and nested values.

## Function
- **`sample_function(a, b)`**: This function compares two numbers and returns the difference between them.

## Example Output
- Running the function with 10 and 5 returns: `Function Result: 5`.

import pandas as pd
import numpy as np

# Variables
number_var = 42
string_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
dict_var = {
    'key1': 'value1',
    'key2': [1, 2, 3],
    'key3': {'nested_key': 'nested_value'}
}

# Function
def sample_function(a, b):
    if a > b:
        result = a - b
    else:
        result = b - a
    return result

# Print statements
print("Number Variable:", number_var)
print("String Variable:", string_var)
print("List Variable:", list_var)
print("Dictionary Variable:", dict_var)

# Function call and print result
result = sample_function(10, 5)
print("Function Result:", result)

#MY EXAMPLE FOR HOMEWORK STARTS HERE!!!! :)
patient_name = "Peisbel Baret" #string variable 
patient_age = 22 #number variable 
patient_ethnicity = "Hispanic" #string v that will be incorporated into list
Chief_complaint = "Chest pains" #string v that will be incorporated into list
patient_information = [22, "Peisbel Baret", "Hispanic", "chest pains"] #list
#basic dictionary for an admitted patient 
admitted_patient = {
    "name" : "Peisbel Baret",
    "age" : 22,
    "ethnicity" : "Hispanic",
    "Chief complaint" : "chest pains"

}  
#accessing values from dictionary 
print(admitted_patient["name"])
print(admitted_patient["age"])
print(admitted_patient["ethnicity"])
print(admitted_patient["Chief complaint"])

#example of dictionary WITH nested dictionary 
admitted_patient = {
    "name" : "Peisbel Baret",
    "age" : 22,
    "ethnicity" : "Hispanic",
    "chief_complaint" : "chest pains", #literally took me an hour to realize i forgot a comma
   "vitals": {  # Changed from list to dictionary
        "blood_pressure": "120/80",
        "temperature": 97,
        "pulse": 78
    },
    "address" : {  #example of nested
        "street" : "123 Brookshire Lane",
        "city" : "Louisville",
        "state" : "Texas",
        "zipcode" : "19999"}

    }
#we are now going to try to evaluate the patient (my!) temperature :)
def check_temperature(age,temperature):
    #we have to define normal temperature range
    normal_temperature = 98.7

#Here we are going to try to determine if my temperature is normal or elevated
if temperature < normal_temperature:
        return "Below normal"
elif temperature == normal_temperature:
        return "Normal"
else:
        return "Elevated"
#why isn't this working :(



def check_temperature(temperature):
    normal_temperature = 98.6
    
    if temperature < normal_temperature:
        return "Below normal"
    elif temperature == normal_temperature:
        return "Normal"
    else:
        return "Elevated" 
    #why did this work and the other didn't?????? im guessing the indentation is incorrect? ugh 
    #oh well time to see if this works
    
#patient details
print("Name:", admitted_patient["name"])
print("Age:", admitted_patient["age"])

print("Ethnicity:", admitted_patient["ethnicity"])
print("Chief Complaint:", admitted_patient["chief_complaint"])

#patient's address...not really
print("Street:", admitted_patient["address"]["street"])
print("City:", admitted_patient["address"]["city"])
print("State:", admitted_patient["address"]["state"])
print("Zipcode:", admitted_patient["address"]["zipcode"])

#did someone request vital signs???
print("blood_pressure:", admitted_patient["vitals"]["blood_pressure"])
print("Temperature:", admitted_patient["vitals"]["temperature"])
print("Pulse:", admitted_patient["vitals"]["pulse"])

temperatue = admitted_patient["vitals"]["temperature"]
result = check_temperature(temperature)

print(f"Temperature: {temperature}°F")
print(f"Temperature Analysis: {result}")
#the function did not work. :( we will never know if I had a fever or not. 