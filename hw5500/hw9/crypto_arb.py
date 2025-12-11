import networkx as nx
import requests
import json
import mapping

#This url pulls all currency exchange rates at once
url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum,bitcoin,litecoin,ripple,cardano,bitcoin-cash,eos&vs_currencies=eth,btc,ltc,xrp,ada,btc,eos"

# requests exchange rates from coin gecko
request = requests.get(url)
# print(request.text) # print to double check data from web json api is good
dct_full = json.loads(request.text)



#creates empty graph called g
g =  nx.DiGraph()

#adds nodes and edges to g
mapping = {
    "bitcoin": "btc",
    "bitcoin-cash": "bch",
    "cardano": "ada",
    "eos": "eos",
    "ethereum": "eth",
    "litecoin": "ltc",
    "ripple": "xrp"
}
edges = [
    (mapping[a], b, w)
    for a, inner in dct_full.items()
    for b, w in inner.items()
]
g.add_weighted_edges_from(edges)

# sets smallest and largest weights and paths to be updated later
smallest_weight = 1
smallest_paths = []
largest_weight = 1
largest_paths = []

# Goes through every combination of nodes
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
                    largest_paths = [path,rev_path]
                if roundtrip < smallest_weight:
                    smallest_weight = roundtrip
                    smallest_paths = [path,rev_path]

# print statements detailing the findings
print('Smallest Paths weight factor:', smallest_weight)
print('Paths',smallest_paths)
print('Greatest Paths weight factor:', largest_weight)
print('Paths',largest_paths)


