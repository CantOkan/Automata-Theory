class Transmitter(object):#Transmitter
    def __init__(self,s=[]):
        self.s=s
        self.r=r
    def transition(self):
        r.start(self.s)

class Receiver(object):#Receiver
    msg=[]
    def __init__(self,key=[],fkey=[]):
        self.key=key
        self.fkey=fkey
    def start(self,m=[]):
        print("start to receving")
        i=0
        while i<len(m):
            print(m[i])
            if(m[i]==self.key[0]):
                if(m[i+1]==self.key[1]):
                    print(m[i+1])
                    i+=2
                    print("Starting bit was received")
                    self.store(i,m)
                    break;
            i+=1


    def store(self,i,m):
        print("start to storing")
        c=i
        while c<(i+8):#8 bit storing
            print(m[c], end="")
            self.msg.append(m[c])
            c+=1
        print("\nend to storing")
        self.end(c,m)

    def end(self,i,m):
        print("Control to stop bits")
        for i in range(i,len(m)):
            print(m[i])
            if(m[i]==self.fkey[0] and i<(len(m)-1)):
                if(m[i+1]==self.fkey[1]):
                    print(m[i+1])
                    self.show(True)
                    break
        else:
                self.show(False)



    def show(self,isstreamTrue):
        if(isstreamTrue==True):
            print("Stream is True")
            print("Stored value")
            for i in self.msg:
                 print(i, end="")
        else:
            print("Stream is False")
            print("There is no stored value")
            self.msg.clear()

r=Receiver(['0','1'],['1','1'])
msg1=Transmitter(['1','1','1','0','1','1','1','1','0','1','1','1','0','0','1'])
print("Mesaj1")
print("first bit stream")
for i in msg1.s:
     print(i, end="")
print("\n")
msg1.transition()


msg2=Transmitter(['1','1','1','1','0','1','1','1','1','0','1','1','1','0','1','1'])
print("\n Mesaj 2")
print("second bit stream")
for i in msg2.s:
     print(i, end="")
print("\n")

msg2.transition()
