import click
import requests

@click.group()
def fancywallet():
    '''
    Fancy commands to manage your assets.
    '''
    pass


@click.group(name='get')
def get_group():
    '''
    This group is for making requests.
    '''
    pass


@click.command(name='price')
def get_stock_price():
    '''
    This is a function to get the stock price.
    '''