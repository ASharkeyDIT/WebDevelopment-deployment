
from quandl import qapi

ticker = input("Enter stock ticker")
date = input("Enter date in year|month|day")

call = qapi(ticker.upper(),date)
call.query()
print(call)





























'''
json_repsonse = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?date=20170201&ticker=FSLR&api_key=-wWq3h4QHgNyRYNZsVVx')

x = json_repsonse.json()

columns_list = []
data_list = []
data_dict = {}

for el in x['datatable']['data']:
    for value in el:
        data_list.append(value)

for el in x['datatable']['columns']:
    for key,value in el.items():
        if key == 'name':
            columns_list.append(value)


for element in zip(data_list,columns_list):
    data_dict[element[1]]=element[0]

print(data_dict)

'''
