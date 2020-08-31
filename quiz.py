#QUIZ-QUESTION BANK
import pickle
import os
def getnextqno(c):
    n=0
    try:
        file=open("question.dat","rb")
        while True:
            ob=pickle.load(file)
            if ob.category==c:
                n=ob.qno
    except EOFError:
        file.close()
        return n+1
    except IOError:
        pass

 
class Questions :
    def __init__(self):
        self.category=0
        self.qno=0
        self.question=""
        self.options={}
        self.answer=""
        self.explanation=""
    def qinput(self):
        print("Enter question bank ")
        print
        print("Enter the category ")
        print
        print("1. Sports")
        print
        print("2. Current Affairs")
        print
        print("3. History")
        print
        print("4. Politics")
        print
        print("5. maths")
        print
        print("6. Science ")
        print
        print("7. mental ability")
        print
        print("8. rapid fire")
        print
        self.category=int(input("Enter category "))
        if self.category==1:
            print( "enter the question in sports category")
            print
        elif self.category==2:
               print( "enter the question in current affairs category")
               print
        elif self.category==3:
               print ("enter the question in histoty category")
               print
        elif self.category==4:
               print ("enter the question in politics category")
               print
        elif self.category==5:
               print ("enter the question in maths category")
               print
        elif self.category==6:
               print ("enter the question in science category")
               print
        elif self.category==7:
            print("enter the questions in mental ability category")
            print
        elif self.category==8:
            print("enter the questions for rapid fire round")
            print
        else:
            print("category not found")
            exit()
        print
        self.qno=getnextqno(self.category)
        print ("QUESTION no. ",self.qno)
        print
        self.question=input("Enter question ")
        print
        self.options=dict()
        self.options["A"]=input("enter first option ")
        print
        self.options["B"]=input("enter second option ")
        print
        self.options["C"]=input("enter third option ")
        print
        self.options["D"]=input("enter fourth option ")
        print
        self.answer=input("Enter answer ")
        print
        self.explanation=input("ENTER EXPLANATION ")
        print
        
    def output(self):
        print ("\n")
        print ("Category :  ",self.category)
        print
        print("Question Number :  ",self.qno)
        print
        print ("Question :  ",self.question)
        print
        print ("Options :  ",self.options)
        print
        print ("Enter Answers :  ",self.answer)
        print
        print ("Explanation is :  ",self.explanation)
        
ob=Questions()
ob1=Questions()

def sAdd():
    file=open("question.dat","ab")
    ob.qinput()
    pickle.dump(ob,file)
    file.close()
    
def sDisplay():
  try:
    file=open("question.dat","rb")
    print ('$'*166)
    print
    print (" " *70 , " CATEGORY : ")
    print 
    print ('$'*166)
    print
    print("1 PARTICULAR CATEGORY ")
    print
    print("2.Display complete data ")
    print
    ch=int(input("enter the choice :  "))
    if ch==1:
        r=int(input("enter the category you want to display :  "))
        while True:
            ob=pickle.load(file)
            if ob.category==r:
                  ob.output()
    elif ch==2:
         while True:
             ob=pickle.load(file)
             ob.output()
    else :
        print ("DATA NOT EXIST")
        exit()
  except EOFError:
         pass
         file.close()
  except IOError:
        print("FILE DOES NOT EXIST")
 
def sDelete():
   try:
       file1=open("question.dat","rb")
       file2=open("temp.dat","wb")
       print ('$'*166)
       print
       print (" " *70 , "DELETE FUNCTION :  ")
       print
       print ('$'*166)
       print
       print ("CATEGORIES ARE :  ")
       print
       print("1. Sports")
       print
       print("2. Current Affairs")
       print
       print("3. History")
       print
       print("4. Politics")
       print
       print("5. maths")
       print
       print("6. Science ")
       print
       print("7. mental ability")
       print
       print("8. rapid fire")
       print
       r=int(input("ENTER THE CATEGORY :  "))
       print
       x=int(input("ENTER THE QUESTION NUMBER :  "))
       print
       while True:
             ob=pickle.load(file1)
             if ob.qno!=x and ob.category!=r:
                pickle.dump(ob,file2)
   except EOFError:
             pass
             file1.close()
             file2.close()
             os.remove("question.dat")
             os.rename("temp.dat","question.dat")
   except IOError:
             print("FILE DO NOT EXIST")

def sModify():
   try:
             file1=open("question.dat","rb")
             file2=open("temp.dat","wb")
             print("ENTER THE DETAILS FOR THE QUIZ THAT YOU WANT TO MODIFY")
             print
             print("CATEGORIES ARE")
             print
             print("1. Sports")
             print
             print("2. Current Affairs")
             print
             print("3. History")
             print
             print("4. Politics")
             print
             print("5. maths")
             print
             print("6. Science ")
             print
             print("7. mental ability")
             print
             print("8. rapid fire")
             print
             r=int(input("ENTER THE CATEGORY :  "))
             print
             x=int(input("ENTER THE QUESTION NUMBER TO BE MODIFIED :  "))
             print
             found=0
             while True:
               ob=pickle.load(file1)
               c='n'
               if ob.qno==x and ob.category==r:
                  c=input("Do you want to change the question y/n :  ")
                  print("previous question is :  ",ob.question)
                  if c=='y':
                      ob.question=input("Enter the question : ")
                      print("modified question is :  ",ob.question)
                  print
                  c=input("Do you want to change the options y/n :  ")
                  print ("previous options are :  ",ob.options)
                  if c=='y':
                      ob.options=input("Enter the Options : ")
                      print("modified options are :  ",ob.options)
                  print
                  c=input("Do you want to change the Answer y/n :  ")
                  print ("previous answer is :  ",ob.answer)
                  if c=='y':
                      ob.answer=input("Enter the Answer : ")
                      print("modified answer is :  ",ob.answer)
                  print
                  c=input("Do you want to change the expalantion y/n :  ")
                  print("previous explanation is :  ",ob.explanation )
                  if c=='y':
                      ob.explanation=input("Enter the explanation :  ")
                      print("modified explanation is :  ",ob.explanation)
                  print
                  pickle.dump(ob,file2)
               else:
                      pickle.dump(ob,file2)
   except EOFError:
             pass
             file1.close()
             file2.close()
             os.remove("question.dat")
             os.rename("temp.dat","question.dat")
   except IOError:
             print("FILE DOES NOT EXIST")
             
def sSearch():
   try:
            file=open("question.dat","rb")
            r=int(input("ENTER THE CATEGORY"))
            print
            x=int(input("ENTER THE QUESTION NUMBER TO BE SEARCHED :  "))
            print
            found=0
            while True:
                  ob=pickle.load(file)
                  if ob.qno==x and ob.category==r:
                     ob.output()
                     found=1
   except EOFError:
                  if found==0:
                     print("QUESTION NUMBER NOT FOUND")
                     print
                  pass
                  file.close()
   except IOError:
                  print (" FILE DOES NOT EXIST ")
                  
def getnextpno():
    n=0
    try:
        file=open("player.dat","rb")
        while True:
            pb=pickle.load(file)
            n=pb.pno
    except EOFError:
        file.close()
        return n+1
    except IOError:
        pass
    
class player:
    def __init__(self):
        self.pno=0
        self.name=""
        self.age=0
        self.gender=""
        self.score=0
    def pinput(self):
        self.pno=getnextpno()
        print ("Registration no. ",self.pno)
        print
        self.name=input("Enter your name : ")
        print
        self.age=int(input("Enter your age : "))
        print
        self.gender=input("Enter your gender F/M :  ")
        print
        self.score=playgame()
        print
        print( '$'*166)
        print
        print( " " *70 ,"You scored : ",self.score)
        print
    def poutput(self):
        print ("Registration number : ",self.pno)
        print
        print( "Name : ",self.name)
        print
        print( "Age : ",self.age)
        print        
        print ("Gender : ",self.gender)
        print
        print( "Score : ",self.score)
        print
pb=player()
pb1=player()

def pAdd():
       file=open("player.dat","ab")
       pb.pinput()
       pickle.dump(pb,file)
       file.close()

def pDisplay():
   try:
    file=open("player.dat","rb")
    print ('^'*166)
    print
    print (" " *70 + "PLAYER INFORMATION : ")
    print
    print ('^'*166)
    print
    while True:
        pb=pickle.load(file)
        pb.poutput()
   except EOFError:
       pass
       file.close()
   except IOError:
       print(" FILE NOT EXIST")
       print
def pModify():
    try:
        file1=open("player.dat","rb")
        file2=open("ptemp.dat","wb")
        print( '^'*166)
        print
        print( " " *70 ,"ENTER THE DETAILS OF THE PLAYER THAT YOU WANT TO MODIFY ")
        print
        z=int(input("Enter the registration number whose details you want to modify :  "))
        print
        found=0
        while True:
            pb=pickle.load(file1)
            c='n'
            if pb.pno==z:
                c=input("Do you want to change the Name y/n : ")
                print ("YOUR NAME IS :  ",pb.name)
                if c=='y':
                    pb.name=input("Enter the Name :  ")
                    print("MODIFIED NAME IS :  ",pb.name)
                print
                c=input("Do you want to change the Age y/n :")
                print ("YOUR AGE IS :  ",pb.age)
                if c=='y':
                    pb.age=input("Enter the Age :  ")
                    print("MODIFIED AGE IS :  ",pb.age)
                print
                c=input("Do you want to change the Gender y/n : ")
                print ("GENDER IS :  ",pb.gender)
                if c=='y':
                    pb.gender=input("Enter the gender :  ")
                    print (pb.gender)
                print
                pickle.dump(pb,file2)
            else:
                pickle.dump(pb,file2)
    except EOFError:
        pass
        file1.close()
        file2.close()
        os.remove("player.dat")
        os.rename("ptemp.dat","player.dat")
    except IOError:
        print("FILE DOES NOT EXIST")
        print

def pSearch():
    try:
        file=open("player.dat","rb")
        x=int(input("ENTER THE REGISTRATION NUMBER TO BE SEARCHED :  "))
        print
        found=0
        while True:
              pb=pickle.load(file)
              if pb.pno==x :
                 pb.poutput()
                 found=1
    except EOFError:
        if found==0:
            print("REGISTRATION NUMBER NOT FOUND ")
            print
            pass
            file.close()
    except IOError:
        print (" FILE DOES NOT EXIST ")
        print

def playgame():
    print
    print ("Enter the category")
    print
    print ("1. Sports")
    print
    print( "2. Current Affairs")
    print
    print( "3. History")
    print
    print ("4. Politics")
    print
    print( "5. maths")
    print
    print ("6. Science ")
    print
    print ("7. mental ability")
    print
    print ("8. rapid fire")
    print
    c=int(raw_input("Enter category :  "))
    print
    l=[]
    try:
        file=open("question.dat","rb")
        found=0
        while True:
              ob=pickle.load(file)
              if ob.category==c:
                 l.append(ob)
                 found=1
    except EOFError:
        if found==0:
            print("QUESTION NUMBER NOT FOUND")
            print
            pass
            file.close()
    except IOError:
        print (" FILE DOES NOT EXIST ")
    s=0
    for i in range(len(l)):
        ob=l[i]
        print 
        print (ob.qno)
        print (ob.question)
        for z in ob.options:
            print (ob.options[z])
        x=input("ENTER YOUR ANSWER : ")
        if x.upper()==ob.answer.upper():
            print
            print ('#'*166)
            print
            print (" " *70 , "CORRECT ANSWER IS :  ",ob.answer)
            print
            print ('^'*166)
            print
            print ("EXPLANATION IS: ")
            print
            s=s+4
        else:
            match=0
            for y in ob.options:
                if ob.options[y].upper()==x.upper():
                    match=1
            if match==0:
                print ('!'*166)
                print
                print (" " *70 ,"Invalid input ")
            else:
                print ('!'*166)
                print
                print (" " *70 ,"Wrong answer ")            
            print
            print ('='*166)
            print
            print (" " *70 , "CORRECT ANSWER IS :  ",ob.answer)
            print
            print ('^'*166)
            print
            print ("EXPLANATION IS: ")
            print (ob.explanation)
            print
            s=s-1
    return s
                 
    
while True:
    print
    print ("*"*166)
    print
    print (" "*80 ,"MAIN MENU")
    print
    print ("*"*166)
    print ("1. Question Bank")
    print
    print ("2. Player")
    print
    choice=int(input("ENTER YOUR CHOICE :  "))
    print
    if choice==1:
        print
        print ("QUESTION BANK")
        print
        print(" 1.ADD QUESTIONS")
        print
        print(" 2.DISPLAY ALL RECORDS")
        print
        print(" 3.DELETE A RECORDS")
        print
        print(" 4.MODIFY A RECORD")
        print
        print(" 5.SEARCH A RECORD")
        print
        print("ANY OTHER NUMBER TO EXIT")
        print
        ch=int(input("ENTER YOUR CHOICE :  "))
        print
        if ch==1:
            sAdd()
        elif ch==2:
            sDisplay()
        elif ch==3:
            sDelete()
        elif ch==4:
            sModify()
        elif ch==5: 
           sSearch()
        else:
            exit()
    elif choice==2:
        print
        print(" PLAYER ")
        print
        print(" 1.PLAY GAME")
        print
        print(" 2.VIEW OLD SCORE")
        print
        print(" 3.DISPLAY ALL RECORDS")
        print
        print(" 4.MODIFY A RECORD")
        print
        qp=int(input("ENTER YOUR CHOICE :  "))
        print
        if qp==1:
            pAdd()
        elif qp==2:
            pSearch()
        elif qp==3:
            pDisplay()
        elif qp==4:
            pModify()
        else:
            exit()
    else:
        exit()
