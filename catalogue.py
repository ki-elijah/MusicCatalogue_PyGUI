from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('catalog.db')

#functions reponsible for the buttons actions, these functions are the commands for the buttons
def populate_list():
#so that the list only shows the data in the database and it does not repeat itself even if its called many times
    song_list.delete(0, END)
    for row in db.fetch():
        song_list.insert(END, row)

def add_item():
    #this if condition is to enable us not to add empty data into the database
    if song_text.get() == '' or artist_text.get() == '' or biography_text.get() == '' or genre_text.get() == '':
        messagebox.showerror('Recquired Fields', 'Please fill in all the fields')
        return
    db.insert(song_text.get(), artist_text.get(), biography_text.get(), genre_text.get())
    song_list.delete(0, END)
    song_list.insert(END, (song_text.get(), artist_text.get(), biography_text.get(), genre_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    try:
        global selected_item
        index = song_list.curselection()[0]
        selected_item = song_list.get(index)

        song_entry.delete(0, END)
        song_entry.insert(END, selected_item[1])
        artist_entry.delete(0, END)
        artist_entry.insert(END, selected_item[2])
        biography_entry.delete(0, END)
        biography_entry.insert(END, selected_item[3])
        genre_entry.delete(0, END)
        genre_entry.insert(END, selected_item[4])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()

def update_item():
    db.update(selected_item[0], song_text.get(), artist_text.get(), biography_text.get(), genre_text.get())
    populate_list()

def clear_text():
    song_entry.delete(0, END)
    artist_entry.delete(0, END)
    biography_entry.delete(0, END)
    genre_entry.delete(0, END)

#creating a window
app = Tk()

#Artist Name
artist_text = StringVar()
artist_label = Label(app, text='Artist Name', pady = 20)
artist_label.grid(row=0, column=0, sticky=W)
artist_entry = Entry(app, textvariable=artist_text)
artist_entry.grid(row=0, column=1)

#Artist Biography
biography_text = StringVar()
biography_label = Label(app, text='Artist Biography')
biography_label.grid(row=0, column=2, sticky=W)
biography_entry = Entry(app, textvariable=biography_text)
biography_entry.grid(row=0, column=3)

#song name
song_text = StringVar()
song_label = Label(app, text='Song')
song_label.grid(row=1, column=0, sticky=W)
song_entry = Entry(app, textvariable=song_text)
song_entry.grid(row=1, column=1)

#song genre
genre_text = StringVar()
genre_label = Label(app, text='Song Genre')
genre_label.grid(row=1, column=2, sticky=W)
genre_entry = Entry(app, textvariable=genre_text)
genre_entry.grid(row=1, column=3)

#Song List (Listbox)
song_list = Listbox(app, height=15, width=80, border=0)
song_list.grid(row=3, column=0, rowspan=6, columnspan=3, pady=20, padx=20) 

#Creating a scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

#Setting scrollbar to listbox
song_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=song_list.yview)

#Bind Select
song_list.bind('<<ListboxSelect>>', select_item)

#Buttons
add_btn = Button(app, text='Add Song', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove Song', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Song', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Text', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Music Catalogue')
app.geometry('700x420')

# Populating data into the listbox
populate_list()

app.mainloop()