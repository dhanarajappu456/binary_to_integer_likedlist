class node:
    
    def __init__(self,data):
        self.data=data 
        self.next=None
                
class create:
    head=None
    def __init__(self):
        pass 
    def created(self,obj):
        
        if(self.head==None):
            self.head=obj
        else:
            temp=self.head
            while(temp.next!=None ):
                
                temp=temp.next
        
            temp.next=obj


a=node(1)
b=node(0)
c=node(1)
d=node(1)
inter=create()

inter.created(a)
inter.created(b)
inter.created(c)
inter.created(d)
temp=inter.head
val=0
while(temp!=None):
 val=val<<1
 val+=temp.data
 print(val)
 temp=temp.next

print("bin------>int",val)








