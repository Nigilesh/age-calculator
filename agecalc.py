from tkinter import *
from  tkinter import messagebox
def clearAll():
    dayField.delete(0, END)
    monthField.delete(0, END)
    yearField.delete(0, END)
    givenDayField.delete(0, END)
    givenMonthField.delete(0, END)
    givenYearField.delete(0, END)
    rsltDayField.delete(0, END)
    rsltMonthField.delete(0, END)
    rsltYearField.delete(0, END)

def checkError():
    if(dayField.get()=='' or monthField.get()=='' or yearField.get()==''
       or givenDayField.get()==''
       or givenMonthField.get()=='' or givenYearField.get()==''):
        messagebox.showerror('Input error')
        clearAll()
        return -1
def calculateAge():
    value = checkError()
    if value == -1 :
        return
    else:
        birth_day = int(dayField.get())
        birth_month = int(monthField.get())
        birth_year = int(yearField.get())

        given_day = int(givenDayField.get())
        given_month = int(givenMonthField.get())
        given_year = int(givenYearField.get())
        
        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (birth_day > given_day):
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]

        calculated_day = given_day - birth_day;
        calculated_month = given_month - birth_month;
        calculated_year = given_year - birth_year;

        rsltDayField.insert(10, str(calculated_day))
        rsltMonthField.insert(10, str(calculated_month))
        rsltYearField.insert(10, str(calculated_year))
# Driver Code

if __name__ == "__main__" :
    gui = Tk()
    gui.title("Age Calculator")
    gui.geometry('555x360')
    gui.configure(background = "purple")
    #Date of birth
    dob=Label(gui,text='Date of Birth',bg='blue')
    day = Label(gui, text = "Day",bg='light green')
    month = Label(gui, text = "Month",bg='light green')
    year = Label(gui, text = "Year",bg='light green')

    dayField=Entry(gui)
    monthField=Entry(gui)
    yearField=Entry(gui)
    #recent date field
    Dob=Label(gui,text='Current Date',bg='blue')
    givenDay = Label(gui, text = "Day",bg='light green')
    givenMonth = Label(gui, text = "Month",bg='light green')
    givenYear = Label(gui, text = "Year",bg='light green')

    givenDayField=Entry(gui)
    givenMonthField=Entry(gui)
    givenYearField=Entry(gui)

    resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "Red",command = calculateAge)
    #result
    rsltYear = Label(gui, text = "Years", bg = "light green")
    rsltMonth = Label(gui, text = "Months", bg = "light green")
    rsltDay = Label(gui, text = "Days", bg = "light green")

    rsltYearField = Entry(gui)
    rsltMonthField = Entry(gui)
    rsltDayField = Entry(gui)

    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red",command = clearAll)
    # date of birth grid
    dob.grid(row = 0, column = 2)

    day.grid(row = 1, column = 1)
    dayField.grid(row = 1, column = 2)
    
    month.grid(row = 2, column = 1)
    monthField.grid(row = 2, column = 2)
    
    year.grid(row = 3, column = 1)
    yearField.grid(row = 3, column = 2)
    
    
    #current date grid
    Dob.grid(row = 0, column = 12)

    givenDay.grid(row = 1, column = 10)
    givenDayField.grid(row = 1, column = 12)
    
    givenMonth.grid(row = 2, column = 10)
    givenMonthField.grid(row = 2, column = 12)
    
    givenYear.grid(row = 3, column = 10)
    givenYearField.grid(row = 3, column = 12)
    #Result
    resultantAge.grid(row = 4, column = 6)
    
    rsltYear.grid(row = 5, column = 6)
    rsltYearField.grid(row = 6, column = 6)
     
    rsltMonth.grid(row = 7, column = 6)
    rsltMonthField.grid(row = 8, column = 6)
     
    rsltDay.grid(row = 9, column = 6)
    rsltDayField.grid(row = 10, column = 6)

    clearAllEntry.grid(row = 13, column = 6)
    gui.mainloop()
