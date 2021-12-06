
# assignment3 by Mohammed Farhan Alloush 
#           Samir Elmassri

import csv
from datetime import date

today = date.today()

class Physician:

    __slots__ = ["__id", "__name"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    
    def __repr__(self):
        return "%s, %s" % (self.__id, self.__name)
    
    def __str__(self):
        return "%s, %s" % (self.__id, self.__name)

    #   Accessor

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    #  Mutator

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name
 

class Patient:

    __slots__ = ["__emr_id", "__name", "__gender", "__phone_number"]

    def __init__(self, emr_id, name, gender, phone_number):
        self.__emr_id = emr_id
        self.__name = name
        self.__gender = gender
        self.__phone_number = phone_number

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.__emr_id, self.__name, self.__gender, self.__phone_number)
    
    #   Accessor

    def get_emr_id(self):
        return self.__emr_id

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender
    
    def get_phone_number(self):
        return self.__phone_number

    #  Mutator

    def set_emr_id(self, emr_id):
        self.__emr_id = emr_id

    def set_name(self, name):
        self.__name = name
    
    def set_gender(self, gender):
        self.__gender = gender
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
 
class Encounter:

    __slots__ = ["physician", "patient", "date", "disease", "medication"]

    def __init__(self, physician, patient, date, disease, medication):
        self.physician = physician
        self.patient = patient
        self.date = date
        self.disease = disease
        self.medication = medication

#   Reading patients
def read_patients():
    file = open('patients.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    
    return rows

#   Reading physicians
def read_physicians():
    file = open('physicians.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    return rows

def print_en(en):   #   function to print all encounters

    print("physician:")
    print("id:", en.physician.get_id())
    print("name:", en.physician.get_name(), "\n")

    print("patient:")
    print("emr_id:", en.patient.get_emr_id())
    print("name:", en.patient.get_name())
    print("gender:", en.patient.get_gender())
    print("phone_number:", en.patient.get_phone_number(), "\n")

    print(en.date)
    print(en.disease)
    print(en.medication, "\n")


 
def main():
    #  Creating 10 patient objects 
    p = []
    patitent = read_patients()
    p.append(Patient(patitent[0][0], patitent[0][1], patitent[0][2], patitent[0][3]))
    p.append(Patient(patitent[1][0], patitent[1][1], patitent[1][2], patitent[1][3]))
    p.append(Patient(patitent[2][0], patitent[2][1], patitent[2][2], patitent[2][3]))
    p.append(Patient(patitent[3][0], patitent[3][1], patitent[3][2], patitent[3][3]))
    p.append(Patient(patitent[4][0], patitent[4][1], patitent[4][2], patitent[4][3]))
    p.append(Patient(patitent[5][0], patitent[5][1], patitent[5][2], patitent[5][3]))
    p.append(Patient(patitent[6][0], patitent[6][1], patitent[6][2], patitent[6][3]))
    p.append(Patient(patitent[7][0], patitent[7][1], patitent[7][2], patitent[7][3]))
    p.append(Patient(patitent[8][0], patitent[8][1], patitent[8][2], patitent[8][3]))
    p.append(Patient(patitent[9][0], patitent[9][1], patitent[9][2], patitent[9][3]))
    
    #   Creating 3 physicians objects
    ph = []
    physician = read_physicians()
    ph.append(Physician(physician[0][0], physician[0][1]))
    ph.append(Physician(physician[1][0], physician[1][1]))
    ph.append(Physician(physician[2][0], physician[2][1]))

    #   Creating 5 encounter objects
    en = []
    date = today.strftime("%d/%m/%Y")
    en.append(Encounter(ph[0], p[0], date, "Flu", "antibiotics"))
    en.append(Encounter(ph[1], p[3], date, "Headache", "panadol"))
    en.append(Encounter(ph[2], p[5], date, "Headache", "panadol"))
    en.append(Encounter(ph[1], p[8], date, "Flu", "antibiotics"))
    en.append(Encounter(ph[0], p[2], date, "Headache", "panadol"))


    #   Printing all patients
    print("printing all patients\n")
    for i in range(len(p)):
        print(p[i])
    print("\n")

    #   Printing all physicians 
    print("printing all physicians\n")
    for i in range(len(ph)):
        print(ph[i])
    print("\n")

    #   Priting all encounter
    print("printing all encounter")
    for i in range(len(en)):
        print_en(en[i])

    #	Creating an encounter.csv file to store all encounters
    with open('encounter.csv', 'w', encoding='UTF8') as f:
        header = ['physician_id', 'physician_name', 'patient_emr_id', 'patient_name','patient_gender','patient_phone_number', 'date',  'disease', 'medication']
        writer = csv.writer(f)
        writer.writerow(header)
        data = []
        for i in range(len(en)):
           list = [en[i].physician.get_id(), en[i].physician.get_name(), en[i].patient.get_emr_id(), en[i].patient.get_name(), en[i].patient.get_gender(), en[i].patient.get_phone_number(), en[i].date, en[i].disease, en[i].medication]
           data.append(list)
        
        writer.writerows(data)







main()