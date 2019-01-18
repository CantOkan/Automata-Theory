#q0 = {'Name': 'q0', '1': 'q1', '0': 'q0'}

class q0Node(object):#initial State and also #Final State
    def __init__(self,s,i):
        self.s=s
        self.i=i

    def transition(self,i):
        self.i=i
        print("q0")
        if(len(self.s)>self.i):
            if(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to q0)")
                q0.transition(self.i+1)
            elif(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to q1)")
                q1.transition(self.i+1)
        else:
            print("It is a Final State")

class q1Node(object):
    def __init__(self,s):
        self.s=s
    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to q3)")
                q3.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to q2)")
                q2.transition(self.i+1)
        else:
            print("It is not a Final State X")


class q2Node(object):
    def __init__(self,s):
        self.s=s

    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to q0)")
                q0.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to q4)")
                q4.transition(self.i+1)
        else:
            print("It is not a Final State X")



class q3Node(object):
    def __init__(self,s):
        self.s=s

    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to q2)")
                q2.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to q1)")
                q1.transition(self.i+1)
        else:
            print("It is not a Final State X")
            print("divisible by 5")


class q4Node(object):
    def __init__(self,s):
        self.s=s

    def transition(self,i):
        self.i=i
        if(len(self.s)>self.i):
            if(self.s[self.i]=="1"):
                print(self.s[self.i]+"-(go to q4)")
                q4.transition(self.i+1)
            elif(self.s[self.i]=="0"):
                print(self.s[self.i]+"-(go to q3)")
                q3.transition(self.i+1)
        else:
            print("It is not a Final State X")

s1="1010"
s2="11"

print(s1)
q0=q0Node(s1,0)
q1=q1Node(s1)
q2=q2Node(s1)
q3=q3Node(s1)
q4=q4Node(s1)
q0.transition(0)

print("----------------------------------------------")
print(s2)
q0=q0Node(s2,0)
q1=q1Node(s2)
q2=q2Node(s2)
q3=q3Node(s2)
q4=q4Node(s2)
q0.transition(0)
