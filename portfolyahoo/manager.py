import requests

class Manager:
    def __init__(self, crumb: str, userId: str, cookie: str):
        self.crumb = crumb
        self.userId = userId
        self.cookie = cookie
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            "Cookie": cookie
        }

    def create_portfolio_from_file(self, filename: str, name: str, currency: str): 
        portfolio = str()
        with open(filename, "r") as file:
            portfolio = file.read()
        url = f'https://query1.finance.yahoo.com/v1/finance/w/importPortfolio?crumb={self.crumb}'
        data = { "portfolio": portfolio }
        creationResult = requests.post(url, headers = self.headers, json = data)
        portfolioId = creationResult.json()['pfId']
        self.update_portfolio_settings(portfolioId, name, currency)
        return portfolioId

    def update_portfolio_settings(self, id: str, name: str, currency: str):
        url = f'https://query1.finance.yahoo.com/v6/finance/portfolio/update?crumb={self.crumb}&action=update&userId={self.userId}&pfId={id}'
        data = {"parameters":{"userId":self.userId,"userIdType":"guid","pfId":id,"fullResponse":True},"operations":[{"operation":"portfolio_update", "pfName": name,"baseCurrency":currency,"cashCurrency":currency}]}
        return requests.put(url, headers = self.headers, json = data)

    def delete_portfolio(self, id: str):
        url = f'https://query1.finance.yahoo.com/v6/finance/portfolio?crumb={self.crumb}&userId={self.userId}&pfId=%s' % id
        return requests.delete(url, headers = self.headers)

    def get_portfolios(self):
        url = f'https://query1.finance.yahoo.com/v7/finance/desktop/portfolio?formatted=true&crumb={self.crumb}&lang=en-US&region=US&userId={self.userId}&corsDomain=finance.yahoo.com'
        return requests.get(url, headers = self.headers).json()['finance']['result'][0]['portfolios']