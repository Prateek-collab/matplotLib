from tkinter import*
import numpy as np
import matplotlib.pyplot as plt

root=Tk()
root.title("Histogram")
root.geometry("400x200")

def graph():
                house_prices=np.random.normal(200000,25000,5000)
                #np=numpy, normal= normal distribution
                plt.hist(house_prices,50)
                #hlist=histogram

my_btn=Button(root,text="Graph it",command=graph)
my_btn.pack()


root.mainloop()

