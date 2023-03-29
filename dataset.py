import pandas

import pandas as pd
df = pd.read_csv(r"C:\Users\KIIT\Dropbox\My PC (DESKTOP-T2MIRLG)\Downloads\data.csv")
print(df)  
print("*********")

print(pd.options.display.max_rows) 
print("*********")

print(df.to_string()) 
