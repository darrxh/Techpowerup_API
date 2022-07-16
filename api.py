import requests
from bs4 import BeautifulSoup
import json

class Api():
    def html_query():
        new_request = requests.get("https://www.techpowerup.com/gpu-specs/")
        if not(new_request.ok):
            print ("Error making HTTP request. \n\n")
            return
        sort_database(new_request)

    def sort_database(new_request):
        html_text = BeautifulSoup(new_request.text, "html.parser")
        html_text = html_text.find("table", class_="processors")
        parts_list = list(html_text.find_all("a"))
        for index in range(len(parts_list)):
            parts_list[index] = "Nvidia " + parts_list[index].string
        print (parts_list)

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

def main():
    pass

if __name__ == '__main__':
    html_query()
    #main()



