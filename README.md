# Portfolyahoo
Portfolyahoo is an unofficial API to manage your portfolios on Yahoo Finance.

It currently supports:
- Creating a portfolio from a CSV file
- Deleting a portfolio
- Browsing your portfolios

## Installation
```properties
pip install -r requirements.txt
pip install -e .
```

## Usage
```python
import portfolyahoo

manager = portfolyahoo.Manager(
		crumb='?',
		userId='?',
		cookie='?'
)

# Create a portfolio from a CSV file
myPortfolio = manager.create_portfolio('portfolio.csv', 'My Portfolio', 'USD')

# Delete a portfolio by ID
manager.delete_portfolio(myPortfolio)

# List portfolios IDs
portfolios = manager.get_portfolios()
for portfolio in portfolios:
    print("Portfolio: %s" % portfolio['pfId'])
```