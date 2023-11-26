#imports
import requests
import pandas

#getting database, hypixel doesn't work
raw=pandas.read_csv("diamonds.csv")
class sortData:
    def __init__(self,data):
        #read data into the class
        self.data=data
    def sortType(self):
        items={"Ideal":0,"Premium":0,"Good":0,"Very Good":0,"Fair":0}
        for x in self.data["cut"]:
            #they will be put in the dictanary
            cut=x
            if(cut=="Ideal"):  
                items["Ideal"]=items["Ideal"]+1
            elif(cut=="Premium"):  
                items["Premium"]=items["Premium"]+1
            elif(cut=="Good"):  
                items["Good"]=items["Good"]+1
            elif(cut=="Very Good"):  
                items["Very Good"]=items["Very Good"]+1
            elif(cut=="Fair"):  
                items["Fair"]=items["Fair"]+1
        print(items)
        return items
            
    def extreamPrice(self):
        low=bool
        high=bool
        for x in enumerate(self.data["price"]):
            if(x[0]==0):
                low=x[1]
                high=x[1]
            else:
                if(x[1]>high):
                    high=x[1]
                if(x[1]<low):
                    low=x[1]
        print(f"{high},{low}")
    def meanprice(self):
        price=.0
        itemnum=0
        for x in self.data["price"]:
            price=price+x
            itemnum=itemnum+1
        print(f"{price/itemnum:.2f}")
        return price/itemnum
    #techicly good, but i could combine cut and mean of price.
    
    
#print(raw["cut"])
#options
item = sortData(raw)
#item.extreamPrice()
#item.meanprice()
#item.sortType()
#Shove menue to fetch info here
menue=1
while (menue!=0):
    print("Options: 0 to quit, 1 to find price min and max, \n2 to find the price mean, and 3 to find the number of each type.")
    menue=int(input())
    if(menue==1):
        item.extreamPrice()
    elif(menue==2):
        item.meanprice()
    elif(menue==3):
        item.sortType()

