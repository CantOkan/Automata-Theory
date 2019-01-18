class ANode(object):#initial State
    def __init__(self,s,i):
        self.s=s
        self.i=i
    def transition(self):
        print("A")
        if(len(self.s)>=self.i):
            if(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to B)")
                b.transition(self.i+1)
            elif(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to B)")
                b.transition(self.i+1)
        else:
            print("It is not a Final State X")

class BNode(object):#State
    def __init__(self,s):
        self.s=s

    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to C)")
                c.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to C)")
                c.transition(self.i+1)
        else:
            print("It is not a Final State X")

class CNode(object):#Final State
    def __init__(self,s):
        self.s=s

    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to D)")
                d.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to D)")
                d.transition(self.i+1)
        else:
            print("in Final State ")
            print("It is a String")

class DNode(object):#Dead State
    def __init__(self,s):
        self.s=s

    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to D)")
                d.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to D)")
                d.transition(self.i+1)
        else:
            print("It is not a Final State(Trap State) X")

s1="01"
print(s1)
a=ANode(s1, 0)
b=BNode(s1)
c=CNode(s1)
d=DNode(s1)
a.transition()


print("****************************************")
#second string test
s2="10"
print(s2)
a=ANode(s2, 0)
b=BNode(s2)
c=CNode(s2)
d=DNode(s2)
a.transition()

print("****************************************")
#third string test
s3="101"
print(s3)
a=ANode(s3, 0)
b=BNode(s3)
c=CNode(s3)
d=DNode(s3)
a.transition()
