from vnstock_data import Market
import json

mkt = Market()
df = mkt.index("VNINDEX").quote()
latest = df.iloc[-1]

data = {
    "VNINDEX": float(latest["price"]),
    "time": str(latest["time"])
}

with open("vnindex.json", "w") as f:
    json.dump(data, f)
