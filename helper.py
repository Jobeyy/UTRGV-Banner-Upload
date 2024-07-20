import csv

def check_zip_code(dataset):
    with open("zcodes.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        list_of_valid_zips = list(reader)
    for row in dataset:
        if(row[7] == 'ZIPCODE'):
            continue
        if(row[7] not in list_of_valid_zips or len(row[0]) == 0):
            row[7] = "78542"
    return dataset

def remove_2nd_address(dataset):
    default_address = "W Schunior St"
    for row in dataset:
        if(row[2] == 'The University Of Texas Rio'):
            row[2] = default_address
            row[3] = ""
    return dataset    
    

def check_state(dataset):
    default_state = 'TX'
    default_city = "Edinburg"
    for row in dataset:
        if (row[6] == 'STATE'):
            continue
        if(row[6] != default_state):
            row[6] = default_state
            row[5] = default_city
    return dataset

def check_phone_number(dataset):
    default_phone = '9565555555'
    for row in dataset:
        if(row[8]== 'CELLPHONE'):
            continue
        if(len(row[8]) != 10 or len(row[9]) != 10):
            row[8] = default_phone
            row[9] = default_phone
    return dataset