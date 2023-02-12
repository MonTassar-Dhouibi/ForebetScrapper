import requests, csv, os ,sys
from bs4 import BeautifulSoup
import urllib3.request
import json ,pdfkit

def scrap(write_to_csv = True,filename = 'prdect'):

    games = []
##    url = 'https://www.forebet.com/en/football-predictions/double-chance-predictions/2023-02-12'
##    response = requests.get(url).text
##    #http = urllib3.PoolManager()
##    #response = http.request("GET", url).data.decode("utf-8")
##
##    #print(response.data.decode("utf-8"))
    with open('p.html','r',encoding="utf8") as f :
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('div', {'class': 'schema dbc'})
    tr_0 = table.findAll('div',{'class': 'rcnt tr_0'})
    tr_1 = table.findAll('div',{'class': 'rcnt tr_1'})

    lines = tr_0 + tr_1
    print('tr0 len ',len(tr_0),'tr1 len ',len(tr_1),'lines len ',len(lines))
    
    for line in lines:
        game_notplayed = True if  line.findAll('div', {'class': 'predict'}) else False
        if(game_notplayed):       
            liga = line.find('div', {'class': 'stcn'}).find('span', {'class': 'shortTag'}).text
            homeTeam = line.find('div', {'class': 'tnms'}).find('span', {'class': 'homeTeam'}).text
            awayTeam = line.find('div', {'class': 'tnms'}).find('span', {'class': 'awayTeam'}).text
            date = line.find('div', {'class': 'tnms'}).find('time').span.text
            #probUnder = int(line.find('div', {'class': 'fprc'}).findAll('span')[0].text)
            #probOver = int(line.find('div', {'class': 'fprc'}).findAll('span')[1].text)
            #predicted_result = line.find('span', {'class': 'forepr'}).span.text
            odd_str = line.find('div', {'class': 'bigOnly prmod'}).span.text
            predect = line.find('div', {'class': 'predict'}).find('span', {'class': 'forepr'}).span.text
            

            game = {'liga': liga, 'homeTeam': homeTeam, 'awayTeam': awayTeam, 'date': date,'predection' : predect}
            games.append(game)

    fields = ['liga', 'homeTeam', 'awayTeam', 'date', 'predection']
    print(games)
    
    if(write_to_csv):
       with open(filename+'.csv', 'w') as csvfile:
        # creating a csv dict writer object
        #csv.field_size_limit(1000)
        writer = csv.DictWriter(csvfile, fieldnames = fields)#,delimiter = '\t'
         
        # writing headers (field names)
        writer.writeheader()
         
        # writing data rows
        writer.writerows(games)
    
    

##def read_from_csv(filename):
##    with open('{}.csv'.format(filename), 'w') as csvfile:
##    # creating a csv writer object
##        csvwriter = csv.writer(csvfile)
##     
##    # writing the fields
##        csvwriter.writerow(fields)
##     
##    # writing the data rows
##        csvwriter.writerows(rows)
##        for row in reader:
##            games.append(row)
##    return games
def dicToJsonTpPdf(data):
    with open("mydata.json", "w") as final:
       json.dump(data, final)
       pdfkit.from_file('mydata.json', 'mydata.pdf')


        

def main():
    scrap(write_to_csv = True, filename = 'prdect')

if __name__ == '__main__':
    main()
