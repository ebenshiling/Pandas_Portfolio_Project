# %%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"D:\python tut\csv files\Customer Call List.xlsx")
df


# %%
df["Last_Name"] = df["Last_Name"].str.strip("123/_.")
df["First_Name"]
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"]  = df["Phone_Number"].apply(lambda x: x[0:3]+ "-" + x[3:6] + "-"+ x[6:10])
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')



# %%
df["Phone_Number"] = df["Phone_Number"].str.replace('--', '')


# %%

df

# %%
address_split = df["Address"].str.split(',', expand = True)
df = df.assign(Street_Address = address_split[0], State = address_split[1], Zip_Code = address_split[2])


# %%
df["Paying Customer	"] = df["Paying Customer"].str.replace("Yes","Y").str.replace("No","N")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes","Y").str.replace("No","N")

# %%
df = df.drop(columns="Paying Customer\t")

# %%
df.fillna('', inplace=True)
df

# %%
df

# %%
for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == "Y":
        df.drop(x, inplace=True)
        
            

# %%
for x in df.index:
    if df.loc[x,"Phone_Number"] == " ":
        df.drop(x, inplace= True)
    

# %%
df

# %%
df.to_csv(r"D:\Dataset\new_data.csv")

# %%



