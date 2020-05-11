from tkinter import Tk, Frame, YES, NO, CENTER, IntVar, StringVar, END
from tkinter import ttk
import sqlite3 as sql
from os import getcwd
from PIL import Image, ImageTk
from time import sleep

position = getcwd()

class Counseling(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self)
        self.title("Counseling App")
        self.iconbitmap(position + "/Requirements/AU.ico")
        self.wm_state('zoomed')
        self.minsize(width=1300, height=649)
        self.width1 = self.winfo_screenwidth()
        self.height1 = self.winfo_screenheight()
        self.frame = Frame(self, background="white",
                           width=self.width1, height=self.height1)
        self.frame.place(width=self.width1, height=self.height1)
        self.width_change = self.frame['width']
        self.height_change = self.frame['height']
        self.insideOfCounse()
        self.bind("<Configure>", self.on_resize)

    def on_resize(self, event):
        self.config(width=event.width, height=event.height)
        self.width_change = event.width
        self.height_change = event.height
        if self.width_change >= 1300 and self.height_change >= 649:
            self.gvt.place_configure(x=float(self.width_change/13),
                        y=float(self.height_change/20))
            self.myname.place_configure(x=float(self.width_change/6),
                            y=float(self.height_change/10))
            self.fromRankEn.place_configure(x=float(self.width_change/2),
                                y=float(self.height_change/10))
            x_axis = float(self.width_change/2) - (self.fromLabel.winfo_reqwidth() -
                                                self.fromRankEn.winfo_reqwidth())/2
            self.fromLabel.place_configure(x=x_axis, y=float(self.height_change/17))
            self.TORankEn.place_configure(x=float(self.width_change/2) +
                        (self.fromLabel.winfo_reqwidth()+self.fromRankEn.winfo_reqwidth()), y=float(self.height_change/10))
            x_axis2 = float(self.width_change/2)+(self.fromLabel.winfo_reqwidth()+self.fromRankEn.winfo_reqwidth()) - (self.TOLabel.winfo_reqwidth() -
                                                                                                                    self.TORankEn.winfo_reqwidth())/2
            self.TOLabel.place_configure(x=x_axis2, y=float(self.height_change/17))
            self.CollEn.place_configure(
                x=x_axis2+(2*self.TOLabel.winfo_reqwidth()), y=float(self.height_change/10))
            self.CollLabel.place_configure(x=x_axis2+(2*self.TOLabel.winfo_reqwidth()) - (
                (self.CollLabel.winfo_reqwidth()-self.CollEn.winfo_reqwidth())/2), y=float(self.height_change/17))

            x_axis3 = x_axis2+(2*self.TOLabel.winfo_reqwidth()) - \
                ((self.CollLabel.winfo_reqwidth()-self.CollEn.winfo_reqwidth())/2)
            self.label.place_configure(
                x=x_axis3 + 2*self.CollLabel.winfo_reqwidth(), y=float(self.height_change/11))

            small_width = int((self.width_change/11) +
                              (2*((self.width_change/11)/3))/11)
            self.WholeView.column("#0", stretch=YES, minwidth=int((self.width_change/11)/2),
                                width=int((self.width_change/11)/2), anchor='w')
            self.WholeView.column("#1", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#2", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#3", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#4", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#5", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#6", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#7", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#8", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#9", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
            self.WholeView.column("#10", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)

        else:
            pass

    def insideOfCounse(self):
        self.INTVARFR = IntVar()
        self.INTVARTO = IntVar()
        self.COLCODE = StringVar()
        self.gvt = ttk.Label(self.frame, text="TNEA 2018 Cutoff details", font = ("Times 20"), background="white", foreground="brown")
        self.gvt.place(x=float(self.width_change/13), y=float(self.height_change/20))
        self.myname = ttk.Label(self.frame, text="Created by,\n\tKiruban Kamaraj", font = ("Times 16"), background="white", foreground="brown")
        self.myname.place(x=float(self.width_change/6),
                          y=float(self.height_change/11))
        self.fromRankEn = ttk.Entry(self.frame, textvar=self.INTVARFR, font = ("Times 16"), width = 6)
        self.fromRankEn.place(x=float(self.width_change/2), y=float(self.height_change/10))
        self.fromRankEn.focus()
        self.fromLabel = ttk.Label(self.frame, text="From Rank",
                              font=("Times 16"), background="white")
        x_axis = float(self.width_change/2) - (self.fromLabel.winfo_reqwidth() -
                                     self.fromRankEn.winfo_reqwidth())/2
        self.fromLabel.place(x=x_axis, y=float(self.height_change/17))
        self.TORankEn = ttk.Entry(self.frame, textvar=self.INTVARTO,
                               font=("Times 16"), width=6)
        self.TORankEn.place(x=float(self.width_change/2) +
                       (self.fromLabel.winfo_reqwidth()+self.fromRankEn.winfo_reqwidth()), y=float(self.height_change/10))

        self.TOLabel = ttk.Label(self.frame, text="To Rank",
                              font=("Times 16"), background="white")
        x_axis2 = float(self.width_change/2)+(self.fromLabel.winfo_reqwidth()+self.fromRankEn.winfo_reqwidth()) - (self.TOLabel.winfo_reqwidth() -
                                        self.TORankEn.winfo_reqwidth())/2
        self.TOLabel.place(x=x_axis2, y=float(self.height_change/17))
        self.CollEn = ttk.Entry(self.frame, textvar=self.COLCODE,
                           font=("Times 16"), width=6)
        self.CollEn.place(x=x_axis2+(2*self.TOLabel.winfo_reqwidth()), y=float(self.height_change/10))
        self.CollLabel = ttk.Label(self.frame, text="Community",
                            font=("Times 16"), background="white")
        self.CollLabel.place(x=x_axis2+(2*self.TOLabel.winfo_reqwidth()) - ((self.CollLabel.winfo_reqwidth()-self.CollEn.winfo_reqwidth())/2), y=float(self.height_change/17))

        x_axis3 = x_axis2+(2*self.TOLabel.winfo_reqwidth()) - \
            ((self.CollLabel.winfo_reqwidth()-self.CollEn.winfo_reqwidth())/2)

        def fch(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/findup.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/find.png"
            self.findImageChange = ImageTk.PhotoImage(
                Image.open(position+ImageName))
            self.label.configure(image=self.findImageChange)
            self.label.image = self.findImageChange
        
        photo = ImageTk.PhotoImage(Image.open(
            position + "/Requirements/find.png"))
        self.label = ttk.Label(self.frame, image=photo, background="#FDFEFE")
        self.label.image = photo
        self.label.place(
            x=x_axis3 + 2*self.CollLabel.winfo_reqwidth(), y=float(self.height_change/11))

        self.label.bind("<Enter>", fch)
        self.label.bind("<Leave>", fch)
        self.label.bind("<Button-1>", self.fetching)
        self.label.bind("<Return>", self.fetching)
        
        def upchange(event):
            self.label.event_generate("<Enter>")
            self.label.focus()

        self.fromRankEn.bind("<Return>", lambda a: self.TORankEn.focus())
        self.TORankEn.bind("<Return>", lambda a: self.CollEn.focus())
        self.fromRankEn.bind("<FocusIn>", lambda a:self.fromRankEn.select_range(0, END))
        self.TORankEn.bind("<FocusIn>", lambda a: self.TORankEn.select_range(0, END))
        self.CollEn.bind("<FocusIn>", lambda a: self.CollEn.select_range(0, END))
        self.CollEn.bind("<Return>", upchange)

        style = ttk.Style()
        style.configure("Treeview", font=(
            "Times", 12), background="brown", foreground="white", rowheight=30)
        style.configure("Treeview.Heading", font=(
            "Times", 12), background="brown")

        self.WholeView = ttk.Treeview(self.frame, selectmode='browse')
        self.WholeView["columns"] = ("SL.NO.", "College Code", "Branch Code", "Round No", "APP.NO.", "Community", "Overall Rank", "Community Rank", "MARK",
        "Choice No", "Category Allotted")

        self.Scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.WholeView.yview)

        small_width = int((self.width_change/11) +
                            (2*((self.width_change/11)/3))/11)

        self.WholeView.column("#0", stretch=YES, minwidth=int((self.width_change/11)/2),
                             width=int((self.width_change/11)/2), anchor='w')
        self.WholeView.column("#1", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#2", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#3", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#4", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#5", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#6", stretch=NO, minwidth=small_width,
                                width=small_width, anchor=CENTER)
        self.WholeView.column("#7", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#8", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#9", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)
        self.WholeView.column("#10", stretch=NO, minwidth=small_width,
                             width=small_width, anchor=CENTER)

        self.WholeView.heading("#0", text="SL.NO.")
        self.WholeView.heading("#1", text="College Code")
        self.WholeView.heading("#2", text="Branch Code")
        self.WholeView.heading("#3", text="Round No")
        self.WholeView.heading("#4", text="APP.NO.")
        self.WholeView.heading("#5", text="Community")
        self.WholeView.heading("#6", text="Overall Rank")
        self.WholeView.heading("#7", text="Community Rank")
        self.WholeView.heading("#8", text="MARK")
        self.WholeView.heading("#9", text="Choice No")
        self.WholeView.heading("#10", text="Category Allotted")

        negheight = (self.height_change - float(self.height_change/5.5))/28.276363636363634
        self.WholeView.place(x=0, y=float(self.height_change/5.5),
                            width=self.width_change - 20, height=self.height_change - float(self.height_change/5.5) - negheight)

        self.WholeView.configure(
            yscrollcommand=self.Scroll.set)
        self.Scroll.place(x=self.width_change - 20, y=float(self.height_change/5.5),
                          height=self.height_change - float(self.height_change/5.5) - negheight)

    def fetching(self, event=None):
        start = self.INTVARFR.get() 
        end = self.INTVARTO.get()
        colco = self.COLCODE.get()
        self.WholeView.delete(*self.WholeView.get_children())
        if len(str(start)) >= 1 and len(str(end)) >= 1:
            with sql.connect(position + "/Counseling.db") as db:
                data = db.cursor()
                data.execute(
                    '''SELECT * FROM Counseling WHERE OverallRank >= %s AND OverallRank <= %s ORDER BY OverallRank ASC''' % (start, end))
                details = data.fetchall()
                db.commit()
            if len(colco) >= 1:
                hole_out = []
                for i in details:
                    if i[4] == str(colco).upper():
                        hole_out.append(i)
                    else:
                        pass
                for insert in range(0, len(hole_out)):
                    self.WholeView.insert("", "end", text=insert+1, values=(
                        hole_out[insert][0], hole_out[insert][1], hole_out[insert][2], hole_out[insert][3], hole_out[insert][4], hole_out[insert][5], hole_out[insert][6], hole_out[insert][7], hole_out[insert][8], hole_out[insert][9]))
            else:
                for insert in range(0, len(details)):
                    self.WholeView.insert("", "end", text=insert+1, values=(
                        details[insert][0], details[insert][1], details[insert][2], details[insert][3], details[insert][4], details[insert][5], details[insert][6], details[insert][7], details[insert][8], details[insert][9]))
        else:
            pass

        try:
            if event.keysym == "Return":
                sleep(0.5)
                self.label.event_generate("<Leave>")
                self.fromRankEn.focus()
            else:   pass
        except:
            pass

if __name__ == "__main__":    
    app = Counseling()
    app.mainloop()
