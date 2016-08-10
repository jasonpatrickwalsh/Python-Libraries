import sys
import csv

##########################################
##             CSV Library              ##
##          Author: Jason Walsh         ##
##                                      ##
##########################################

def file_to_full_list(s0,s1,s2):#where s2 equals what's in s1 grab all - cols seperated with |, rows seperated with newline
	f = open(s0,'rt')
	
	try:
		fileReader = csv.reader(f) #create the reader
		count=0 					#counter
		compareCol=-1 					#row verify query against
		readCol=-1					#row to draw data from
		
		#get the column to test the query against
		count=0
		for row in fileReader:
			for el in row:
				if el == s1:
					compareCol = count;
				count+=1
			break
		f.seek(0) #reset to top
			
		#find the rows that match
		count=0
		rowMatches=""
		for row in fileReader:
			if str(row[compareCol])==s2:
				rowMatches+=str(count)+','
			count+=1
		#print('the following rows match: '+rowMatches)
		f.seek(0) #reset to top
		
		#pull the data from the row where the query matched
		matches = rowMatches.split(',')#split string based on commas
		count=0
		results=""
		for row in fileReader: #for each row
			for elem in matches: #for each element in matches
				if str(count) == str(elem): #if the row# matches an entry in "matches"
					results+=('|'.join(row))+'\n'
			count+=1
		f.seek(0)
		
			
	finally:
		f.close() 
		return results