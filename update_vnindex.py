from vnstock import Vnstock
import json

stock = Vnstock().stock(symbol="VNINDEX", source="VCI")
quote = stock.quote.intraday_quote()

latest = quote.iloc[-1]

data = {
    "VNINDEX": float(latest["price"]),
    "time": str(latest["time"])
}

with open("vnindex.json", "w") as f:
    json.dump(data, f)
