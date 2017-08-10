#!/usr/bin/python

""" 
    Exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#print(len(enron_data))


for i in enron_data:
 	print enron_data[i]
 	print '\n'

print enron_data.keys()

ctr = 0 
for i in enron_data:
  	if(enron_data[i]['poi']==1):
 		ctr = ctr+1

suspects = [] #Persons of interest
suspects = enron_data.keys();

#Store the names of all Persons of interest in a file
POI_file = open(“POI_list.txt”,”w”) 
for i in range(0,len(suspects)-1):
	print i+1,".",suspects[i]
	POI_file.write(suspects[i])

 POI_file.close()
 