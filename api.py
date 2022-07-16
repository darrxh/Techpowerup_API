import requests
from bs4 import BeautifulSoup
import json


def html_query():
    new_request = requests.get("https://www.techpowerup.com/gpu-specs/")
    if not(new_request.ok):
        print ("Error making HTTP request. \n\n")
        return
    pull_database(new_request)

def sort_database(new_request):
    html_text = BeautifulSoup(new_request.text, "html.parser")
    html_text = html_text.find("table", class_="processors")
    parts_list = list(html_text.final_all("a"))
    for index in range(len(parts_list)):
        parts_list[index] = parts_list[index].string
        parts_list[index] = "Nvidia" + parts_list[index]
    print (parts_list)

def update_reference():
    pass

def query_user():
    user_input = str(input("Enter GPU model: \n"))
    query_object = {"quicksearch": user_input}
    new_query = requests.post("https://www.techpowerup.com/gpu-specs/", json = query_object)

    print (new_query.text)



def main():
    pass

#Export dict object into json file in subfolder "export"
def json_export(dict_object):
    print ("Creating JSON file.\n\n")
    new_file = open('export/data.json', 'x')
    json_object = json.dumps(dict_object, indent=2)
    new_file.write(json_object)
    new_file.close()
    print ("JSON file created.")

if __name__ == '__main__':
    html_query()
    #main()



