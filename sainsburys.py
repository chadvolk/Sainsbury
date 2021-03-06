import json , requests , warnings, ssl, csv


api_url_base = 'https://api.stores.sainsburys.co.uk/v1/stores/all/'


#headers = {'Content-Type': 'application/json' , 'username': u ,'password':p }
headers = {'Content-Type': 'application/json'  }
csvfile = 'district_codes.csv'
def get_result_info():
    api_url = format(api_url_base)


    warnings.filterwarnings("ignore")
    response = requests.get(api_url,  verify=False, headers=headers)

    return json.loads(response.content.decode('utf-8'))

def get_district_codes() : 
    result_info = get_result_info()
    #List to store existing district_codes
    district_codes = []
    for node in result_info['results'] :
        #print(node['district_code'])
        district_codes.append(node['district_code'])
        
    #Write the district codes in a csv file 
    with open(csvfile, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for val in district_codes:
            writer.writerow([val])
    #return district_codes
    return district_codes


print ('''SAINSBURY'S API DISTRICT CODES ''')
#Printing the existing district_codes
print(get_district_codes())
