

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
    api = Cpu()
    api.update_url_list()
    api.gpu_fetch()

if __name__ == '__main__':
    main()


