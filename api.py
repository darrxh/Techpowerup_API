from requests import get
from bs4 import BeautifulSoup
import json


def database_query(user_input):
    new_request = get("https://www.techpowerup.com/gpu-specs/")
    if not(new_request.ok):
        return



def main():
    pass





if __name__ == '__main__':
    main()


