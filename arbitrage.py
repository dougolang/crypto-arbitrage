
# Detect arbitrage opportunities between Kucoin and Coinbase.
# You must install coingecko wrappepr for python. pip install pycoingecko

import requests

#list of top 10 cryptos
top10 = [
    "BTC",
    "ETH",
    "ALGO",
    "DOGE",
    "MATIC",
    "ADA",
    "SOL",
    "DOT",
    "CRO",
    "AVAX"
]

#Gets the price for a given market for different cryptos
def getPrice(crypto, market):
    url = f"https://api.coingecko.com/api/v3/exchanges/{market}/tickers"  #url to coingecko's exchanges API, formated to accept market as a input
    results = requests.get(url).json() #creates dict of API crypto info
    results = results["tickers"] #get results for tickers
    for c in results: #iterate through result find base ticker, targets that are paired to USD, and last price
        if c["base"] == crypto and "USD" in c["target"]: #find crypto and only show paired to USD,USDC,USDT
            return c["last"] #returns the last price or spot price of the crypto


#Determines the change in price and prints to user, takes crypto ticker symbol as an argument
def getChange(crypto):
    kuprice = getPrice(crypto,"kucoin")  #sets variable for kucoin price
    cbprice = getPrice(crypto, "gdax")  #sets variable for cbprice(gdax is coinbase's code in coingecko api)
    if kuprice is None or cbprice is None:  #rejects input for tickers if not in API
        print("Ticker not found")
        return
    x = kuprice / cbprice  #determine the difference in price between the exchanges as int x
    change = 1 - x  #measure the change between the 2 assets
    if change > .005 or change < -.005:  #remove results that are within .5% of each other
        if x > 1: 
            print(crypto, "\tArbitrage at Kucoin!")  #arbitrage found at Kucoin, tabbed out
            print("\tKucoin Price:", kuprice)  #display kucoin price
            print("\tCoinbase Price:", cbprice) #display coinbase price
            print("\tDifference",round(x,5)) #display the difference limited to the 10,000th place
        else:
            print(crypto, "\tArbitrage at Coinbase!") #arbitrage found at Coinbase, tabbed out
            print("\tKucoin Price:", kuprice)
            print("\tCoinbase Price:", cbprice)
            x = cbprice / kuprice
            print("\tDiffernce",round(x,5))
    else:
        print("No arbitrage at this time for", crypto) #no arbitrage found
        print("Kucoin Price:", kuprice)
        print("Coinbase Price:", cbprice)
    print()

#If green flag clicked , gets the program started with Welcome
if __name__ =="__main__":
    print("\nWelcome to the Arbitrage Calculator!\n") #send welcome message to screen
    while True:    #loop to main menu for repeated ticker searches
        print("Press 1 to see Top 10 Cryptos\nPress 2 to search ticker") #get input 1 for top 10 2 for users choice
        choice = input()
        if choice == "1": #option 1 to print top10
            for ticker in top10: #check tickers in top 10 
                getChange(ticker) #run get change function for tickers in top10, will compare prices and display results
        elif choice == "2":   #option 2
            customTicker = input("Please input a ticker: ")  #get input for ticker
            getChange(customTicker.upper())   #force to uppercase, ticker is always upper in results
        else:
            break #if user inputs any key except 1 or 2 leave the program