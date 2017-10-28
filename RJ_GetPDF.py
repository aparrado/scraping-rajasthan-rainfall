#--------------------------------#
#------Akshat Goel---------------# 
#------IDinsight-----------------# 
#------Thursday, March 25th 2017-#
#--------------------------------#

# Importing relevant libraries 
import requests, os, time

# Beginning timer
start_time = time.time()

# Description:
# This function takes as the URL of the .pdfs containing daily Rajasthan rainfall data. 
# It creates a directory to store the files.
# It writes each file to the created directory.
def downloadRain(year, end_year):
	
	## Storing current working directory 
	current_dir = "/Users/Akshat/Desktop/RJ_Rainfall/"

	while year <= end_year: 
		
		## Get PDF and store as a response object
		res = requests.get("http://www.water.rajasthan.gov.in" + 
				   "/content/dam/water/water-resources-department/AnnualRainfall/Print%20" 
				   + str(format(year, '04d')) + ".pdf")
		type(res)  
		res.status_code == requests.codes.ok
	
		## Write PDF to hard drive
		with open( current_dir + str(format(year, '04d')) + ".pdf", 'wb') as f:
			
			## Write command
			f.write(res.content)
    
    		## Update year
		year = year + 1 
		
		
# Testing function 
downloadRain(1957,2015)
print("Done!")


# Timing function
print(time.time() - start_time)


