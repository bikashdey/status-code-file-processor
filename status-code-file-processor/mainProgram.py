
# import regular expression
import re

#to read logfile
log_file = open("access_log", 'r')

#to store result
match_success = []
match_bad_request = []
match_unauthorized = []
match_payment_required = []
match_forbidden = []
match_not_found = []

#to search for below status code
status_code =['200','400','401','402','403','404']

#var to match pattern
reg_success = re.compile('HTTP/1.1" '+ status_code[0])
reg_bad_request = re.compile('HTTP/1.1" '+ status_code[1])
reg_unauthorized = re.compile('HTTP/1.1" '+ status_code[2])
reg_payment_required = re.compile('HTTP/1.1" '+ status_code[3])
reg_forbidden = re.compile('HTTP/1.1" '+ status_code[4])
reg_not_found = re.compile('HTTP/1.1" '+ status_code[5])

#to search for line by line 
for line in log_file:
    match_success += (reg_success.findall(line))
    match_bad_request += (reg_bad_request.findall(line))
    match_unauthorized += (reg_unauthorized.findall(line))
    match_payment_required += (reg_payment_required.findall(line))
    match_forbidden += (reg_forbidden.findall(line))
    match_not_found += (reg_not_found.findall(line))

#calculate occurence count 	
success_count = len(match_success)
bad_request = len(match_bad_request)
unauthorized = len(match_unauthorized)
payment_required = len(match_payment_required)
forbidden = len(match_forbidden)
not_found = len(match_not_found)

#printing output on console
print("count of status code 200 -> ", success_count)
print("count of status code 400 -> ", bad_request)
print("count of status code 401 -> ", unauthorized)
print("count of status code 402 -> ", payment_required)
print("count of status code 403 -> ", forbidden)
print("count of status code 404 -> ", not_found)

#closing file read operation
log_file.close();

####################### logic for PDF Report generation ##############################################
file_name = 'StatusCode_Output.pdf'

#import reportlab library 
from reportlab.platypus import Paragraph, SimpleDocTemplate

pdf = SimpleDocTemplate(file_name)

#dataset 
data=[
		['Status code','Response Message','Result Count'],
		[status_code[0],'Success', success_count],
		[status_code[1],'Bad Request', bad_request ],
		[status_code[2],'Unauthorized', unauthorized],
		[status_code[3],'Payment Required', payment_required],
		[status_code[4],'Forbidden', forbidden],
		[status_code[5],'Not Found', not_found],
	 ]
#for tabular data
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()

table =Table(data)

table_style = TableStyle([('GRID',(0,0),(-1,-1),1,colors.black)])
table.setStyle(table_style)

status_code_count = []
styleH = styles['Heading2']

#header
status_code_count.append(Paragraph("Successfully generated Report for Status Code Count",styleH))
status_code_count.append(table)

pdf.build(status_code_count)