class DairyProduct:
    def __init__(self,dairyId,dairyBrand,productType,price,grade):
        self.dairyId=dairyId
        self.dairyBrand=dairyBrand
        self.productType=productType
        self.price=price
        self.grade=grade

class ProductGrade:
    def __init__(self,dairyList,weightageDict):
        self.dairyList=dairyList
        self.weightageDict=weightageDict

    def priceBasedOnBrandAndType(self,dairyBrand,productType):
        d={}
        for i in self.dairyList:
            if i.dairyBrand==dairyBrand and i.productType==productType:
                updatedPrice=i.price+i.price*self.weightageDict.get(i.grade)/100
                d.update({i.dairyBrand:updatedPrice})
        return d


if __name__=='__main__':
    n=int(input())
    dairyList=[]
    for i in range(n):
        id=int(input())
        brand=input()
        product=input()
        price=int(input())
        grade=input()
        dairyList.append(DairyProduct(id,brand,product,price,grade))
    m=int(input())
    weightageDict={}
    for i in range(m):
        grade=input()
        weightage=int(input())
        weightageDict.update({grade:weightage})
    obj=ProductGrade(dairyList,weightageDict)
    brand=input()
    product=input()
    if obj.priceBasedOnBrandAndType(brand,product)==None:
        print("No dairy product found")
    else:
        for key,value in obj.priceBasedOnBrandAndType(brand,product).items():
            print('Dairy Brand : '+key)
            print(('Price : '+str(value)))