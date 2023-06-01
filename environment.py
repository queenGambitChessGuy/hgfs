from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import time
import webbrowser
import streamlit as st

root = Tk()
root.config(bg="white")
root.title("Environment")
root.geometry("910x750")



close = ImageTk.PhotoImage(Image.open("close.jpg"))
next_img = ImageTk.PhotoImage(Image.open("next.jpg"))
prev_img = ImageTk.PhotoImage(Image.open("previous.jpg"))
dpsmisLogo = ImageTk.PhotoImage(Image.open("logo.jpg"))
info_corner = ImageTk.PhotoImage(Image.open("information_corner.jpg"))
event_corner = ImageTk.PhotoImage(Image.open("event_corner.jpg"))
dpsmis = ImageTk.PhotoImage(Image.open("dpsmis.jpg"))
dot = ImageTk.PhotoImage(Image.open("dot.jpg"))
news = ImageTk.PhotoImage(Image.open("news.jpg"))
back = ImageTk.PhotoImage(Image.open("back.png"))
env1 = ImageTk.PhotoImage(Image.open("env1.jpg"))
env2 = ImageTk.PhotoImage(Image.open("env2.png"))
tree1 = ImageTk.PhotoImage(Image.open("tree1.jpg"))
tree2 = ImageTk.PhotoImage(Image.open("tree2.jpg"))
env_corner = ImageTk.PhotoImage(Image.open("env_corner.jpg"))
nintendo = ImageTk.PhotoImage(Image.open("nintendo.jpg"))


dpsmisLogo_image = Label(root, image=dpsmisLogo, bg="white")
dpsmisLogo_image.place(relx=0.5, rely=0.375, anchor=CENTER)

tree1_img = Label(root, image=tree1, bg="white")
tree1_img.place(relx=0.2, rely=0.375, anchor=CENTER)

tree2_img = Label(root, image=tree2, bg="green")
tree2_img.place(relx=0.8, rely=0.375, anchor=CENTER)

def hyperlink1():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/samirfaizal/DynamicFolder/2022_23/Event%20Corner/Awareness%20Drive%20of%20Environment%20Club%202022.htm")

def hyperlink11():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/samirfaizal/DynamicFolder/2022_23/Information%20Corner/Class%20I_XII_Online%20Art%20Competition%20on%20World%20Environment%20Day_2022.htm")
    
def hyperlink2():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/emily/DynamicFolder/2022_2023/Events%20corner/classVIII_seminar_health_2022.htm")
    
def hyperlink22():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/emily/DynamicFolder/2022_2023/Information%20Corner/Class_IXandX_Environment_Quiz_2022_23.htm")
    
def hyperlink3():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/emily/DynamicFolder/2022_2023/Events%20corner/Environmental_club_interclub_quiz_competition_2022.htm")
    
def hyperlink33():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/samirfaizal/DynamicFolder/2022_23/Information%20Corner/DPS_MIS%20Environment%20Club_2022_23.htm")
    
def hyperlink44():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/UserSpace/UserName/samirfaizal/DynamicFolder/2021_22/Information%20Corner/Class%20III-V%20World%20Environment%20Day%20Junk%20Art%20Competition%20-%202021-22.htm")
    
def hyperlink55():
    webbrowser.open("https://www.dpsmisdoha.com/DPSDoha/Userform/News/News.asp?ccode=6566&frm=I")

def game_hyper_link():
    webbrowser.open("https://scratch.mit.edu/projects/812420845/")

def go_back_from_minigame():
    global big_environment_information_corner_btn
    global big_minigame_corner
    global prev_env_btn
    global next_env_btn
    global rules_title
    global rules
    global minigame_link
    global minigame_title
    global nintendo_img

    close_button.config(command=close_welcomedpsmis)
    big_environment_information_corner_btn.place(relx=0.25, rely=0.325, anchor=CENTER)
    big_minigame_corner.place(relx=0.75, rely=0.325, anchor=CENTER)
    environment_corner_img.place(relx=0.25, rely=0.7, anchor=CENTER)
    nintendo_img.place(relx=0.75, rely=0.7, anchor=CENTER)
    
    next_env_btn.place(relx=0.9, rely=0.96, anchor=CENTER)
    prev_env_btn.place(relx=0.1, rely=0.96, anchor=CENTER)
    
    title1.config(fg="darkgreen")
    title1["text"] = "DPS Modern Indian School"
    title1.place(relx=0.5, rely=0.05, anchor=CENTER)
    
    rules_title.pack()
    rules_title.pack_forget()
    rules.pack()
    rules.pack_forget()
    minigame_link.pack()
    minigame_link.pack_forget()
    minigame_title.pack()
    minigame_title.pack_forget()


minigame_title = Label(root, text="Minigame Link:", font=("Calibri", 20, "bold"), fg="black", bg="white")
def minigame():
    global big_environment_information_corner_btn
    global prev_env_btn
    global next_env_btn
    global what_env_is_label_ans
    global what_env_is_label_ques
    global types_of_ecosystem_ques
    global types_of_ecosystem_ans
    global env1_img
    global env2_img
    global environment_corner_img
    global big_minigame_corner
    global rules_title
    global rules
    global minigame_link
    global nintendo_img
    
    
    
    big_environment_information_corner_btn.pack()
    big_environment_information_corner_btn.pack_forget()
    environment_corner_img.pack()
    environment_corner_img.pack_forget()
    big_minigame_corner.pack()
    big_minigame_corner.pack_forget()
    nintendo_img.pack()
    nintendo_img.pack_forget()
    
    prev_env_btn.pack()
    prev_env_btn.pack_forget()
    
    next_env_btn.pack()
    next_env_btn.pack_forget()
    
    close_button.config(command=go_back_from_minigame)
    
    title1.config(fg="black")
    title1["text"] = "DPS Modern Indian School\nEnvironment Minigame"
    title1.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    rules_title = Label(root, text="Rules of Minigame:", font=("Calibri", 20, "bold"), fg="black", bg="white")
    rules_title.place(relx=0.125, rely=0.25, anchor=CENTER)
    
    rules = Label(root, justify="left", font=("Calibri", 15, "bold"), fg="black", bg="white", text="1. Use arrow keys(left and right) to control bowl.\n2. Collect the item which does not harm the environment to get points.\n3. If you collect something harmful for the environment you will lose points.\n4. As a bonus feature, there will appear a field around the items which gives you bonus points for \n    correct and penalty for wrong.\n5. There is 10% chance to get the bonus.")
    rules.place(relx=0.46, rely=0.37, anchor=CENTER)
    
    minigame_title.place(relx=0.1, rely=0.6, anchor=CENTER)
    
    minigame_link = Button(root, relief=FLAT, command=game_hyper_link, text="https://scratch.mit.edu/projects/812420845/", font=("calibri", 15, "underline"), fg="blue", bg="white")
    minigame_link.place(relx=0.215, rely=0.65, anchor=CENTER)
    
def go_back_from_env():
    global big_environment_information_corner_btn
    global prev_env_btn
    global next_env_btn
    global what_env_is_label_ans
    global what_env_is_label_ques
    global types_of_ecosystem_ques
    global types_of_ecosystem_ans
    global env1_img
    global env2_img
    global environment_corner_img
    global big_minigame_corner
    global nintendo_img
    
    close_button.config(command=close_welcomedpsmis)
    big_environment_information_corner_btn.place(relx=0.25, rely=0.325, anchor=CENTER)
    big_minigame_corner.place(relx=0.75, rely=0.325, anchor=CENTER)
    environment_corner_img.place(relx=0.25, rely=0.7, anchor=CENTER)
    nintendo_img.place(relx=0.75, rely=0.7, anchor=CENTER)
    what_env_is_label_ans.pack()
    what_env_is_label_ans.pack_forget()
    what_env_is_label_ques.pack()
    what_env_is_label_ques.pack_forget()
    types_of_ecosystem_ques.pack()
    types_of_ecosystem_ques.pack_forget()
    types_of_ecosystem_ans.pack()
    types_of_ecosystem_ans.pack_forget()
    env1_img.pack()
    env1_img.pack_forget()
    env2_img.pack()
    env2_img.pack_forget()
    
    next_env_btn.place(relx=0.9, rely=0.96, anchor=CENTER)
    prev_env_btn.place(relx=0.1, rely=0.96, anchor=CENTER)
    
    
    

def env_info():
    global big_environment_information_corner_btn
    global prev_env_btn
    global next_env_btn
    global what_env_is_label_ans
    global what_env_is_label_ques
    global types_of_ecosystem_ques
    global types_of_ecosystem_ans
    global env1_img
    global env2_img
    global environment_corner_img
    global big_minigame_corner
    global nintendo_img
    
    
    big_environment_information_corner_btn.pack()
    big_environment_information_corner_btn.pack_forget()
    environment_corner_img.pack()
    environment_corner_img.pack_forget()
    big_minigame_corner.pack()
    big_minigame_corner.pack_forget()
    nintendo_img.pack()
    nintendo_img.pack_forget()
    
    prev_env_btn.pack()
    prev_env_btn.pack_forget()
    
    next_env_btn.pack()
    next_env_btn.pack_forget()
    
    close_button.config(command=go_back_from_env)
    
    what_env_is_label_ques = Label(root, text="What is Environment?", fg="black", bg="white", font=("Calibri", 20, "bold"))
    what_env_is_label_ques.place(relx=0.145, rely=0.2, anchor=CENTER)
    
    what_env_is_label_ans = Label(root, justify="left", text="An Environment is everything that is around us, which includes both living and nonliving things such as soil, water, animals and plants, which adapt themselves to their surroundings. It is nature’s gift that helps in nourishing life on Earth.\nThe environment plays an important role in the existence of life on the planet earth. The word Environment is derived from the French word “Environ” which means “surrounding.” An ecosystem refers to all the living and non-living things present in the environment and it is a foundation of the Biosphere, which determines the health of the entire planet earth.", font=("Calibri", 15), fg="black", bg="white", wraplength=900)
    what_env_is_label_ans.place(relx=0.5, rely=0.34, anchor=CENTER)
    
    types_of_ecosystem_ques = Label(root, text="Types of Ecosystem", fg="black", bg="white", font=("Calibri", 20, "bold"))
    types_of_ecosystem_ques.place(relx=0.135, rely=0.475, anchor=CENTER)
    
    types_of_ecosystem_ans = Label(root, justify="left", font=("Calibri", 15), fg="black", bg="white", wraplength=900, text="There are two main types of ecosystems. Listed below are the types and examples of the ecosystem.\n1. Natural ecosystem – It is a naturally produced biological environment found in nature. It includes deserts, forests, grasslands, lakes, mountains, ponds, rivers, oceans, etc.\n2. Artificial ecosystem – It is an artificial environment which is created and maintained by man. It includes an aquarium, crop fields, gardens, parks, zoo, etc.")
    types_of_ecosystem_ans.place(relx=0.5, rely=0.58, anchor=CENTER)
    
    env1_img = Label(root, image=env1, bg="white")
    env1_img.place(relx=0.25, rely=0.8, anchor=CENTER)
    
    env2_img = Label(root, image=env2, bg="white")
    env2_img.place(relx=0.75, rely=0.8, anchor=CENTER)
    
def next_env():
    global big_environment_information_corner_btn
    global environment_corner_img
    global big_minigame_corner
    global nintendo_img
    
    big_information_button.pack()
    big_information_button.pack_forget()
    
    big_information_image.pack()
    big_information_image.pack_forget()
    
    big_events_button.pack()
    big_events_button.pack_forget()
    
    big_events_image.pack()
    big_events_image.pack_forget()
    
    big_environment_information_corner_btn = Button(root, text="Environment\nInformation\nCorner", font=("calibri", 40, "bold"), fg="black", bg="white", relief=RIDGE, command=env_info)
    big_environment_information_corner_btn.place(relx=0.25, rely=0.325, anchor=CENTER)
    
    big_minigame_corner = Button(root, command=minigame, text="Minigame\nCorner", font=("calibri", 40, "bold"), fg="black", bg="white", relief=RIDGE)
    big_minigame_corner.place(relx=0.75, rely=0.325, anchor=CENTER)
    
    environment_corner_img = Label(root, image=env_corner, bg="white")
    environment_corner_img.place(relx=0.25, rely=0.7, anchor=CENTER)
    
    nintendo_img = Label(root, image=nintendo, bg="white")
    nintendo_img.place(relx=0.75, rely=0.7, anchor=CENTER)
    
def prev_env():
    global big_environment_information_corner_btn
    global environment_corner_img
    global big_minigame_corner
    global nintendo_img
    
    big_events_button.place(relx=0.75, rely=0.325, anchor=CENTER)
    
    big_events_image.place(relx=0.75, rely=0.735, anchor=CENTER)
    
    big_information_image.place(relx=0.25, rely=0.7, anchor=CENTER)
    
    big_information_button.place(relx=0.25, rely=0.325, anchor=CENTER)
    
    big_environment_information_corner_btn.pack()
    big_environment_information_corner_btn.pack_forget()
    environment_corner_img.pack()
    environment_corner_img.pack_forget()
    big_minigame_corner.pack()
    big_minigame_corner.pack_forget()
    nintendo_img.pack()
    nintendo_img.pack_forget()
    
    

def close_events_corner():
    global big_information_button
    global environment_hyperlink1
    global environment_hyperlink2
    global environment_hyperlink3
    global dot_img1
    global dot_img2
    global dot_img3
    global big_information_image
    global big_events_button
    global big_events_image
    global environment_hyperlink11
    global environment_hyperlink22
    global environment_hyperlink33
    global environment_hyperlink44
    global environment_hyperlink55
    global dot_img11
    global dot_img22
    global dot_img33
    global dot_img44
    global dot_img55
    global new_img11
    global new_img22
    global new_img1
    global prev_env_btn
    global next_env_btn
    
    close_button.config(command=close_welcomedpsmis)
    title1["text"] = "DPS Modern Indian School"
    title1.config(fg="darkgreen")
    title1.place(relx=0.5, rely=0.05, anchor=CENTER)
    
    next_env_btn.place(relx=0.9, rely=0.96, anchor=CENTER)
    prev_env_btn.place(relx=0.1, rely=0.96, anchor=CENTER)
    
    try:
        environment_hyperlink1.pack()
        environment_hyperlink1.pack_forget()
        environment_hyperlink2.pack()
        environment_hyperlink2.pack_forget()
        environment_hyperlink3.pack()
        environment_hyperlink3.pack_forget()
        dot_img1.pack()
        dot_img1.pack_forget()
        dot_img2.pack()
        dot_img2.pack_forget()
        dot_img3.pack()
        dot_img3.pack_forget()
        new_img1.pack()
        new_img1.pack_forget()
        
        dot_img11.pack()
        dot_img11.pack_forget()
        dot_img22.pack()
        dot_img22.pack_forget()
        dot_img33.pack()
        dot_img33.pack_forget()
        dot_img44.pack()
        dot_img44.pack_forget()
        dot_img55.pack()
        dot_img55.pack_forget()
        new_img11.pack()
        new_img11.pack_forget()
        new_img22.pack()
        new_img22.pack_forget()
        environment_hyperlink11.pack()
        environment_hyperlink11.pack_forget()
        environment_hyperlink22.pack()
        environment_hyperlink22.pack_forget()
        environment_hyperlink33.pack()
        environment_hyperlink33.pack_forget()
        environment_hyperlink44.pack()
        environment_hyperlink44.pack_forget()
        environment_hyperlink55.pack()
        environment_hyperlink55.pack_forget()
    except:
        try:
            dot_img11.pack()
            dot_img11.pack_forget()
            dot_img22.pack()
            dot_img22.pack_forget()
            dot_img33.pack()
            dot_img33.pack_forget()
            dot_img44.pack()
            dot_img44.pack_forget()
            dot_img55.pack()
            dot_img55.pack_forget()
            new_img11.pack()
            new_img11.pack_forget()
            new_img22.pack()
            new_img22.pack_forget()
            environment_hyperlink11.pack()
            environment_hyperlink11.pack_forget()
            environment_hyperlink22.pack()
            environment_hyperlink22.pack_forget()
            environment_hyperlink33.pack()
            environment_hyperlink33.pack_forget()
            environment_hyperlink44.pack()
            environment_hyperlink44.pack_forget()
            environment_hyperlink55.pack()
            environment_hyperlink55.pack_forget()
        except:
            print("")
            
    big_events_button.place(relx=0.75, rely=0.325, anchor=CENTER)
    big_events_image.place(relx=0.75, rely=0.735, anchor=CENTER)
    big_information_image.place(relx=0.25, rely=0.7, anchor=CENTER)
    big_information_button.place(relx=0.25, rely=0.325, anchor=CENTER)
    

def events_corner():
    global environment_hyperlink1
    global environment_hyperlink2
    global environment_hyperlink3
    global dot_img1
    global dot_img2
    global dot_img3
    global new_img1
    global prev_env_btn
    global next_env_btn
    close_button.config(command=close_events_corner)
    
    prev_env_btn.pack()
    prev_env_btn.pack_forget()
    
    next_env_btn.pack()
    next_env_btn.pack_forget()
    
    big_information_button.pack()
    big_information_button.pack_forget()
    
    big_information_image.pack()
    big_information_image.pack_forget()
    
    big_events_button.pack()
    big_events_button.pack_forget()
    
    big_events_image.pack()
    big_events_image.pack_forget()
    
    title1["text"] = "DPS Modern Indian School\nEvents Corner"
    title1.config(fg="black")
    title1.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    environment_hyperlink1 = Button(root, relief=FLAT, text="Awareness Drive of Environment Club 2022", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink1.place(relx=0.1, rely=0.3)
    environment_hyperlink1.config(command=hyperlink1)
    
    environment_hyperlink2 = Button(root, relief=FLAT, text="Environment Club-Seminar on Health,Hygiene and \nHappiness-2022", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink2.place(relx=0.1, rely=0.4)
    environment_hyperlink2.config(command=hyperlink2)
    
    environment_hyperlink3 = Button(root, relief=FLAT, text="Environment Club Conducted Interclub Quiz Competition-2022", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink3.place(relx=0.1, rely=0.55)
    environment_hyperlink3.config(command=hyperlink3)
    
    dot_img1 = Label(root, image=dot, bg="white")
    dot_img1.place(relx=0.1, rely=0.34, anchor=CENTER)
    
    dot_img2 = Label(root, image=dot, bg="white")
    dot_img2.place(relx=0.1, rely=0.44, anchor=CENTER)
    
    dot_img3 = Label(root, image=dot, bg="white")
    dot_img3.place(relx=0.1, rely=0.59, anchor=CENTER)
    
    new_img1 = Label(root, image=news, bg="white")
    new_img1.place(relx=0.63, rely=0.32)
    
def infor_corner():
    global environment_hyperlink11
    global environment_hyperlink22
    global environment_hyperlink33
    global environment_hyperlink44
    global environment_hyperlink55
    global dot_img11
    global dot_img22
    global dot_img33
    global dot_img44
    global dot_img55
    global new_img11
    global new_img22
    global prev_env_btn
    global next_env_btn
    close_button.config(command=close_events_corner)
    
    prev_env_btn.pack()
    prev_env_btn.pack_forget()
    
    next_env_btn.pack()
    next_env_btn.pack_forget()
    
    big_information_button.pack()
    big_information_button.pack_forget()
    
    big_information_image.pack()
    big_information_image.pack_forget()
    
    big_events_button.pack()
    big_events_button.pack_forget()
    
    big_events_image.pack()
    big_events_image.pack_forget()
    
    title1["text"] = "DPS Modern Indian School\nInformation Corner"
    title1.config(fg="black")
    title1.place(relx=0.5, rely=0.1, anchor=CENTER)
    
    environment_hyperlink11 = Button(root, relief=FLAT, text="Class I-XII - Online Art Competition on World Environment \nDay - 2022", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink11.place(relx=0.1, rely=0.3)
    environment_hyperlink11.config(command=hyperlink11)
    
    environment_hyperlink22 = Button(root, relief=FLAT, text="Class IX and X-Environment Quiz-2022-23", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink22.place(relx=0.1, rely=0.45)
    environment_hyperlink22.config(command=hyperlink22)
    
    environment_hyperlink33 = Button(root, relief=FLAT, text="DPS-MIS Environment Club - 2022-23", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink33.place(relx=0.1, rely=0.55)
    environment_hyperlink33.config(command=hyperlink33)
    
    environment_hyperlink44 = Button(root, relief=FLAT, text="Class III-V World Environment Day Junk Art Competition - \n2021-22", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink44.place(relx=0.1, rely=0.65)
    environment_hyperlink44.config(command=hyperlink44)
    
    environment_hyperlink55 = Button(root, relief=FLAT, text="Environment Club Activities: For Classes VI-XII - 2020-21", font=("Calibri", 20, "underline"), fg="blue", bg="white", justify="left")
    environment_hyperlink55.place(relx=0.1, rely=0.8)
    environment_hyperlink55.config(command=hyperlink55)
    
    dot_img11 = Label(root, image=dot, bg="white")
    dot_img11.place(relx=0.1, rely=0.34, anchor=CENTER)
    
    dot_img22 = Label(root, image=dot, bg="white")
    dot_img22.place(relx=0.1, rely=0.49, anchor=CENTER)
    
    dot_img33 = Label(root, image=dot, bg="white")
    dot_img33.place(relx=0.1, rely=0.59, anchor=CENTER)
    
    dot_img44 = Label(root, image=dot, bg="white")
    dot_img44.place(relx=0.1, rely=0.69, anchor=CENTER)
    
    dot_img55 = Label(root, image=dot, bg="white")
    dot_img55.place(relx=0.1, rely=0.84, anchor=CENTER)
    
    new_img11 = Label(root, image=news, bg="white")
    new_img11.place(relx=0.245, rely=0.368)
    
    new_img22 = Label(root, image=news, bg="white")
    new_img22.place(relx=0.61, rely=0.475)

def environmentInfo():
    
    global big_information_button
    global environment_hyperlink1
    global big_information_image
    global big_events_button
    global big_events_image
    global prev_env_btn
    global next_env_btn
    close_button["image"] = back
    dpsmisLogo_image.pack()
    dpsmisLogo_image.pack_forget()
    information_corner_title.pack()
    information_corner_title.pack_forget()
    welcome_dpsmis_title.pack()
    welcome_dpsmis_title.pack_forget()
    welcome_dpsmis.pack()
    welcome_dpsmis.pack_forget()
    tree1_img.pack()
    tree1_img.pack_forget()
    contact.pack()
    contact.pack_forget()
    tree2_img.pack()
    tree2_img.pack_forget()
    read_more_button1.pack()
    read_more_button1.pack_forget()
    read_more_button2.pack()
    read_more_button2.pack_forget()
    title2.pack()
    title2.pack_forget()
    information_corner.pack()
    information_corner.pack_forget()
    close_button.config(command=close_welcomedpsmis)
    
    big_information_button = Button(root, text="Information\nCorner", font=("calibri", 40, "bold"), fg="black", bg="white", relief=RIDGE, command=infor_corner)
    big_information_button.place(relx=0.25, rely=0.325, anchor=CENTER)
    
    big_information_image = Label(root, bg="white", image=info_corner)
    big_information_image.place(relx=0.25, rely=0.7, anchor=CENTER)
    
    big_events_button = Button(root, text="Events\nCorner", font=("calibri", 40, "bold"), fg="black", bg="white", relief=RIDGE, command=events_corner)
    big_events_button.place(relx=0.75, rely=0.325, anchor=CENTER)
    
    big_events_image = Label(root, bg="white", image=event_corner)
    big_events_image.place(relx=0.75, rely=0.735, anchor=CENTER)
    
    next_env_btn = Button(root, image=next_img, bg="white", relief=FLAT, command=next_env)
    next_env_btn.place(relx=0.9, rely=0.96, anchor=CENTER)
    
    prev_env_btn = Button(root, image=prev_img, bg="white", relief=FLAT, command=prev_env)
    prev_env_btn.place(relx=0.1, rely=0.96, anchor=CENTER)
    

major_features_info = Label(root, text="1. 3 blocks (buildings) housing the Administration , Junior, Middle and Senior Schools\n2. Total around 200 classrooms\n3. Naturally lit Labs for Sciences, Maths, Information Technology and the Libraries\n4. Well equipped auditorium for 1000 seating capacity\n5. Indoor swimming pool, gymnasium and badminton courts\n6. Well arranged pathways leading to all utilities\n7. Parking for 300 cars and buses\n8. Large size football ground and athletic track\n9. Energy efficient building and services\n10. Secured WIFI enabled campus\n11. Digital Signage, E Notice Boards and Video enabled announcement system", font=("Calibri", 15), fg="black", bg="white", justify="left")
major_features_title = Label(root, text="The school has the following major features:", font=("Calibri", 20, "bold"), fg="black", bg="white")
dpsmis_label = Label(root, image=dpsmis)

def previous_info():
    
    global dpsmisAreaAndBuildingTitle
    global environment_hyperlink1
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global major_features_title
    global major_features_info
    global dpsmis_label
    
    dpsmisAreaAndBuildingTitle.place(relx=0.12, rely=0.45, anchor=CENTER)
    dpsmisAreaAndBuildingInfo.place(relx=0.5, rely=0.7, anchor=CENTER)
    dpsmisInfo.place(relx=0.5, rely=0.325, anchor=CENTER)
    dpsmisAreaAndBuildingInfo["text"] = "The campus has been thoughtfully designed to create a dynamic environment which triggers learning and facilitates the teaching process. It has been designed to miniscule details and addresses the contemporary needs of the Learners.\n\nThe academic buildings (Block A, Block B and Block C (First Floor and 2nd Floor)) has 158 classrooms. Each room has adequate storage provisions for the entire class. The building is networked and provided with computers.\n\nIn addition to regular classroom, the building has classrooms equipped with Smart Interactive Boards for Senior School and LCD Televisions for Junior School, language rooms, science labs, computer labs, music and dance rooms, staff rooms, art rooms and adequate toilet facilities for boys and girls.\n\nThe building also has one state of art Auditorium and an Olympic Size Swimming Pool. The total area of the academic building is 22,000 sq ft."
    dpsmisInfo["text"] = "The school was established in 2001. In nineteen years, the school has carved a niche for itself and is counted among the best schools in Doha-Qatar. Bettering the best in Academics, Extra-curricular activities and sports, the school has succeeded in bringing out well-rounded personalities-students who are academically bright, physically strong, mentally agile, emotionally balanced, socially committed and spiritually serene."
    dpsmisAreaAndBuildingTitle["text"] = "Area and Building"
    
    
    major_features_info.pack()
    major_features_info.pack_forget()
    major_features_title.pack()
    major_features_title.pack_forget()
    dpsmis_label.pack()
    dpsmis_label.pack_forget()

def next_info():
    
    global major_features_title
    global dpsmisAreaAndBuildingTitle
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global major_features_info
    global environment_hyperlink1
    global dpsmis_label
    
    dpsmisAreaAndBuildingInfo.pack()
    dpsmisAreaAndBuildingTitle.pack()
    dpsmisAreaAndBuildingInfo.pack_forget()
    dpsmisAreaAndBuildingTitle.pack_forget()
    dpsmisInfo.pack()
    dpsmisInfo.pack_forget()
    
    major_features_title.place(relx=0.285, rely=0.25, anchor=CENTER)
    
    major_features_info.place(relx=0.405, rely=0.465, anchor=CENTER)
    
    dpsmis_label.place(relx=0.5, rely=0.8, anchor=CENTER)
    
def dpsmis_read_more():
    global dpsmisAreaAndBuildingTitle
    global environment_hyperlink1
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global next_button
    global prev_button
    global major_features_title
    global major_features_info
    global dpsmisLogo_image
    global dpsmis
    
    
    dpsmisLogo_image.pack()
    dpsmisLogo_image.pack_forget()
    tree1_img.pack()
    tree1_img.pack_forget()
    tree2_img.pack()
    tree2_img.pack_forget()
    information_corner_title.pack()
    information_corner_title.pack_forget()
    welcome_dpsmis_title.pack()
    welcome_dpsmis_title.pack_forget()
    welcome_dpsmis.pack()
    welcome_dpsmis.pack_forget()
    read_more_button1.pack()
    read_more_button1.pack_forget()
    read_more_button2.pack()
    read_more_button2.pack_forget()
    title2.pack()
    title2.pack_forget()
    information_corner.pack()
    information_corner.pack_forget()
    contact.pack()
    contact.pack_forget()
    title1["text"] = "Welcome to\nDPS Modern Indian School"
    title1.config(fg="black")
    title1.place(relx=0.5, rely=0.1, anchor=CENTER)
    close_button.config(command=close_welcomedpsmis)
    close_button["image"] = back
    
    dpsmisInfo = Label(root, text="The school was established in 2001. In nineteen years, the school has carved a niche for itself and is counted among the best schools in Doha-Qatar. Bettering the best in Academics, Extra-curricular activities and sports, the school has succeeded in bringing out well-rounded personalities-students who are academically bright, physically strong, mentally agile, emotionally balanced, socially committed and spiritually serene.", font=("Calibri", 15), fg="black", bg="white", justify="left", wraplength=900)
    dpsmisInfo.place(relx=0.5, rely=0.325, anchor=CENTER)
    
    dpsmisAreaAndBuildingTitle= Label(root, text="Area and Building", font=("Calibri", 20, "bold"), fg="black", bg="white")
    dpsmisAreaAndBuildingTitle.place(relx=0.12, rely=0.45, anchor=CENTER)
    
    dpsmisAreaAndBuildingInfo = Label(root, text="The campus has been thoughtfully designed to create a dynamic environment which triggers learning and facilitates the teaching process. It has been designed to miniscule details and addresses the contemporary needs of the Learners.\n\nThe academic buildings (Block A, Block B and Block C (First Floor and 2nd Floor)) has 158 classrooms. Each room has adequate storage provisions for the entire class. The building is networked and provided with computers.\n\nIn addition to regular classroom, the building has classrooms equipped with Smart Interactive Boards for Senior School and LCD Televisions for Junior School, language rooms, science labs, computer labs, music and dance rooms, staff rooms, art rooms and adequate toilet facilities for boys and girls.\n\nThe building also has one state of art Auditorium and an Olympic Size Swimming Pool. The total area of the academic building is 22,000 sq ft.", font=("Calibri", 15), fg="black", bg="white", justify="left", wraplength=900)
    dpsmisAreaAndBuildingInfo.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    next_button = Button(root, image=next_img, relief=FLAT, bg="white")
    next_button.place(relx=0.9, rely=0.96, anchor=CENTER)
    next_button.config(command=next_info)
    
    prev_button = Button(root, image=prev_img, relief=FLAT, bg="white")
    prev_button.place(relx=0.1, rely=0.96, anchor=CENTER)
    prev_button.config(command=previous_info)

def close_root():
    
    root.destroy()
    
def close_welcomedpsmis():
    global big_information_button
    global dpsmisAreaAndBuildingTitle
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global next_button
    global prev_button
    global major_features_title
    global major_features_info
    global dpsmisLogo_image
    global big_information_image
    global big_events_button
    global big_events_image
    global dpsmis_label
    global prev_env_btn
    global next_env_btn
    global big_environment_information_corner_btn
    global environment_corner_img
    global big_minigame_corner
    global nintendo_img
    
    
    close_button.config(command=close_root)
    close_button["image"] = close
    
    dpsmisLogo_image.place(relx=0.5, rely=0.375, anchor=CENTER)
    tree1_img.place(relx=0.2, rely=0.375, anchor=CENTER)
    tree2_img.place(relx=0.8, rely=0.375, anchor=CENTER)
    
    title1["text"] = "DPS Modern Indian School"
    title1.place(relx=0.5, rely=0.05, anchor=CENTER)
    title2.place(relx=0.5, rely=0.15, anchor=CENTER)
    
    information_corner_title.place(relx=0.8, rely=0.6, anchor=CENTER)
    
    welcome_dpsmis_title.place(relx=0.2, rely=0.6, anchor=CENTER)
    welcome_dpsmis.place(relx=0.2, rely=0.8, anchor=CENTER)
    
    read_more_button1.place(relx=0.2, rely=0.95, anchor=CENTER)
    read_more_button2.place(relx=0.8, rely=0.95, anchor=CENTER)
    
    information_corner.place(relx=0.8, rely=0.8, anchor=CENTER)
    
    title1.config(fg="darkgreen")
    
    contact.place(relx=0.5, rely=0.925, anchor=CENTER)
    
    try:
        next_button.pack()
        next_button.pack_forget()
        prev_button.pack()
        prev_button.pack_forget()
        
        dpsmisInfo.pack()
        dpsmisInfo.pack_forget()
        dpsmisAreaAndBuildingInfo.pack()
        dpsmisAreaAndBuildingInfo.pack_forget()
        dpsmisAreaAndBuildingTitle.pack()
        dpsmisAreaAndBuildingTitle.pack_forget()
        
        major_features_title.pack()
        major_features_title.pack_forget()
        major_features_info.pack()
        major_features_info.pack_forget()
        
        dpsmis_label.pack()
        dpsmis_label.pack_forget()
        
        big_information_button.pack()
        big_information_button.pack_forget()
        
        big_information_image.pack()
        big_information_image.pack_forget()
        
        big_events_button.pack()
        big_events_button.pack_forget()
        
        big_events_image.pack()
        big_events_image.pack_forget()
        
        prev_env_btn.pack()
        prev_env_btn.pack_forget()
        
        next_env_btn.pack()
        next_env_btn.pack_forget()
        
        big_environment_information_corner_btn.pack()
        big_environment_information_corner_btn.pack_forget()
        
        environment_corner_img.pack()
        environment_corner_img.pack_forget()
        
        big_minigame_corner.pack()
        big_minigame_corner.pack_forget()
        
        nintendo_img.pack()
        nintendo_img.pack_forget()
    except:
        try:
            big_information_button.pack()
            big_information_button.pack_forget()
            
            big_information_image.pack()
            big_information_image.pack_forget()
            
            big_events_button.pack()
            big_events_button.pack_forget()
            
            big_events_image.pack()
            big_events_image.pack_forget()
            
            prev_env_btn.pack()
            prev_env_btn.pack_forget()
            
            next_env_btn.pack()
            next_env_btn.pack_forget()
            
            big_environment_information_corner_btn.pack()
            big_environment_information_corner_btn.pack_forget()
            
            environment_corner_img.pack()
            environment_corner_img.pack_forget()
            
            big_minigame_corner.pack()
            big_minigame_corner.pack_forget()
            
            nintendo_img.pack()
            nintendo_img.pack_forget()
        except:
            major_features_title.pack()
            major_features_title.pack_forget()
            major_features_info.pack()
            major_features_info.pack_forget()
            
            dpsmis_label.pack()
            dpsmis_label.pack_forget()
            
    try:
        prev_env_btn.pack()
        prev_env_btn.pack_forget()
        
        next_env_btn.pack()
        next_env_btn.pack_forget()
        
        big_environment_information_corner_btn.pack()
        big_environment_information_corner_btn.pack_forget()
        
        environment_corner_img.pack()
        environment_corner_img.pack_forget()
        
        big_minigame_corner.pack()
        big_minigame_corner.pack_forget()
        
        nintendo_img.pack()
        nintendo_img.pack_forget()
    except:
        print("")

title1 = Label(root, text="DPS Modern Indian School", font=("agency FB", 50, "bold", "underline"), bg="white", fg="darkgreen")
title1.place(relx=0.5, rely=0.05, anchor=CENTER)

title2 = Label(root, text="Environment Club", font=("algerian", 40, "bold", "italic"), bg="white", fg="green")
title2.place(relx=0.5, rely=0.15, anchor=CENTER)

information_corner_title = Label(root, text="Environment \nCorner", font=("calibri", 25, "bold"), bg="white", fg="black", highlightthickness=4, highlightcolor="black", highlightbackground="black", borderwidth=4)
information_corner_title.place(relx=0.8, rely=0.6, anchor=CENTER)

information_corner = Label(root, text="DPS-MIS Envorionment Information and Events Corner. DPS-MIS has won 2nd place in the school debate competion. DPS-MIS Environment Inter-School Tree Planting Competion....", font=("calibri", 15), wraplength=300, fg="black", bg="white")
information_corner.place(relx=0.8, rely=0.8, anchor=CENTER)

welcome_dpsmis_title = Label(root, text="Welcome To \nDPS-MIS", font=("calibri", 25, "bold"), bg="white", fg="black", highlightthickness=4, highlightcolor="black", highlightbackground="black", borderwidth=4)
welcome_dpsmis_title.place(relx=0.2, rely=0.6, anchor=CENTER)

welcome_dpsmis = Label(root, text="The school was established in 2001. In nineteen years, the school has carved a niche for itself and is counted among the best schools in Doha-Qatar. Bettering the best in Academics, Extra-curricular activities.....", bg="white", fg="black", wraplength=300, font=("Calibri", 15))
welcome_dpsmis.place(relx=0.2, rely=0.8, anchor=CENTER)

read_more_button1 = Button(root, text="Read More", font=("calibri", 17, "bold"),fg="white", bg="green", relief=RIDGE, highlightthickness=4, highlightcolor="lightgreen", highlightbackground="lightgreen", borderwidth=2, command=dpsmis_read_more)
read_more_button1.place(relx=0.2, rely=0.95, anchor=CENTER)

read_more_button2 = Button(root, text="Read More", font=("calibri", 17, "bold"),fg="white", bg="green", relief=RIDGE, highlightthickness=4, highlightcolor="lightgreen", highlightbackground="lightgreen", borderwidth=2, command=environmentInfo)
read_more_button2.place(relx=0.8, rely=0.95, anchor=CENTER)

close_button = Button(root, image=close, relief=FLAT, command=close_root, bg="white")
close_button.place(relx=0.925, rely=0.01)

made_by = Label(root, text="Made By\nSahil P. Chogle\nHouse: Lily\nAdm No.:11135\nClass:VI-G", font=("Agency FB", 15, "italic", "underline"), fg="black", bg="white")
made_by.place(relx=0.05, rely=0.075, anchor=CENTER)

contact = Label(root, text="Contact:\nprashant.chogle@gmail.com\n55432961",  font=("Agency FB", 20, "italic", "underline"), fg="black", bg="white", highlightthickness=2, highlightcolor="red", highlightbackground="red", borderwidth=2)
contact.place(relx=0.5, rely=0.925, anchor=CENTER)

root.mainloop()