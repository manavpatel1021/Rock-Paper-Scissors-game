from tkinter import * 
import random   

screen = Tk()

l1= ["Rock", "Paper" , "Seissor"]

userchoice_var = StringVar()
compchoice_var = StringVar()
result_var = StringVar()

u_score = IntVar()
c_score = IntVar()

user_score = 0
comp_score = 0

def mylogic(userchoice):
    global user_score , comp_score , result_var
    computer_choice = random.choice(l1)

    userchoice_var.set(userchoice)
    compchoice_var.set(computer_choice)


    if computer_choice == userchoice:
        result_var.set("tie")

    elif computer_choice=="Rock" and userchoice == "Paper":
        result_var.set('user won')
        user_score+=1
    
    elif computer_choice=="Rock" and userchoice == "Seissor":
        result_var.set("computer won")
        comp_score+=1

    elif computer_choice=="Paper" and userchoice == "Rock":
        result_var.set("computer won")
        comp_score+=1

    elif computer_choice=="Paper" and userchoice == "Seissor":
        result_var.set("user won")
        user_score+=1

    elif computer_choice=="Seissor" and userchoice == "Rock":
        result_var.set("user won")
        user_score+=1
    
    elif computer_choice=="Seissor" and userchoice == "Paper":
        result_var.set("computer won")
        comp_score+=1

    print(userchoice)
    print(computer_choice)
    u_score.set(user_score)
    c_score.set(comp_score)


screen.title("Rock Paper Seissor")

screen.geometry("520x500")

#---------------------> tkinter design
lbl_tittle = Label(screen,text="ROCK PAPER SEISSOR" , fg="red" , font=('arial',20,'bold') )
lbl_tittle.place(x=100 ,y = 30)

btn_rock = Button(screen, text="Rock" , bg = "black" , fg="white", font=('arial',12,'bold') , activebackground="red" , activeforeground="white", command=lambda : mylogic("Rock"))
btn_rock.place(x = 50, y = 120)

btn_paper = Button(screen, text="Paper" , bg = "black" , fg="white", font=('arial',12,'bold'), activebackground="red" , activeforeground="white",command=lambda : mylogic("Paper"))
btn_paper.place(x = 190, y = 120)

btn_seissor = Button(screen, text="Seissor" , bg = "black" , fg="white", font=('arial',12,'bold'), activebackground="red", activeforeground="white",command=lambda : mylogic("Seissor"))
btn_seissor.place(x = 340, y = 120)

#---------------->begin: user section

lbl_userdisplay = Label(screen, text="USER : " , font=('arial', 12 , 'bold'))
lbl_userdisplay.place(x = 50 , y = 280)

lbl_userdisplaychoice = Label(screen,textvariable=userchoice_var , font=('arial', 12 , 'bold'))
lbl_userdisplaychoice.place(x = 200 , y = 280)

lbl_userscoredisplay = Label(screen, textvariable=u_score , font=('arial', 12 , 'bold'))
lbl_userscoredisplay.place(x = 350 , y = 280)

#-------->end : user section

#----------->begin:computer section

lbl_computerdisplay = Label(screen, text="COMPUTER : " , font=('arial', 12 , 'bold'))
lbl_computerdisplay.place(x = 50 , y = 350)

lbl_computerdisplaychoice = Label(screen, textvariable=compchoice_var , font=('arial', 12 , 'bold'))
lbl_computerdisplaychoice.place(x = 200 , y = 350)

lbl_computerscoredisplay = Label(screen, textvariable=c_score , font=('arial', 12 , 'bold'))
lbl_computerscoredisplay.place(x = 350 , y = 350)

#------------> end :user section

btn_result = Button(screen, textvariable=result_var , font=('arial',12 , 'bold'),width=48,fg="blue")
btn_result.place(x=10 , y = 390)


screen.mainloop()