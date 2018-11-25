# this imports the tknitner gui commands
import tkinter


# this creates the class for the program so it can be used in other places if necessary
class MpgConverter:
    def __init__(self):
        # initializes the main window
        self.main_window = tkinter.Tk()

        # this creates the separate frames of the screen
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # this creates teh labels and boxes that the program uses to calculate the mpg
        self.gallon_label = tkinter.Label(self.top_frame,
                                          text='Enter how many gallon your car can take:')
        self.gallon_entry = tkinter.Entry(self.top_frame,
                                          width=10)
        self.miles_driven_label = tkinter.Label(self.top_frame,
                                                text='How many miles have you traveled:')
        self.miles_driven_entry = tkinter.Entry(self.top_frame,
                                                width=10)

        # this packs them up and makes them usable
        self.gallon_label.pack(side='top')
        self.gallon_entry.pack(side='top')
        self.miles_driven_label.pack(side='top')
        self.miles_driven_entry.pack(side='top')

        # this desplays the data the program calculates
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='Converted to miles per gallons:')

        # this is used to store the mpg
        self.value = tkinter.StringVar()

        # this displays the mpg
        self.mpg_label = tkinter.Label(self.mid_frame,
                                       textvariable=self.value)

        # this packs the labels and makes them usable
        self.descr_label.pack(side='left')
        self.mpg_label.pack(side='left')

        # this creates the buttons and gives them the functions to calculate the mpg and close teh program
        self.convert_button = tkinter.Button(self.bottom_frame,
                                             text='Convert',
                                             command=self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        # this packs the buttons up to be able to use them
        self.convert_button.pack(side='left')
        self.quit_button.pack(side='left')

        # this packs the frames up
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # this makes the program run
        tkinter.mainloop()

    # this defines how the program calculates the data
    def convert(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_driven_entry.get())

        mpg = miles / gallons

        self.value.set(mpg)


# this makes an instance of the program
mpg_converter = MpgConverter()
