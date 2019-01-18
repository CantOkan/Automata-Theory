
#E-epsilon
class q0(object):
    def __init__(self,s,i):
        self.s=s
        self.i=i
    def transition(self):
        if(len(self.s)>=self.i):
            print(self.s)
            if(self.s[self.i]=="E"):
                print("q0 State read E, pop E,push Z ")
                stk.push("Z")
                b.transition(self.i+1)


class q1(object):
    def __init__(self,s):
        self.s=s
    def transition(self,i):
        self.i=i
        if(len(self.s)>=self.i):
            if(self.s[self.i]=="E"):
                print(self.s[self.i])
                print("q1 state read E,pop E,push S")
                stk.push("S")
                c.transition(self.i+1)


class qloop(object):
    def __init__(self,s):
        self.s=s
    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="a"):
                st=stk.get_stack()
                if(st[-1]=="S"):
                    print("--------------------------------")
                    print("qloop situation 1: read E, pop S,Push S")
                    print("--------------------------------")
                    stk.pop()#pop s
                    #print(stk.get_stack())
                    stk.push("S")
                    st1.transition(self.i)
                                                                            #for i in st:
                elif(st[-1]=="a"):
                    print("--------------------------------")
                    print("qloop situation2(terminal) read a,pop a,push E")
                    print("--------------------------------")
                    stk.pop()
                    terminal.push("a")                                                                     #print(i)
                    print(stk.get_stack())
                    #print("input",self.s[self.i+1])
                    c.transition(self.i+1)

            elif(self.s[self.i]=="b"):
                st=stk.get_stack()
                if(st[-1]=="S"):
                    print("--------------------------------")
                    print("qloop situation 3: read E, pop S,Push b")
                    print("--------------------------------")
                    stk.pop()#pop S
                    #print(stk.get_stack())
                    stk.push("b")

                    c.transition(self.i)

                elif(st[-1]=="b"):
                    print("--------------------------------")
                    print("qloop situation3(terminal) read b,pop b,push E")
                    print("--------------------------------")
                    stk.pop()
                    terminal.push("b")                                                                     #print(i)
                    print(stk.get_stack())
                    c.transition(self.i+1)
        else:
            final.transition()


class st1(object):
    def __init__(self,s):
        self.s=s
    def transition(self,i):
        self.i=i
        print("st1 read E,pop E,push a")
        stk.push("a")
        print(stk.get_stack())
        c.transition(self.i)


class Final(object):
    def __init__(self,s):
        self.s=s

    def transition(self):
        print("qloop final_Situation(terminal) read E,pop Z,push E")
        print("--------------------------------")
        stk.pop()
        print("Final State (String is acceppted) {}".format(terminal.get_stack()))

class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get_stack(self):
        return self.items


string=['E','E','a','a','b']
#['E','E','a','a','a','b']
stk=Stack()
terminal=Stack()

a=q0(string,0)
b=q1(string)
c=qloop(string)
st1=st1(string)
final=Final(string)

a.transition()
print(stk.get_stack())
