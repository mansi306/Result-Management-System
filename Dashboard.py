from tkinter import*
from PIL import Image,ImageTk
from Course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time 
import sqlite3
from math import*
import os 
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # == icons ==
        self.logo_dash=ImageTk.PhotoImage(file="Images\logo_p.png")





        # ===TITLE===
        title = Label(self.root,text="Student Result Management System",padx=10,image=self.logo_dash,compound=LEFT,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        # == menu ==
        M_Frame = LabelFrame(self.root,text="Menu",font=("times new roman ",15),bg="white")
        M_Frame.place(x=10,y=70,width=1250,height=80)

        btn_course = Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=10,y=5,width=200,height=40)
        btn_student = Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=220,y=5,width=200,height=40)
        btn_result = Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=430,y=5,width=200,height=40)
        btn_View = Button(M_Frame,text="View Student Results",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=640,y=5,width=200,height=40)
        btn_logout = Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=850,y=5,width=200,height=40)
        btn_exit = Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1060,y=5,width=180,height=40)


        # ==== content window ==== 
        # self.bg_img = Image.open(r"Images\bg.png")
        # self.bg_img = self.bg_img.resize((920,350),Image.ANTIALIAS)
        # self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.bg_img = Image.open(r"Images\bg.png")
        self.bg_img = self.bg_img.resize((850, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=400,y=180,width=850,height=350)

        # === update details ===
        self.lbl_course = Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="white")
        self.lbl_course.place(x=400,y=530,width=270,height=100)

        self.lbl_student = Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="white")
        self.lbl_student.place(x=685,y=530,width=270,height=100)

        self.lbl_result = Label(self.root,text="Total Results\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="white")
        self.lbl_result.place(x=970,y=530,width=270,height=100)

        # ================ clock ================================================================
        
        self.lbl=Label(self.root,text="\nWebcode Clock",font=("Book Antiqua",20,"bold"),fg="white",compound=BOTTOM,bg="#081923")
        self.lbl.place(x=20,y=175,height=450,width=350)
        
        self.working()

        # === FOOTER ================================================================
        footer = Label(self.root,text="SRMS-Student Result Management System \n Contact Us for any Technical Issue : 9168458838",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)
        self.update_details()
        # ===========================================================
    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            self.lbl_course.after(200,self.update_details)

            cur.execute("select * from student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result ")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")




        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        # print(h,m,s)
        hr= (h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(hr,min_,sec_)
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file=r"clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw = ImageDraw.Draw(clock)
        #  ================= for clock image =====================
        bg = Image.open(r"Images\c.png")
        bg= bg.resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg,(50,50))

        # Formula to rotate the clock 
        # angle_in_radians = angle_in_degrees * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)


        origin = 200,200  
        # ============= hour line image =======================
        # x1,y1,x2,y2
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)

        # ================ minute line image =================
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)

         # ================ second line image =================
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("clock_new.png")

        

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)


    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op= messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    
    def exit_(self):
        op= messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op == True:
            self.root.destroy()
            
    
    


if __name__=="__main__":
    root = Tk()
    obj=RMS(root)
    root.mainloop()
