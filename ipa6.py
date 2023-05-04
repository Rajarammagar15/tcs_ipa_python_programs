class Property:
    def __init__(self,property_type,property_value,max_bid_price):
        self.property_type=property_type
        self.property_value=property_value
        self.max_bid_price=max_bid_price

class Tender:
    def __init__(self,buyerName,propertyType,bidPrice):
        self.buyerName=buyerName
        self.propertyType=propertyType
        self.bidPrice=bidPrice

def bidProperty(plist,tlist):
    l=[]
    for i in tlist:
        for j in plist:
            if i.propertyType==j.property_type:
                if j.property_value<=i.bidPrice and i.bidPrice<=j.max_bid_price:
                    l.append(i)
    l1=[]
    for i in l:
        l1.append(i.bidPrice)
    for i in l:
        if max(l1)==i.bidPrice:
            return i.buyerName or l



if __name__=='__main__':
    n=int(input())
    plist=[]
    tlist=[]
    for i in range(n):
        property_type=input()
        property_value=int(input())
        max_bid_price=int(input())
        plist.append(Property(property_type.lower(),property_value,max_bid_price))
    m=int(input())
    for i in range(m):
        buyerName=input()
        propertyType=input()
        bidPrice=int(input())
        tlist.append(Tender(buyerName,propertyType,bidPrice))
    if bidProperty(plist,tlist)==None:
        print('Property Not found')
    else:
        print(bidProperty(plist,tlist))
    