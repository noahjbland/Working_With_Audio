import numpy as np
import simpleaudio as sa
from tkinter import *
import matplotlib.pyplot as plot
from random import seed
from random import randint

def audioFunction(frequency_input, seconds_input):
    frequency = frequency_input  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = seconds_input  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a sine wave
    note1 = np.sin(frequency * t * 2 * np.pi)

    # Generate a second sine wave for harmonics1
    note2 = np.sin(frequency*1 * t * 2 * np.pi)

    note3 = np.sin(frequency*3 * t * 2 * np.pi)

    note4 = np.sin(frequency*5 * t * 2 * np.pi)


    note5 = note1 + note3

    # Generate a square wave

    # Ensure that highest value is in 16-bit range
    audio = note5 * (2**15 - 1) / np.max(np.abs(note5))

    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Square lead on sin wave
    # for i in range(fs*seconds):
    #     if audio[i] > 0:
    #         audio[i] = 32767
    #     if audio[i] < 0:
    #         audio[i] = -32767

    # Clipping
    # for i in range(fs*seconds):
    #     if audio[i] > 5000:
    #         audio[i] = 5000
    #     if audio[i] < -5000:
    #         audio[i] = -5000

    # low pass

    # high pass

    # distortion
    # for i in range(fs*seconds):
    #     if audio[i] > 0:
    #         audio[i] = audio[i] - randint(0,100)
    #     if audio[i] < 0:
    #         audio[i] = audio[i] + randint(0,100)

    play_obj = sa.play_buffer(audio, 1, 2, fs)

    plot.plot(t, audio)
    plot.xlim([0, .1])
    plot.show()

    play_obj.wait_done()

    # Start playback

    # Wait for playback to finish before exiting

def show_values(w1,w2):
    print("show")

def main():
    root = Tk()
    root.title('AudioMaker')
    root.geometry("400x400")

    label1 = Label(root, text = "FREQUENCY").pack()

    slider1 = Scale(root, from_=0, to=440, orient=HORIZONTAL)
    slider1.pack()

    label2 = Label(root, text = "SECONDS").pack()

    slider2 = Scale(root, from_=0, to=5, orient=HORIZONTAL)
    slider2.pack()

    def getValues():
        frequency = slider1.get()
        seconds = slider2.get()
        audioFunction(frequency,seconds)
        

    button1 = Button(root, text = "PLAY AUDIO", command = getValues).pack()

    root.mainloop()
    

if __name__ == "__main__":
    main()