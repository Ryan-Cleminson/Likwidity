from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as urllib2
import csv

west_url = 'https://www.westpac.com.au/personal-banking/bank-accounts/term-deposit/rates/'
west_table_id = 'tabcordion-body'

request = urllib2.Request(west_url)
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

west_table = soup.find_all('div', attrs={'class': west_table_id})
west_TD = pd.read_html(str(west_table))
west_df = pd.DataFrame(west_TD)

west_xl = pd.ExcelWriter('Westpac_TD.xlsx')
west_df.to_excel(west_xl, sheet_name = 'Sheet1', index = False)
west_xl.save()

# west_table = west_table[0]

# for row in west_table.find_all('tr'):
#     for cell in row.find_all('td'):
#         print(cell.text)

# with open ('West_td.txt', 'w') as r:
#     for row in west_table.find_all('tr'):
#         for cell in row.find_all('td'):
#             r.write(cell.text)

# west_td = pd.read_html(str(west_table))

# responce = requests.get(west_url)
# soup = BeautifulSoup(responce.text, 'html.parser')

# westpac_table = soup.find('div', attrs={'id': west_table_id})

# west_df.to_csv(r'C:\GitHub\Python-Library\Projects\Bank_Web_Scrape\Westpac_TD.csv', index = False)

pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',500)
pd.set_option('display.min_rows',500)
pd.set_option('display.max_colwidth',150)
pd.set_option('display.width',120)
pd.set_option('expand_frame_repr',True)

##############################################################################

anz_url = 'https://www.anz.com.au/personal/bank-accounts/your-account/rates-fees-terms/#td'
anz_table_id = 'table-scrollable'

request = urllib2.Request(anz_url)
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

anz_table = soup.find_all('div', attrs={'class': anz_table_id})
anz_TD = pd.read_html(str(anz_table))
anz_df = pd.DataFrame(anz_TD)

anz_xl = pd.ExcelWriter('anz_TD.xlsx')
anz_df.to_excel(anz_xl, sheet_name = 'Sheet1', index = False)
anz_xl.save()

##############################################################################

com_url = 'https://www.commbank.com.au/banking/term-deposits.html'
com_table_id = 'table'

request = urllib2.Request(com_url)
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

com_table = soup.find('div', attrs={'class': com_table_id})
com_TD = pd.read_html(str(com_table))
com_df = pd.DataFrame(com_TD)

com_xl = pd.ExcelWriter('Westpac_TD.xlsx')
com_df.to_excel(com_xl, sheet_name = 'Sheet1', index = False)
com_xl.save()

##############################################################################

nab_url = 'https://www.nab.com.au/personal/interest-rates-fees-and-charges/indicator-rates-selected-term-deposit-products'
nab_table_id = 'nabrwd-table section'

request = urllib2.Request(nab_url)
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

nab_table = soup.find_all('div', attrs={'class': nab_table_id})
nab_TD = pd.read_html(str(nab_table))
nab_df = pd.DataFrame(nab_TD)

nab_xl = pd.ExcelWriter('Westpac_TD.xlsx')
nab_df.to_excel(nab_xl, sheet_name = 'Sheet1', index = False)
nab_xl.save()