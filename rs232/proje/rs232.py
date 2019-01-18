class Transmitter(object):#initial State and also #Final State
    def __init__(self,s=[]):
        self.s=s

    def transition(self):
        r.reciving(self.s)

class Receiver(object):
    msg=[]
    def __init__(self,key=[]):
        self.key=key
    def reciving(self,m=[]):
        for i in range(0,len(m)) :
            print(m[i])
            if(m[i]==self.key[0]):
                if(m[i+1]==self.key[1]):
                    for s in range(i+2,i+10):
                        self.msg.append(m[s])
                    self.store()
                    break;

    def store(self):
        print("start to receving")
        for i in self.msg:
             print(i, end="")



    '''
    for s in range(i+1,i+9):#8 bit storing
        self.msg.append(m[s])
    '''
r=Receiver(['1','0'])
msg1=Transmitter(['0','1','1','1','0','1','1','1','1','1','0','1','0','1','0','0','1'])
msg1.transition()
