##########################################
##       Jason's Python Library         ##
##        Author: Jason Walsh           ##
##                                      ##
##########################################

_______________READ ME___________________

JASON_XML_LIB.PY
	
	*load_xml(s0):
		-Loads an XML file using minidom and returns the object

	*xml_nodelist_pull_tag(s0,s1):#pull tagged element from nodelist	
		-Given a nodelist(s0), it will return all the elements that match the tag(s1) you give.
		-If multiple entries are found they are joined into a single string with ',' delimiter.

JASON_UTIL_LIB.PY

	*is_empty(s0)
		-returns a true if the passed s0 is empty. Otherwise it returns False
	
	*list_to_matches(s0,s1)
		-returns a list of items that appear in both lists. 
		-prevents one entry in s1 from pairing with multiple matches in s0.
		-In other words, it finds unique matches
		
	*list_to_unique(s0,s1)
		-mimics the behavior of list_to_matches, however, it returns the items with no suitable match
	
	*similar(a,b)
		-returns a % similar of a and b. Recommended similarity to heck for is > 0.8
		
	*remove_bad_chars(s0,s1)
		-returns a sanitized s0 after it's had any characters found in s1 removed
	
	*write_to_file(s0,s1)
		-writes file named s0 with content of s1
	
JASON_HTML_LIB.PY
	
	*get_html_header()
		-returns a standard HTML header to start a HTML (or writestring) with.
		
	*get_javascript_sorttable():
		-returns a script line to link the sort-table javascript library
		
	*get_css_style():
		-returns a compiled CSS inline style to serve as a good base for sort-table formatting
		
	*get_table_header(s0):
		-returns a formatted table header using a passed list of column titles (s0)
	
	*get_table_end():
		-returns a closing table tag for quick table formatting
		
	*get_table_row(s0):
		-returns a formatted row using a passed list of entries (s0)
	
JASON_CSV_LIB.PY
	*file_to_full_list(s0,s1,s2)
		-opens a csv file (s0), and grabs every row where column s1 matches s2.
		-example: (example.csv,"Name","Walsh, Jason")
		-this would return every row where my name is in the name field.
-columns are seperated with a pipe (|) and rows are seperated with a newline character (\n)
