import requests
from bs4 import BeautifulSoup
import json
import time

class Gpu():

    def __init__(self):
        self.base_url = "https://www.techpowerup.com/gpu-specs/"
        self.parameters = {
        "mfgr" : ["NVIDIA","AMD","INTEL"],
        "lower_year" : 2010,
        "upper_year" : 2023 }
        self.url_list = []

    def update_url_list(self):
        self.url_list.clear()
        for year in range(self.parameters["lower_year"],self.parameters["upper_year"]):
            self.url_list.append(f"{self.base_url}?mfgr={self.parameters['mfgr'][0]}&released={year}&mobile=No")
            self.url_list.append(f"{self.base_url}?mfgr={self.parameters['mfgr'][1]}&released={year}&mobile=No")
            self.url_list.append(f"{self.base_url}?mfgr={self.parameters['mfgr'][2]}&released={year}&mobile=No")
            self.url_list.append(f"{self.base_url}?mfgr={self.parameters['mfgr'][0]}&released={year}&mobile=Yes")
            self.url_list.append(f"{self.base_url}?mfgr={self.parameters['mfgr'][1]}&released={year}&mobile=Yes")
            self.url_list.append(f"{self.base_url}?mfgr={self.parameters['mfgr'][2]}&released={year}&mobile=Yes")

        for i in self.url_list: #testing line
            print (i)
        self.validate_url_list()

    def validate_url_list(self):
        for each_url in self.url_list:
            time.sleep(30)
            if not (requests.get(each_url).ok):
                print (f"Error with URL: {each_url}")
                return False
            else:
                print(f"URL: {each_url} OK")
        return True

    def html_query(self):
        new_request = requests.get(self.base_url)
        print (new_request.ok)
        return new_request.ok

    def gpu_fetch(new_request):
        URL = "https://www.techpowerup.com/gpu-specs/"
        html_query(URL)
        html_text = BeautifulSoup(new_request.text, "html.parser")
        html_text = html_text.find("table", class_="processors")
        parts_list = list(html_text.find_all("a"))
        for index in range(len(parts_list)):
            parts_list[index] = "Nvidia " + parts_list[index].string
        print (parts_list) #testing line


    def update_reference():
        pass

    def query_user():
        user_input = str(input("Enter GPU model: \n"))
        query_object = {"quicksearch": user_input}
        new_query = requests.post("https://www.techpowerup.com/gpu-specs/", json = query_object)

        print (new_query.text)


    #Export dict object into json file in subfolder "export"
    def json_export(dict_object):
        print ("Creating JSON file...\n")
        new_file = open('export/data.json', 'x')
        json_object = json.dumps(dict_object, indent=2)
        new_file.write(json_object)
        new_file.close()
        print ("JSON file created.")

    def help(self):
        command_list = "json_export : export a json file containing gpu and cpu data" \
                       "gpu_list : output list of all GPUs in database" \
                       "cpu_list : output list of all CPUs in database" \
                       "find : returns True of False" \
                       "specs : returns detailed spec dictionary object from specified gpu or cpu (1 argument)" \
                       "list_all : return list of GPUs or CPUs containing string argument given" \
                       "compare : returns performance difference between two GPUs or CPUs (2 arguments)" \
                       ""
        print (command_list)

class Cpu():

    def __init__(self):
        self.base_url = "https://www.techpowerup.com/cpu-specs/"
        self.parameters = {
        "mfgr" : ["AMD","INTEL"],
        "mobile" : ["No","Yes"],
        "lower_year" : 2010,
        "upper_year" : 2023 }
        self.url_list = []

    def cpu_fetch(new_request):
        URL = "https://www.techpowerup.com/cpu-specs/"
        html_query(URL)
        html_text = BeautifulSoup(new_request.text, "html.parser")
        html_text = html_text.find("table", class_="processors")
        parts_list = list(html_text.find_all("a"))
        for index in range(len(parts_list)):
            parts_list[index] = parts_list[index].string
        print (parts_list) #testing line

def main():
    api = Gpu()
    api.update_url_list()

if __name__ == '__main__':
    main()



