import networkx as nx
import requests
import json
import mapping
import alpaca_trade_api as tradeapi
import time
from alpaca_trade_api.rest import APIError
import os
from datetime import datetime
import csv

# This url pulls all currency exchange rates at once from CoinGecko
url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,chainlink,polkadot,dogecoin,avalanche-2,uniswap&vs_currencies=eth,btc,ltc,xrp,ada,btc,link,dot,doge,avax,uni"

# requests exchange rates from coin gecko
request = requests.get(url)
# print(request.text) # print to double check data from web json api is good
rates = json.loads(request.text)

#creates empty graph called g
g =  nx.DiGraph()

#adds nodes and edges to g from the rates dictionary
mapping = {
    "bitcoin": "btc",
    "bitcoin-cash": "bch",
    "cardano": "ada",
    "eos": "eos",
    "ethereum": "eth",
    "litecoin": "ltc",
    "ripple": "xrp",
    "chainlink": "link",
    "polkadot": "dot",
    "dogecoin": "doge",
    "avalanche-2": "avax",
    "uniswap": "uni",
    "stellar": "xlm"
}
edges = [
    (mapping[a], b, w)
    for a, inner in rates.items()
    for b, w in inner.items()
]
g.add_weighted_edges_from(edges)


# sets smallest and largest weights and paths to be updated later
smallest_weight = 1
smallest_paths = []
largest_weight = 1
largest_path = []

# Goes through every combination of currency, finds all paths to and from, and calculates weight. Updates largest weight
for node in g:
    for node2 in g:
        if node != node2:
            # Finds all the paths
            # print("paths from",node, "to",node2)
            paths = nx.all_simple_paths(g, node, node2)
            for path in paths:
                # ---- FORWARD WEIGHT ----
                forward = 1
                for u, v in zip(path, path[1:]):
                    forward *= g[u][v]['weight']

                # ---- REVERSED PATH ----
                rev_path = list(reversed(path))

                # ---- REVERSE WEIGHT ----
                reverse = 1
                try:
                    for u, v in zip(rev_path, rev_path[1:]):
                        reverse *= g[u][v]['weight']
                except KeyError:
                    # no reverse edge — skip this roundtrip
                    # print(path, "has no valid reverse path → skipped\n")
                    continue

                # ---- TOTAL ROUND-TRIP VALUE ----
                roundtrip = forward * reverse

                # print(path, forward)
                # print(rev_path, reverse)
                # print(roundtrip)
                if roundtrip > largest_weight:
                    largest_weight = roundtrip
                    largest_path = path+rev_path[1:]
                if roundtrip < smallest_weight:
                    smallest_weight = roundtrip
                    smallest_paths = [path,rev_path]

# # print statements detailing the findings
# print('Smallest Paths weight factor:', smallest_weight)
# print('Paths',smallest_paths)
print('Greatest Paths weight factor:', largest_weight)
print('Greatest Path',largest_path)

base_url = "https://paper-api.alpaca.markets/"
api_key = "PK5U2N5OG5KQNLAHX7NUOHCCGF"
api_secret = "4Vdy19axkgtQpy5ryjM3HeCKacnCC699gkKMiN4FSPEU"

# instantiate REST API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')
# # obtain account information *Use to test connectivity*
# account = api.get_account()
# print(account)

# # Submit a test buy order for $10 of BTC
# for currency in largest_path:
#     symbol = currency.upper() + "/USD"

#     # BUY $10 worth
#     api.submit_order(
#         symbol=symbol,
#         notional=10,
#         side="buy",
#         type="market",
#         time_in_force="gtc"
#     )

#     # FETCH how much we actually got
#     position = api.get_position(symbol)
#     qty = position.qty  # This is a string, but Alpaca accepts it

#     # SELL exactly that amount
#     api.submit_order(
#         symbol=symbol,
#         qty=qty,
#         side="sell",
#         type="market",
#         time_in_force="gtc"
#     )

def symbol_slash(sym):
    return sym.upper() + "/USD"

def symbol_noslash(sym):
    return sym.upper() + "USD"


def buy_and_sell(api, currency, notional=10):
    """
    Buy $notional of a crypto and sell exactly what fills.
    Handles:
      - buy fill delay
      - 404 no position
      - symbol format differences
      - insufficient balance
    """

    slash = symbol_slash(currency)      # BTC/USD
    noslash = symbol_noslash(currency)  # BTCUSD

    # ---------------------- BUY ----------------------
    api.submit_order(
        symbol=slash,
        notional=notional,
        side="buy",
        type="market",
        time_in_force="gtc"
    )

    # Wait briefly for fill
    time.sleep(2)

    # ---------------------- CHECK POSITION ----------------------
    try:
        position = api.get_position(noslash)   # BTCUSD format works better for positions
    except APIError as e:
        if "404" in str(e):
            print(f"No position found for {currency} yet. Skipping sell.")
            return
        else:
            raise

    qty = float(position.qty)

    if qty <= 0:
        print(f"Position quantity zero for {currency}. Nothing to sell.")
        return

    # ---------------------- SELL EXACT QTY ----------------------
    api.submit_order(
        symbol=slash,
        qty=qty,
        side="sell",
        type="market",
        time_in_force="gtc"
    )

    print(f"Completed buy + sell cycle for {currency}: sold {qty} units.")

for currency in largest_path:
    buy_and_sell(api, currency)






def save_exchange_rates():
    # ------------------------- PREP FOLDER -------------------------
    os.makedirs("data", exist_ok=True)

    # ------------------------- CREATE FILENAME -------------------------
    timestamp = datetime.now().strftime("%Y.%m.%d:%H.%M")
    filename = f"currency_pair_{timestamp}.txt"
    filepath = os.path.join("/home/ubuntu/final_project/data", filename)

    # ------------------------- WRITE CSV -------------------------
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["currency_from", "currency_to", "exchange_rate"])

        for currency_from, conversions in rates.items():
            from_symbol = mapping[currency_from]  # <-- convert ID → symbol

            for currency_to, rate in conversions.items():
                writer.writerow([from_symbol, currency_to, rate])

    print(f"Saved {filepath}")
save_exchange_rates()