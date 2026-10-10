import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt

df =pd.read_csv(r"C:\Users\NITHISH KUMAR\Downloads\First_10_Records.csv")
print(df.head().to_string())
# print(df["Sales"].sum())

# df = np.array([[1, 2, 4, 5], [2,3,5,6]])
# print(df.flatten())
# print(df[0])


# plt.plot(df[0], df[1], marker= "o", mec="green", color ='blue', linewidth =3, ms =15, mfc ="hotpink")
# plt.show()

colorss = np.array(["red","green","blue","pink","purple","beige","brown","gray","cyan","magenta"])
plt.subplot(2,3,1)
plt.plot(df['Order ID'], df['Order Quantity'], marker = 'o', mfc = 'red', ms = 9, ls = "-", lw = 8 )
plt.title("ID by Quantity")


plt.subplot(2,3,2)
plt.pie(df['Order Quantity'],labels = df["Product Sub-Category"])
plt.title("Order Quantity")
# plt.legend()


plt.subplot(2,3,3)
plt.bar(df['Order Quantity'], df['Shipping Cost'], width = 5.5, color = colorss)
plt.title("Quantity by shipping")

# colorsss= np.array([1,23,53,22,88,93,44,32,53,62])

plt.subplot(2,3,4)
plt.scatter(df['Order Quantity'], df['Sales'], s = 43, c = colorss)  ###, cmap = 'viridis'
plt.colorbar()
plt.title("Order by Sales")

plt.subplot(2,3,5)
plt.barh(df['Order Quantity'], df['Unit Price'], height = 7.4 , color = colorss)
plt.title("Quantity by Price")

plt.subplot(2,3,6)
plt.hist(df["Unit Price"], color = 'blue')
plt.title("Units by  ID")
plt.xticks(rotation = 45)

plt.suptitle("Sales Data Analysis")
plt.show()

