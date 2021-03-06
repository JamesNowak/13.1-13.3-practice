# this import the necessary commands
import tkinter
import tkinter.messagebox


# creates the class
class CustomerGui:
    def __init__(self):
        # creates the main window
        self.main_window = tkinter.Tk()

        # creates two frames one for the selection on for the buttons
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # creates the selections
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # sets all the variables to zero
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # creates the lables for the selections
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text='Pack of 10 pens',
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text='Pack of 10 pencils',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text='Pack of 5 erasers',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text='1 notebook',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text='Pack of markers',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                       text='Pack of crayons',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                       text='Ear buds',
                                       variable=self.cb_var7)

        # packs all the selcetions
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # creates the buttons and defines their functions
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # packs up the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # packs the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # sets teh loop into motion
        tkinter.mainloop()

    # this defines what happens when a choice is selected and designates how much verything costs
    def show_choice(self):
        self.message = 0
        if self.cb_var1.get() == 1:
            self.message = self.message + 2
        if self.cb_var2.get() == 1:
            self.message = self.message + 2
        if self.cb_var3.get() == 1:
            self.message = self.message + 1.5
        if self.cb_var4.get() == 1:
            self.message = self.message + .75
        if self.cb_var5.get() == 1:
            self.message = self.message + 2.5
        if self.cb_var6.get() == 1:
            self.message = self.message + 2.5
        if self.cb_var7.get() == 1:
            self.message = self.message + 4

        # sets the message that is desplayed after clicking ok
        self.message = 'Your total is:\n' + (str("${:.2f}".format(self.message)))
        tkinter.messagebox.showinfo('selection', self.message)


# this is the first instance of the program
customer_gui = CustomerGui()
