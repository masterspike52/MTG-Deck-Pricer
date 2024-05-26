# MTG-Deck-Pricer
tool to price your mtg decks so you dont have to add them to a cart or have to do math to figure the ones missing

how it works

The program uses the scryfall api for pricing and card data. the scryfall api pulls the card prices from multiple sources and uses the average price from those sources 
please see https://scryfall.com/docs/faqs/where-do-scryfall-prices-come-from-7 

how to use the tool 

1. download the zip file from the github
2. install the latest version of python (if you dont already have it)
3. run pip install -r requirements.txt to install the requirements (at the moment its only requests and tk)
4. run deckprice.py
5. input each cards (or individual cards) into the box and click calculate price
