import tkinter
from tkinter import *
root = Tk()
root.title("Grade Calculator")
root.geometry("500x400")

def calculate_grade():
    try:
        python_marks=int(pythonentry.get())
        WT_marks=int(webTechnology_value_entry.get())
        java_marks=int(JavaProgramming_value_entry.get())

        total = (python_marks+WT_marks+java_marks)
        Label(root,text=total,font="arial 15 bold ").place(x=250,y=170)

        average = int((total/3))
        Label(root,text=average,font="arial 15 bold ").place(x=250,y=210)
        if average >100 :
            grade="Enter valid marks !!"
        elif average>=80 and average<=100:
            grade="PASS - A GRADE"
        elif average>=60 and average<80:
             grade="PASS - B GRADE"
        elif average>40 and average<60:
            grade="PASS - C GRADE"
        else:  
            grade="FAIL !!" 

        Label(text=grade,font="arial 15 bold ").place(x=250,y=250)   
    except ValueError:
     error=Label(text="Invalid Input !!",font="arial 12").place(x=250,y=160)

sub1= Label(root,text="Python : ",font="arial 10")
sub2= Label(root,text="Web Technology : ",font="arial 10")
sub3= Label(root,text="Java Programming : ",font="arial 10")
Total= Label(root,text="Total : ",font="arial 10")
avg= Label(root,text="Average : ",font="arial 10")
Grade= Label(root,text="Grade : ",font="arial 10")

sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
Total.place(x=50,y=170)
avg.place(x=50,y=210)
Grade.place(x=50,y=250)

pythonvalue = StringVar()
webTechnology_value = StringVar()
JavaProgramming_value =  StringVar()

pythonentry = Entry(root,textvariable=pythonvalue,font="arial 15",width=15) 
webTechnology_value_entry = Entry(root,textvariable=webTechnology_value ,font="arial 15",width=15)
JavaProgramming_value_entry = Entry(root,textvariable=JavaProgramming_value,font="arial 15",width=15)
pythonentry.place(x=250,y=20)
webTechnology_value_entry.place(x=250,y=70)
JavaProgramming_value_entry.place(x=250,y=120)

Button(text="Calculate", font="arial 15",background="pink",bd=10,command=lambda:calculate_grade()).place(x=50,y=300)
Button(text="Exit", font="arial 15",background="pink",width=8,bd=10,command=lambda:exit()).place(x=350,y=300)

root.mainloop()