lists= """
rice   rs 50/kg,
sugar  rs 50/kg,
salt   rs 20/kg,
oil    rs 130/kg,
maida  rs 40/kg,
atta   rs 50/kg,
maaza  rs 90/litre
"""


price=0
pricelist=[]
totalprice=0
Finalfinalprice=[]
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':50,'sugar':50,'salt':20,'oil':130,'maida':40,'atta':50,'maaza':90}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))    
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("you entered wrong item") 
    else:
        print("you entered wrong number")
    inp= input("can i bill the items yes or no :")
    if inp=='yes':
        pass    
        if finalamount!=0:
           for i in range(len(pricelist)): 
               print(i,ilist[i],qlist[i],plist[i])
               
    else:
            print("Select products")

    Finalfinalprice=sum(plist)
    print("Total bill:",Finalfinalprice)