import click
import requests


headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://finance.yahoo.com/",
    "Connection": "keep-alive",
}
url = "https://query1.finance.yahoo.com/v8/finance/chart/"
params = {
    "lang": "en-US",
    "region": "US",
    "corsDomain": "finance.yahoo.com"
}
@click.group()
def fancywallet():
    '''
    Fancy commands to manage your assets.
    '''
    pass


@click.group(name='get')
def get_group():
    
    '''
    group of commands to get things.
    '''
    


@click.command(name='price')
@click.argument('stock')
def get_stock_price(stock):
    
    '''
    This is a function to get the stock price.
    '''
    response = requests.get(url=url+stock, params=params, headers=headers)

    result_dict = response.json()

    click.echo(f"The price is: {result_dict['chart']['result'][0]['meta']['regularMarketPrice']}")
get_group.add_command(get_stock_price)
fancywallet.add_command(get_group)



