from requests import get
from bs4 import BeautifulSoup
import json


def html_query(input_dict):
    new_request = get("https://www.techpowerup.com/gpu-specs/")
    if not(new_request.ok):
        print ("Error making HTTP request. \n\n")
        return

def query_user():
    user_input = input("")



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
    main()


