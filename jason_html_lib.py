import sys

##########################################
##             HTML Library             ##
##          Author: Jason Walsh         ##
##                                      ##
##########################################

def get_html_header():
	head=''
	head+='<!DOCTYPE html><html><head>\n'
	head+= '</head>\n<body>\n'
	return head
	
def get_javascript_sorttable():
	return '<script src="sorttable.js"></script>\n'

def get_css_style():
	cssStyle='<style>body{background-color: #F2F2F2;}table, td, th {border: 1px solid black;border-collapse: collapse;background-color: #D9D9D9;}'
	cssStyle+= 'td.offline{background-color: rgb(130, 206, 184);} th{background-color: #C9C9C9;border: 1px solid black;border-collapse: collapse;}'
	cssStyle+= '#results{border: solid;text-align: center;} h1{text-align: center;} p{text-align: center; font-weight: 900;}'
	return cssStyle

def get_table_header(s0): #s0 is a header list
	tabHead='<table class="sortable" style="width:100%"><tr>'
	
	list = []
	list = s0.split(',')
	
	for el in list:
		tabHead+='<th>'+str(el)+'</th>'
	tabHead+='</tr>'
	
	return tabHead
	
def get_table_end():
	return '</table>'
	
def get_table_row(s0): #s0 is a header list
	tabRow='<tr>'
	
	list = []
	list = s0.split(',')
	
	for el in list:
		tabRow+='<th>'+str(el)+'</th>'
	tabRow+='</tr>'
	
	return tabRow

