# Marco Remmerswaal
import pandas as pd

### Filter Sectie ###

Kosten_filter = 3
Conversion_filter = 0
ctr_filter = "0.02%"

### Filter Sectie ###


Filename = "match.csv"
Cost = "Total Media Cost (Advertiser Currency)"
Url = "App/URL"
Ctr = "Click Rate (CTR)"
Conversions = "Total Conversions"
Clicks = "Clicks"
Impressions = "Impressions"

df = pd.read_csv(Filename, sep = ",", low_memory=False)
df.sort_values(by=[Cost], inplace=True, ascending=False)
columns = ["Advertiser Currency", "App/URL ID"]
df.drop(columns, inplace=True, axis=1)
df.dropna()


df[Cost] = df[Cost].round(2)
df[[Url, Impressions, Clicks, Ctr, Conversions, Cost]]

resultaat = df[
    (df[Cost] > Kosten_filter)
    & ((df[Conversions] <= Conversion_filter))
    & ((df[Ctr] <= ctr_filter))
    ]

resultaat.to_csv("output.csv")
print("Done!")