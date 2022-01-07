from subprocess import Popen, PIPE
import requests
import webbrowser

process = Popen(['program.py'], stdout=PIPE, stderr=PIPE,shell = True)

stdout, stderr = process.communicate()
error_type = ""
error_details = ""
s = stderr.decode('utf-8') # if any error found stderr contain the traceback in binary format. We converted to utf-8
hasError = False

if(s != ""):
    hasError = True
    error_list = s.split("\n") # spliting every line
    error_categories = error_list[-2].split(":") # taking the last error line
    error_type = error_categories[0] # to get the error type like Nameerror, ValueError
    error_details = error_categories[1].strip() # to get description of the error
    print(error_type)
    print(error_details)

else: 
    print("Success")


if(hasError):
    tagged = "python"
    URL = "https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=activity&accepted=True&tagged="+ tagged+"&title=" + error_details + "&site=stackoverflow"
    location = "delhi technological university"
    r = requests.get(url = URL)
    data = r.json()
    data_length = len(data['items'])
    if(data_length > 3):
        for i in range(3):
            url = data['items'][i]['link']
            webbrowser.open_new_tab(url)
    else:
        for i in range(data_length):
            url = data['items'][i]['link']
            webbrowser.open_new_tab(url)



else:
    print([])