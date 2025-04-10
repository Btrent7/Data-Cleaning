import pandas as pd
import numpy as np

pivot_table = r"C:\Users\btrent\\Data Analysis.xlsx"
unpivot_table = r"C:\Users\btrent\\Data Analysis2.xlsx"
test_table = r"C:\Users\btrent\\Data Analysis3.xlsx"

df = pd.read_excel(pivot_table, sheet_name = "Sheet1")

df["Date"] = pd.to_datetime(df["Date"]).dt.date

pivot_melted = df.melt(id_vars=["Date", "Site"], var_name= "Location", value_name="Value")

pivot_unpivoted = pivot_melted.pivot_table(index=["Date", "Location"], columns="Site", values="Value").reset_index()

pivot_unpivoted.columns.name = None
pivot_unpivoted.rename(columns={"Location": "Site"}, inplace=True)

print(pivot_unpivoted)

# pivot_unpivoted.to_excel(unpivot_table, index=False)
print("Complete!")

overall_table = pivot_unpivoted.groupby("Site")[["Orders", "Stocks", "Drops", "W/C", "Quotes", "Closed"]].agg([min, max, sum])
overall_table.columns = ["_".join(col).strip() for col in overall_table.columns.values]

print(test_table)

overall_table = overall_table.reset_index()

overall_table["Stock Ratio"] = overall_table["Stocks_sum"] / overall_table["Orders_sum"]
overall_table["Drop Ratio"] = overall_table["Drops_sum"] / overall_table["Orders_sum"]
overall_table["W/C Ratio"] = overall_table["W/C_sum"] / overall_table["Orders_sum"]
overall_table["Range %"] = ((overall_table["Orders_max"] - overall_table["Orders_min"]) / overall_table["Orders_sum"] )
overall_table["Closed %"] = np.where(overall_table["Quotes_sum"] == 0, 0, overall_table["Closed_sum"] / overall_table["Quotes_sum"] )

Closed_bins = [0.0, 0.25, 0.40, 0.50, 0.60, 1]
Closed_labes = [1, 2, 3, 4, 5]

overall_table["Closed_bins"] = pd.cut(overall_table["Closed %"], bins=Closed_bins, labels=Closed_labes, include_lowest=True)

Range_bins = [0.0, 0.07, 0.14, 0.21, 0.28, 0.50]
Range_lables = [1, 2, 3, 4, 5]

overall_table["Range_bins"] = pd.cut(overall_table["Range %"], bins=Range_bins, labels=Range_lables, include_lowest=True)

overall_table = overall_table.drop(["Orders_max", "Orders_min", "Stocks_min", "Stocks_max", "Drops_min", "Drops_max", 
                              "W/C_min", "W/C_max", "Quotes_min", "Quotes_max", "Closed_min", "Closed_max"], axis=1)
print(overall_table)

# overall_table.to_excel(test_table, index=False)

Closed_orders = overall_table.groupby("Closed_bins")["Closed_sum"].agg([sum, max])
Closed_Avg =  overall_table.groupby("Closed_bins")["Closed %"].mean()
Closed_Site = overall_table.groupby("Closed_bins")["Site"].count()
Range_orders = overall_table.groupby("Range_bins")["Orders_sum"].agg([min, max])
Range_Avg = overall_table.groupby("Range_bins")["Range %"].mean()
Range_Site = overall_table.groupby("Range_bins")["Site"].count()
# print(f"""Closed Orders: 
#       {Closed_orders} 
#       Closed Avg: 
#       {Closed_Avg} 
#       Range Orders: 
#       {Range_orders} 
#       Range Avg: 
#       {Range_Avg}""")

Summary_Closed = pd.concat([Closed_orders, Closed_Avg, Closed_Site], axis=1) 
Summary_Range = pd.concat([Range_orders, Range_Avg, Range_Site], axis=1)

Summary_Closed = Summary_Closed.reset_index()
Summary_Range = Summary_Range.reset_index()


print(Summary_Closed)
print()
print(Summary_Range)

with pd.ExcelWriter (test_table) as write:
    overall_table.to_excel(write, sheet_name="Overall_summary", index=False)
    Summary_Closed.to_excel(write, sheet_name="Closed_%_Summmary", index=False)
    Summary_Range.to_excel(write, sheet_name="Order_Range_Summary", index=False)
