from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as urllib2
import csv
import requests



# Scraper Mode 1 ######################
def WebScraperbank1(bank_url, bank_table_id) :
    request = urllib2.Request(bank_url)
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, 'html.parser')
    
    # bank_table_id = 'content'
    bank_table = []
    bank_table = soup.find_all('div', attrs={'class': bank_table_id})
    
    bank_TD = pd.read_html(str(bank_table))
    bank_df = pd.DataFrame(bank_TD)

    return bank_df

# Scraper Mode 2 ########################
def WebScraperbank2(bank_url, bank_table_id) :
    # bank_table_id = 'table'
    responce = requests.get(bank_url)
    soup = BeautifulSoup(responce.text, 'html.parser')
    bank_table = soup.find('div', attrs={'id': bank_table_id})
    bank_df = pd.read_html(str(bank_table))

    return bank_df


###################################

west_url = 'https://www.westpac.com.au/business-banking/savings-accounts/term-deposits/business-term-deposit-rates/'
anz_url = 'https://www.anz.com.au/personal/bank-accounts/your-account/rates-fees-terms/#td'
com_url = 'https://www.commbank.com.au/banking/term-deposits/rates-and-fees.html'



west_df = WebScraperbank1(west_url, 'tabcordion-body')
anz_df = WebScraperbank2(anz_url, 'main-container')
# com_df = WebScraperbank2(com_url, 'table')

print(anz_df)


west_df.to_csv(r'C:\Dev\Github\Lkwd_WebScraper\Likwidity\Westpac_TD.csv', index = False)
# anz_df.to_csv(r'C:\Dev\Github\Lkwd_WebScraper\Likwidity\Anz_TD.csv', index = False)
# com_df.to_csv(r'C:\Dev\Github\Lkwd_WebScraper\Likwidity\Combank_TD.csv', index = False)

####################### Old COde
# request = urllib2.Request(west_url)
# page = urllib2.urlopen(request)
# soup = BeautifulSoup(page, 'html.parser')

# west_table_id = 'content'
# west_table = []
# west_table = soup.find_all('div', attrs={'class': 'tabcordion-body'})

# west_TD = pd.read_html(str(west_table))
# west_df = pd.DataFrame(west_TD)






# with pd.ExcelWriter('Westpac_TD.xlsx') as writer:
#     west_df.to_excel(writer)
# west_xl = pd.ExcelWriter('Westpac_TD.xlsx')
# west_df.to_excel(west_xl, sheet_name = 'Sheet1', index = False)
# west_xl.save()

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



# pd.set_option('display.max_columns',100)
# pd.set_option('display.max_rows',500)
# pd.set_option('display.min_rows',500)
# pd.set_option('display.max_colwidth',150)
# pd.set_option('display.width',120)
# pd.set_option('expand_frame_repr',True)





# ##############################################################################

# anz_url = 'https://www.anz.com.au/personal/bank-accounts/your-account/rates-fees-terms/#td'
# anz_table_id = 'main-container'

# responce = requests.get(anz_url)
# soup = BeautifulSoup(responce.text, 'html.parser')

# anz_table = soup.find('div', attrs={'id': anz_table_id})
# anz_df = pd.read_html(str(anz_table))

# ##############################################################################

# com_url = 'https://www.commbank.com.au/banking/term-deposits/rates-and-fees.html'
# com_table_id = 'table'

# responce = requests.get(com_url)
# soup = BeautifulSoup(responce.text, 'html.parser')

# com_table = soup.find('div', attrs={'class': com_table_id})
# com_df = pd.read_html(str(com_table))

# ##############################################################################

