from subprocess import Popen, PIPE
import requests
import webbrowser
from tkinter import messagebox

def locate_stack_overflow(program_name):
    process = Popen([program_name], stdout=PIPE, stderr=PIPE,shell = True)

    stdout, stderr = process.communicate()
    error_type = ""
    error_details = ""
    error_body = ""
    s = stderr.decode('utf-8') # if any error found stderr contain the traceback in binary format. We converted to utf-8
    hasError = False

    if(s != ""):
        hasError = True
        error_list = s.split("\n") # spliting every line
        error_categories = error_list[-2].split(":") # taking the last error line
        error_type = error_categories[0] # to get the error type like Nameerror, ValueError
        error_details = error_categories[1].strip() # to get description of the error
        error_body = error_list[1].strip()

        print(error_body)
        print(error_type)
        print(error_details)

    else: 
        print("Success")


    if(hasError):
        tagged = "python"
        URL = "https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=activity&body="+ error_body +"&tagged="+ tagged+"&title=" + error_details + "&site=stackoverflow"

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
        messagebox.showinfo("Success", "No error Found in the Program")