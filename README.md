This is a school project - this is not financial advice - use at your own risk.

Arbitrage.py is designed to detect currency arbitrage opportunites that 
exist on the crypto currency exchanges Coinbase and Kucoin.

Please see associated video: https://youtu.be/sOwl4JtS7Mo


Please install CoinGecko Python API wrapper by typing in linux command line.
    pip install pycoingecko


To run Arbitrage type in Linux command line:

python3 arbitrage.py

-------------------------------------------

At the Welcome Screen you will have 2 options.

Option #1 See top 10 Cryptos
Option #2 User Search

Option #1 will find arbitrage opportunities between the top 10 crypto currencies.
Make sure to expand your terminal window tall enough to see all the results.

Option #2 gives the user the ability to input there own crypto ticker. Crypto tickers are 3-4 letter codes i.e. BTC, As long as the ticker is valid, within CoinGecko's Database, and on both exchanges you will get valid results. If the ticker is not valid the program will state so and return to options.

If you want to leave the options press any key and then enter.

Interpreting the results:

If the price difference on the exchanges is within .5% of each other there is no opportunity and it will say:
    No arbitrage at this time for <Ticker>
    Kucoin Price: 1.1
    Coinbase Price: 1.1

If the price difference is great enough the crypto will tab outwards and say:
    <Ticker> Arbitrage at <Exchange>!
    Kucoin price: 5
    Coinbase Price: 6
    Difference 1.2

You can use the difference to guauge if the arbitrage opportunity may be worthwhile.





Please enjoy the calculator! And thank you for a great semester!

Doug Langstraat


Further Reference:

Python wrapper for CoinGecko API https://pypi.org/project/pycoingecko/

Triangular Arbitrage https://en.wikipedia.org/wiki/Triangular_arbitrage
