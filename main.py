from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title("Music Player")
root.geometry("500x350+400+200")
# root.iconbitmap('./assets/as2.png')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='./assets/icon.png'))
# root.overrideredirect(True)
    
Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=0)
Grid.rowconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=0)


# Initialize Pygame Mixer
pygame.mixer.init()

# Grab Song Length
def play_time():
    if stopped:
        return
    # Elapsed Time
    current_time = int(pygame.mixer.music.get_pos() // 1000)
    global song_len1
    # Get Song Title From List
    song = song_box.get(ACTIVE)
    # Add Directory Structure And mp3 To The Song
    song = f"D:/MusicPlayer/audio/{song}.mp3"
    # Load Song with Mutagen
    song_mut = MP3(song)
    song_len1 = int(song_mut.info.length)
    # Get Song Length
    # global song_len
    # Time Format
    song_len = time.strftime("%M:%S", time.gmtime(song_len1))

    if int(slider.get()) == song_len1:
        status_bar["text"] = f"{song_len} / {song_len}"
    elif paused:
        pass
    elif int(slider.get()) == (current_time + 1):
        # slider hasn't been moved
        # Update Slider Postion
        slider["to"] = song_len1
        slider["value"] = current_time + 1
    else:
        # slider has been moved
        # Update Slider Postion
        slider["to"] = song_len1
        slider["value"] = slider.get()
        # Output Time in Status Bar
        slider_time = time.strftime("%M:%S", time.gmtime(int(slider.get())))
        song_len = song_len1 - int(slider.get())
        # Time Format
        song_len = time.strftime("%M:%S", time.gmtime(song_len))
        status_bar["text"] = f"{slider_time} / {song_len}"

        # Move this thing along by one second
        slider["value"] = int(slider.get())+1

    # Get Current Song

    # Update Slider Postion Value
    # slider.config(value=current_time)
    # current_song=song_box.curselection()
    current_time = time.strftime("%M:%S", time.gmtime(current_time))
    # Temp Label to get data
    # slider_l.config(text=f'Slider:{int(slider.get())}  Song:{current_time}')

    # Output Time in Status Bar
    # status_bar.config(text=f'{current_time} / {song_len}	')

    # Update Time
    status_bar.after(1000, play_time)


# Add Song Function
def add_song():
    song = filedialog.askopenfilename(
        initialdir="audio/", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),)
    )
    # Removing Directory Structure And mp3 To The Song
    song = song.replace("D:/MusicPlayer/audio/", "")
    song = song.replace(".mp3", "")
    song = song.replace("/", "")
    song_box.insert(END, song)


# Add Songs Function
def add_songs():
    songs = filedialog.askopenfilenames(
        initialdir="audio/", title="Choose Songs", filetypes=(("mp3 Files", "*.mp3"),)
    )
    for song in songs:
        # Removing Directory Structure And mp3 To The Song
        song = song.replace("D:/MusicPlayer/audio/", "")
        song = song.replace(".mp3", "")
        song = song.replace("/", "")
        song_box.insert(END, song)


# Delete Song Function
def delete_song():
    stop()
    # Delete Current Song
    song_box.delete(ANCHOR)
    # Stop Music If It's Playing
    pygame.mixer.music.stop()


# Delete Songs Function
def delete_songs():
    stop()
    # Delete All Songs
    song_box.delete(0, END)
    # Stop Music If It's Playing
    pygame.mixer.music.stop()


# Create Global Pause Variable
global paused
paused = True


# Pause/Unpause Current Song
# Play Selected Song
def play(is_paused):
    global stopped
    global paused
    if paused:
        # Unpause
        play_button = Button(
            controls_frame,
            image=pause_btn_img,
            borderwidth=0,
            command=lambda: play(paused),
        )
        play_button.grid(row=0, column=1, padx=10)
        pygame.mixer.music.unpause()
        paused = False
        if stopped:
            # Set Stop Variable To False
            stopped = False
            song = song_box.get(ACTIVE)
            # Add Directory Structure And mp3 To The Song
            song = f"D:/MusicPlayer/audio/{song}.mp3"
            # Load & Play Song
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

        # Call play_time function to get song length
        play_time()

        # Update Slider Postion
        # slider.config(to=song_len1,value=0)
        # Get current Volume
        # current_volume=pygame.mixer.music.get_volume()
        # slider_l.config(text=int(current_volume*100))

    else:
        play_button = Button(
            controls_frame,
            image=play_btn_img,
            borderwidth=0,
            command=lambda: play(paused),
        )
        play_button.grid(row=0, column=1, padx=10)
        paused = is_paused
        # Pause
        pygame.mixer.music.pause()
        paused = True


# Stop Playing Current Song
global stopped
stopped = True


def stop():
    # Reset Slider and Status Bar
    status_bar["text"] = "00:00 / 00:00"
    slider["value"] = 0
    # Stop Song from Playing
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    # Clear the status bar
    status_bar["text"] = "00:00 / 00:00"
    # Set Stop Variable To True
    global stopped
    global paused
    stopped = True
    paused=True
    play_button = Button(
            controls_frame,
            image=play_btn_img,
            borderwidth=0,
            command=lambda: play(paused),
        )
    play_button.grid(row=0, column=1, padx=10)


# Play Next Song
def next():
    # Reset Slider and Status Bar
    status_bar["text"] = "00:00 / 00:00"
    slider["value"] = 0
    # Get Current Song Tuple Number
    next_song = song_box.curselection()
    # Add One To The Current Song Number
    next_song = next_song[0] + 1
    # Get Song Title From List
    song = song_box.get(next_song)
    # Add Directory Structure And mp3 To The Song
    song = f"D:/MusicPlayer/audio/{song}.mp3"
    # Load & Play Song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear Active Bar In Listbox
    song_box.selection_clear(0, END)
    # Move Active In Listbox
    song_box.activate(next_song)
    # Set Active Bar In Listbox
    song_box.selection_set(next_song, last=None)
    # Update Slider Postion
    slider["to"] = song_len1
    slider["value"] = 0


# Play Previous Song
def previous():
    # Reset Slider and Status Bar
    status_bar["text"] = "00:00 / 00:00"
    slider["value"] = 0
    # Get Current Song Tuple Number
    next_song = song_box.curselection()
    # Add One To The Current Song Number
    next_song = next_song[0] - 1
    # Get Song Title From List
    song = song_box.get(next_song)
    # Add Directory Structure And mp3 To The Song
    song = f"D:/MusicPlayer/audio/{song}.mp3"
    # Load & Play Song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    # Clear Active Bar In Listbox
    song_box.selection_clear(0, END)
    # Move Active In Listbox
    song_box.activate(next_song)
    # Set Active Bar In Listbox
    song_box.selection_set(next_song, last=None)
    # Update Slider Postion
    slider["to"] = song_len1
    slider["value"] = 0


# Create Slider Function
def slide(x):
    if paused:
        play(paused)
    else:
        # slider_l.config(text=f'{int(slider.get())} / {song_len1}')
        song = song_box.get(ACTIVE)
        # Add Directory Structure And mp3 To The Song
        song = f"D:/MusicPlayer/audio/{song}.mp3"
        # Load & Play Song
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0, start=int(slider.get()))


# Create Volume Function
def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    # Get Current Volume
    current_volume = int(pygame.mixer.music.get_volume() * 100)
    # slider_l["text"] = current_volume
    # Change Volume Meter Image
    if current_volume == 0:
        volume_meter["image"] = vol0
    if current_volume < 25 and current_volume > 0:
        volume_meter["image"] = vol1
    if current_volume < 50 and current_volume > 25:
        volume_meter["image"] = vol2
    if current_volume < 75 and current_volume > 50:
        volume_meter["image"] = vol3
    if current_volume <= 100 and current_volume > 75:
        volume_meter["image"] = vol4


# Create Master Frame
master = Frame(root)
master.grid(row=1,column=0,pady=10)

# Create Playlist Box
song_box = Listbox(
    root,
    bg="black",
    fg="white",
    width=60,
    selectbackground="gray",
    selectforeground="black",
)
song_box.grid(row=0, column=0,padx=10,sticky="NSEW")

# Define Player Control Buttons
back_btn_img = PhotoImage(file="./assets/previous.png")
next_btn_img = PhotoImage(file="./assets/next.png")
play_btn_img = PhotoImage(file="./assets/play.png")
pause_btn_img = PhotoImage(file="./assets/pause.png")
stop_btn_img = PhotoImage(file="./assets/stop.png")

# Define Volume Control Images
vol0 = PhotoImage(file="./assets/vol_0.png")
vol1 = PhotoImage(file="./assets/vol_25.png")
vol2 = PhotoImage(file="./assets/vol_50.png")
vol3 = PhotoImage(file="./assets/vol_75.png")
vol4 = PhotoImage(file="./assets/vol_100.png")

# Create Player Control Frame
controls_frame = Frame(root)
controls_frame.grid(row=1, column=0, pady=20)

# Create Volume Meter Frame
volume_meter = Label(root, image=vol4)
volume_meter.grid(row=1, column=1, padx=10)

# Create Volume Control Frame
volume_frame = LabelFrame(root,text="Volume")
volume_frame.grid(row=0, column=1,padx=10,sticky="NSEW")

# Create Slider Frame
slider_frame = LabelFrame(root)
slider_frame.grid(row=2, column=0,padx=10,sticky="NSEW")

# Create Player Control Buttons
back_button = Button(
    controls_frame, image=back_btn_img, borderwidth=0, command=previous
)
play_button = Button(
    controls_frame, image=play_btn_img, borderwidth=0, command=lambda: play(paused)
)
next_button = Button(controls_frame, image=next_btn_img, borderwidth=0, command=next)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
play_button.grid(row=0, column=1, padx=10)
# pause_button.grid(row=0, column=2, padx=10)
next_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)

# Create Menu
menu = Menu(root)
root['menu']=menu

# Add Add Song Menu
add_song_menu = Menu(menu)
menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add 1 Song To Playlist", command=add_song)
add_song_menu.add_command(label="Add Songs To Playlist", command=add_songs)

# Add Delete Song Menu
remove_song_menu = Menu(menu)
menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete Song From Playlist", command=delete_song)
remove_song_menu.add_command(
    label="Delete All Songs From Playlist", command=delete_songs
)

# Create Status Bar
status_bar = Label(root, text="00:00 / 00:00",borderwidth=1,border=1,relief="solid")
status_bar.grid(row=2,column=1)

# Create Music Position Slider
slider = ttk.Scale(
    root, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360
)
slider.grid(row=2, column=0, pady=5,padx=20,sticky="NSEW")

# Create Volume Slider
volume_slider = ttk.Scale(
    root, from_=1, to=0, orient=VERTICAL, value=1, command=volume,length=100
)
volume_slider.grid(row=0,column=1,padx=20,pady=20,sticky="NSEW")

# Create Volume Slider Label
# slider_l = Label(volume_frame)
# slider_l.grid(row=1,column=0,sticky="NSEW")

root.mainloop()
