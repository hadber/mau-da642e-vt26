# Frozen!
import datetime as dt

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("./data/aw_fb_data.csv")
print(df["calories"])

# part I
# fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

#df["cals_log10"] = df["calories"].transform(np.log10)
#df["cals_sqrt"] = df["calories"].transform(lambda x: np.power(x, 1/2))
#df["cals_exp"] = df["calories"].transform(lambda x: np.exp(x))

#ax1.hist(df["calories"])
#ax1.set_title("original")

#ax2.hist(df["cals_log10"])
#ax2.set_title("cals_log10")

#ax3.hist(df["cals_sqrt"])
#ax3.set_title("cals_sqrt")

#ax4.hist(df["cals_exp"])
#ax4.set_title("cals_exp")

#plt.show()

# part II

#df_dups = df.copy()
#df_dups = df.drop_duplicates(subset=['age', 'height', 'weight'])
#print(df_dups)

#fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

#ax1.hist(df_dups['age'])
#ax1.set_title("age [years]")

#ax2.hist(df_dups['height'], color='orange')
#ax2.set_title("height [cm]")

#ax3.hist(df_dups['weight'], color='green')
#ax3.set_title("weight [kg]")

#plt.show()

# part III

df["user_id"] = df.groupby(['age', 'height', 'weight']).ngroup()

#fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

#user_one = df[(df["user_id"] == 1)]
#ax1.plot(user_one["steps"].values, label="steps")
#ax1.plot(user_one["hear_rate"].values, label="hear_rate")
#ax1.plot(user_one["calories"].values, label="calories")
#ax1.legend(loc="upper right")
#ax1.set_title("user one")


#user_two = df[(df["user_id"] == 2)]
#ax2.plot(user_two["steps"].values, label="steps")
#ax2.plot(user_two["hear_rate"].values, label="hear_rate")
#ax2.plot(user_two["calories"].values, label="calories")
#ax2.legend(loc="upper right")
#ax2.set_title("user two")


#user_three = df[(df["user_id"] == 3)]
#ax3.plot(user_three["steps"].values, label="steps")
#ax3.plot(user_three["hear_rate"].values, label="hear_rate")
#ax3.plot(user_three["calories"].values, label="calories")
#ax3.legend(loc="upper right")
#ax3.set_title("user three")

# part IV

age_df = df["age"]
df["norm_age"] = (age_df-age_df.min())/(age_df.max()-age_df.min())

height_df = df["height"]
df["norm_height"] = (height_df-height_df.min())/(height_df.max()-height_df.min())

weight_df = df["weight"]
df["norm_weight"] = (weight_df-weight_df.min())/(weight_df.max()-weight_df.min())

steps_df = df["steps"]
df["steps_std"] = (steps_df-steps_df.mean())/steps_df.std()

hrate_df = df["hear_rate"]
df["hear_rate_std"] = (hrate_df-hrate_df.mean())/hrate_df.std()

df.to_csv("./data/aw_fb_data-processed.csv", index=False)

# part V

# shuffle first, then grab the first x*.7, etc
df = df.sample(frac=1).reset_index(drop=True)
total_size = df.shape[0]
train = int(total_size*0.7) # force int
val = train + int(total_size*0.15)
test = val + int(total_size*0.15)

train_df = df[0:train]
val_df = df[train:val]
test_df = df[val:test]

# results in 3 dataframes:
# [4384 rows x 26 columns]
# [939 rows x 26 columns]
# [939 rows x 26 columns]
