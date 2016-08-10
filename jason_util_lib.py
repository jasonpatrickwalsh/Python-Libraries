import sys

##########################################
##             Util Library             ##
##          Author: Jason Walsh         ##
##                                      ##
##########################################

def is_empty(s0):
	empty = True
	if s0 != "" and s0 != " ":
		empty = False
	return empty

def list_to_matches(s0,s1): #return matches
	matchedRecords=""
	output=[]
	
	for elem0 in s0:
		if is_empty(str(elem0)) == False:
			for elem1 in s1:
				if is_empty(str(elem1)) == False:
					taken=False
					if str(elem0) == str(elem1):#if they match
						temp1 = matchedRecords.split(',')
						for elem2 in temp1:#for each spoken-for record
							if elem2 == str(elem1):
								taken=True
						if taken != True:#if it's not taken
							output.append(str(elem1))#add it to the output
							matchedrecords+=str(elem1)+","
	return output
	
def list_to_unique(s0,s1): #list, LANDesk,landeskname,landeskoption
	matchedRecords=""
	output=[]
	
	for elem0 in s0:
		if is_empty(str(elem0)) == False:
			matchedNone=True;
			for elem1 in s1:
				if is_empty(str(elem1)) == False:
					taken=False
					if str(elem0) == str(elem1):#if they match
						matchedNone=False
						temp1 = matchedRecords.split(',')
						for elem2 in temp1:#for each spoken-for record
							if elem2 == str(elem1):
								taken=True
						if taken == True:#if it's taken
							output.append(str(elem1))#add it to the output
							matchedrecords+=str(elem1)+","
		if matchedNone:
			output.append(str(elem1))#add it to the output
			
	return output
	
def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def remove_bad_chars(s0,s1):#search s0 for and remove characters found in s1
	stringbuild=''
	badChars = s1
	
	for elem in s0:
		flag = True
		for elem1 in badChars:
			if str(elem) == str(elem1):
				flag = False
		if flag==True:
			stringbuild+= str(elem)
	
	return stringbuild
	
def write_to_file(s0,s1): # filename, content
	with open(s0,'w') as the_file:
		the_file.write(s1)
	the_file.close;