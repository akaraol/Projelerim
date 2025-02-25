from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog


current_volume = float (0.5)


#Functions

def play_song(): 
  filename = filedialog.askopenfilename(initialdir ="C:/", title =("Please Select a File"))
  current_song = filename
  song_title = filename.split("/")
  song_title = song_title[-1]
  print (song_title)



  try:
    mixer.init()
    mixer.music.load(current_song)
    mixer.music.set_volume(current_volume)
    mixer.music.play()
    song_title_label.config(fg="green", text="Now Playing: " + str (song_title) )
    volume_label.config(fg="green", text="Volume: " + str (current_volume) )
  except Exception as e:
    print(e)
    song_title_label.config(fg ="red", text = ("error playing track"))




#Reducing Volume
def reduce_volume():
  try:
    global current_volume
    if current_volume <=0:
      volume_label.config(fg = "red" , text ="Volume: muted")
      return
    current_volume = current_volume - float(0.1)
    current_volume = round(current_volume, 1)
    mixer.music.set_volume(current_volume)
    volume_label.config(fg="green" , text="Volume: " +str(current_volume) )
  except Exception as e:
    print(e)
    song_title_label.config(fg="red", text="Track hasn't been selected yet!")

#Increasing Volume

def increase_volume():
  try:
    global current_volume
    if current_volume >=1:
      volume_label.config(fg = "green" , text ="Volume: max")
      return
    current_volume = current_volume + float(0.1)
    current_volume = round(current_volume, 1)
    mixer.music.set_volume(current_volume)
    volume_label.config(fg="green" , text="Volume: " +str(current_volume) )
  except Exception as e:
    print(e)
    song_title_label.config(fg="red", text="Track hasn't been selected yet!") 




#pause and resume

def pause():
  try:
    mixer.music.pause()
  except Exception as e:
    print(e)
    song_title_label.config(fg="red", text="Track hasn't been selected.")  


def resume():
  try:
    mixer.music.unpause()
  except Exception as e:
    print(e)
    song_title_label.config(fg="red", text="Track hasn't been selected.") 









#Main Screen
master = Tk()
master.title ("Beskan's Music Player")




#Labels
Label(master, text="Music Player ( ͡° ͜ʖ ͡°)", font=("Times New Roman", 20 ), bg="#191414", fg="#1DB954").grid(sticky="N", row = 0, padx =120, pady = 40)

Label(master, text="Please Select a Track", font=("Calibri", 12 ), fg="blue").grid(sticky="N", row = 1)

Label(master, text="Volume", font=("Calibri", 12 ), fg="red").grid(sticky="N", row = 4)

song_title_label = Label (master, font =("Times New Roman", 12) )
song_title_label.grid(sticky="N", row = 3)
volume_label = Label(master, font=("Times New Roman",12))
volume_label.grid(sticky ="N" , row = 5)




#Buttons

Button (master, text="Select Song", font = ("Times New Roman", 12), command = play_song).grid(row = 2, sticky="N")
Button (master, text="Pause", font=("Times New Roman", 12),command = pause).grid(row = 3, sticky ="E")

Button (master, text="Resume", font=("Times New Roman", 12), command = resume).grid(row = 3, sticky ="W")

Button (master, text="+", font=("Times New Roman", 12), width = 5, command = increase_volume).grid(row = 5, sticky ="E")

Button (master, text="-", font=("Times New Roman", 12), width = 5, command = reduce_volume).grid(row = 5, sticky ="W")
master.mainloop()





 