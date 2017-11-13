import requests
import json

''' x = json_repsonse.json() '''

class qapi():

    preamble = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?'
    key = '-wWq3h4QHgNyRYNZsVVx'
    url = ''
    ticker = ''
    date = ''
    data_dict = {}

    def __init__(self,ticker,date):
        self.ticker = ticker
        self.date = date
        self.consurl()


    def consurl(self):
        self.url = self.preamble + 'date=' + self.date + '&ticker=' + self.ticker + '&api_key=' + self.key
        return()

    def query(self):

        json_response = requests.get(self.url)
        x = json_response.json()

        columns_list = []
        data_list = []

        for el in x['datatable']['data']:
            for value in el:
                data_list.append(value)

        for el in x['datatable']['columns']:
            for key,value in el.items():
                if key == 'name':
                    columns_list.append(value)

        for element in zip(data_list,columns_list):
            self.data_dict[element[1]]=element[0]


    def __str__(self):
        return(str(self.data_dict))
