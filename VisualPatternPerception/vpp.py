import tkinter as tk
from PIL import ImageTk
import time

MAX_LOOPS = 50
INTERVAL = 50
START_AT = 1
END_AT = 2

term_signal = False
timer = 0.0

def get_images():
    images = list()
    images.append(ImageTk.PhotoImage(file="./images/introduction.png"))
    for i in [1, 2]:
        images.append(ImageTk.PhotoImage(file="./images/{}.png".format(i)))
    return images

def changeImage(i, loops_left):
    if loops_left > 0 and not term_signal:
        l_img.configure(image=images[i])
        i += 1
        if i > END_AT:
            i = START_AT
            loops_left -= 1
        l_img.after(INTERVAL, changeImage, i, loops_left)

def f_key_func(event):
    global term_signal
    global timer
    loops_left = MAX_LOOPS
    i = START_AT
    term_signal = False
    timer = time.time()
    l_clc.configure(text="Press C when you recognize the characters")
    l_img.after(0, changeImage, i, loops_left)

def c_key_func(event):
    global term_signal
    global timer
    term_signal = True
    timer = time.time() - timer
    print (timer)
    l_clc.configure(text="Time cost: {}".format(timer))

if __name__ == "__main__":
    top = tk.Tk()
    top.title('Visual Pattern Perception')

    images = get_images()
    
    l_img = tk.Label(top, image=images[0])
    l_img.pack()
    l_img.bind("f", f_key_func)
    l_img.bind("c", c_key_func)
    l_img.focus_set()

    l_clc = tk.Label(top, text="Press C when you recognize the characters")
    l_clc.pack()

    top.mainloop()