
# Goodwill Calculator v1.0
import tkinter as tk
from tkinter import *

import time
def clear(event):
    event.widget.delete(0, "end")
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="              Goodwill Calculator ", font=('helvetica',14),fg="green").grid(row=0,column=0)
        tk.Label(self, text="Average Profit Method", font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Super Profit Method", font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Capitalisation Of Super Profit", font=('helvetica',14)).grid(row=3,column=0,sticky=W)
        tk.Label(self, text="Capitalisation Method", font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="Weight Average Profit", font=('helvetica',14)).grid(row=5,column=0,sticky=W)
        tk.Label(self, text="         Developed By - Nishant Tiwari (dx4iot)", font=('helvetica',14),fg="red").grid(row=6,column=0)

        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageOne)).grid(row=1,column=1,sticky=W)
        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageTwo)).grid(row=2,column=1,sticky=W)
        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageThree)).grid(row=3,column=1,sticky=W)
        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFour)).grid(row=4,column=1,sticky=W)
        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFive)).grid(row=5,column=1,sticky=W)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="", font=('helvetica',14)).grid(row=0,column=0,sticky=W)

        tk.Label(self, text="> If Average Profit Is Given", font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="> If Average Profit Is Not Given", font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="> If Total Profit Is Given", font=('helvetica',14)).grid(row=3,column=0,sticky=W)

        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageOneofone)).grid(row=1,column=1,sticky=W)
        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageOneoftwo)).grid(row=2,column=1,sticky=W)
        tk.Button(self, text="Find", font=('helvetica',14),
                  command=lambda: master.switch_frame(PageOneofthree)).grid(row=3,column=1,sticky=W)
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)    

class PageOneofone(tk.Frame):
        
    def __init__(self, master):
        global avg_profit_1of1,no_of_years_1of1,result_1of1

        def calculate_1of1(): 
            val_amount = int(avg_profit_1of1.get()) 
            value_no_of_days = int(no_of_years_1of1.get())              
            calculated_day = val_amount * value_no_of_days  
            result_1of1.insert(10, calculated_day)
           
        tk.Frame.__init__(self, master) 
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Number Of Years",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is ",font=('helvetica',14)).grid(row=2,column=0,sticky=W)

        avg_profit_1of1 = tk.Entry(self,font=('helvetica',10))
        avg_profit_1of1.grid(row=0,column=1,sticky=W)
        no_of_years_1of1 = tk.Entry(self,font=('helvetica',10))
        no_of_years_1of1.grid(row=1,column=1,sticky=W)
        
        result_1of1 = tk.Entry(self,font=('helvetica',10))
        result_1of1.grid(row=2,column=1,sticky=W)

        val_cal = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculate_1of1).grid(row=3,column=1,sticky=W) 
        tk.Button(self, text="Back",font=('helvetica',14),
                          command=lambda: master.switch_frame(PageOne)).grid(row=4,column=0,sticky=W)

    
         
class PageOneoftwo(tk.Frame):
    def __init__(self, master):
        global totalprofit_entry_1of2,noofyears_entry_1of2,avgprofit_entry_1of2
        def calculateavg_1of2(): 
            cal_total_1of2 = float(totalprofit_entry_1of2.get()) 
            cal_noofyr_1of2 = float(noofyears_entry_1of2.get())              
            cal_avg_1of2 = cal_total_1of2 / cal_noofyr_1of2  
            avgprofit_entry_1of2.insert(10,cal_avg_1of2)
        def calculategwill_1of2():
            calyrpur_1of2 = float(yearpurchase_entry_1of2.get())
            calavg_1of2_again = float(avgprofit_entry_1of2.get())
            cal_gwill_1of2 = calyrpur_1of2 * calavg_1of2_again
            gwill_entry_1of2.insert(10,cal_gwill_1of2)
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter Total Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Number Of Years",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Average Profit is ",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Number OF Years Purchase ",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is ",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        totalprofit_entry_1of2 = tk.Entry(self,font=('helvetica',10))
        totalprofit_entry_1of2.grid(row=0,column=1,sticky=W)
        noofyears_entry_1of2 = tk.Entry(self,font=('helvetica',10))
        noofyears_entry_1of2.grid(row=1,column=1,sticky=W)
        avgprofit_entry_1of2 =  tk.Entry(self,font=('helvetica',10))
        avgprofit_entry_1of2.grid(row=2,column=1,sticky=W)
        yearpurchase_entry_1of2 =  tk.Entry(self,font=('helvetica',10))
        yearpurchase_entry_1of2.grid(row=4,column=1,sticky=W)
        gwill_entry_1of2 =  tk.Entry(self,font=('helvetica',10))
        gwill_entry_1of2.grid(row=5,column=1,sticky=W)

    
        avgprofit_button_1of2 = tk.Button(self, text="Average Profit",font=('helvetica',14),command=calculateavg_1of2).grid(row=3,column=1,sticky=W) 
        goodwill_button_1of2 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_1of2).grid(row=6,column=1,sticky=W) 

        tk.Button(self, text="Back",font=('helvetica',14),
                          command=lambda: master.switch_frame(PageOne)).grid(row=8,column=0,sticky=W)
class PageOneofthree(tk.Frame):
    def __init__(self, master):
        global profit_entry_1of3,abloss_entry_1of3,abgain_entry_1of3,nrmexp_entry_1of3,totalprofit_entry_1of3,noofyear_entry_1of3,avgprofit_entry_1of3
        def calculatetotprof_1of3():
            calprofitentry_1of3 = int(profit_entry_1of3.get())
            calabloss_entry_1of3 = int(abloss_entry_1of3.get())
            calabloss_entry_1of3 = int(abgain_entry_1of3.get())
            calnrmexp_entry_1of3 = int(nrmexp_entry_1of3.get())   
            caltotprof_1of3 =  calprofitentry_1of3 + calabloss_entry_1of3 + calabloss_entry_1of3 + calnrmexp_entry_1of3
            totalprofit_entry_1of3.insert(10,caltotprof_1of3) 
        def calculateavgprof_1of3():
            caltotprof_1of3 = float(totalprofit_entry_1of3.get())
            calnoofyear_1of3 = float(noofyear_entry_1of3.get())
            calavgprofit_1of3 = caltotprof_1of3/calnoofyear_1of3
            avgprofit_entry_1of3.insert(10,calavgprofit_1of3)
        def calculategwill_1of3():
            calavgprofit_1of3_again = float(avgprofit_entry_1of3.get())
            calnoofyearpur_1of3 = float(noofyearpur_entry_1of3.get())
            calgwill_1of3 = calavgprofit_1of3_again * calnoofyearpur_1of3
            gwill_entry_1of3.insert(10,calgwill_1of3)
            
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Abnormal Loss",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Enter Abnormal Gain",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Normal Expenses",font=('helvetica',14)).grid(row=3,column=0,sticky=W)
        tk.Label(self, text="Total Profit is",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="Enter No Of Year",font=('helvetica',14)).grid(row=7,column=0,sticky=W)
        tk.Label(self, text="Average Profit is",font=('helvetica',14)).grid(row=8,column=0,sticky=W)
        tk.Label(self, text="Enter No Of Year Purchase",font=('helvetica',14)).grid(row=10,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=11,column=0,sticky=W)

        profit_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        profit_entry_1of3.grid(row=0,column=1,sticky=W)
        
        abloss_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        abloss_entry_1of3.grid(row=1,column=1,sticky=W)
        
        abgain_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        abgain_entry_1of3.grid(row=2,column=1,sticky=W)
        
        nrmexp_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        nrmexp_entry_1of3.grid(row=3,column=1,sticky=W)
        
        totalprofit_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        totalprofit_entry_1of3.grid(row=4,column=1,sticky=W)


        noofyear_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        noofyear_entry_1of3.grid(row=7,column=1,sticky=W)
        
        avgprofit_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        avgprofit_entry_1of3.grid(row=8,column=1,sticky=W)

        noofyearpur_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        noofyearpur_entry_1of3.grid(row=10,column=1,sticky=W)

        gwill_entry_1of3 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_1of3.grid(row=11,column=1,sticky=W)
        
        totalprofit_button_1of3 = tk.Button(self, text="Total Profit",font=('helvetica',14),command=calculatetotprof_1of3).grid(row=6,column=1,sticky=W) 
        avgprofit_button_1of3 = tk.Button(self, text="Average Profit",font=('helvetica',14),command=calculateavgprof_1of3).grid(row=9,column=1,sticky=W) 
        gwill_button_1of3 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_1of3).grid(row=12,column=1,sticky=W) 

        

        
        tk.Button(self, text="Back",font=('helvetica',14),
                              command=lambda: master.switch_frame(PageOne)).grid(row=13,column=0,sticky=W)
        


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Super Profit Is Given",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="> If Super Profit Is Not Given",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="> If Normal Profit Is Not Given",font=('helvetica',14)).grid(row=2,column=0,sticky=W)


        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_2of1)).grid(row=0,column=1)      
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_2of2)).grid(row=1,column=1)     
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_2of3)).grid(row=2,column=1)      

        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)

class Page_2of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global sprprofit_entry_2of1, noofyrpur_entry_2of1, gwill_entry_2of1
        def calculategwill_2of1():
            calsprprofit_entry_2of1 = int(sprprofit_entry_2of1.get())
            calnoofyrpur_entry_2of1 = int(noofyrpur_entry_2of1.get())
            calgwill_2of1 = calsprprofit_entry_2of1 * calnoofyrpur_entry_2of1
            gwill_entry_2of1.insert(10,calgwill_2of1)
            
        tk.Label(self, text="Enter Super Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Number Of Year Purchase",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)

        sprprofit_entry_2of1 = tk.Entry(self,font=('helvetica',10))
        sprprofit_entry_2of1.grid(row=0,column=1,sticky=W)
        
        noofyrpur_entry_2of1 = tk.Entry(self,font=('helvetica',10))
        noofyrpur_entry_2of1.grid(row=1,column=1,sticky=W)

        gwill_entry_2of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_2of1.grid(row=2,column=1,sticky=W)

        gwill_button_2of1 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_2of1).grid(row=4,column=1,sticky=W) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageTwo)).grid(sticky=W)
        
class Page_2of2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global noofyrpur_entry_2of2,sprprof_entry_2of2, avgprof_entry_2of2, gwill_entry_2of2,norprof_entry_2of2

        def calculatesprprof_2of2():
            calavgprof_entry_2of2 = int(avgprof_entry_2of2.get())
            calnormalprof_entry_2of2 = int(norprof_entry_2of2.get())
            calsprprof_2of2 = calavgprof_entry_2of2 -  calnormalprof_entry_2of2
            sprprof_entry_2of2.insert(10,calsprprof_2of2)
        def calculategwill_2of2():
            calsprprof_entry_2of2_again = int(sprprof_entry_2of2.get())
            calnoofyrpur_entry_2of2 = int(noofyrpur_entry_2of2.get())
            calgwill_2of2 = calsprprof_entry_2of2_again * calnoofyrpur_entry_2of2
            gwill_entry_2of2.insert(10,calgwill_2of2)
            
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Normal Profit",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Super Profit is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter No Of Year Purchase",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        avgprof_entry_2of2 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_2of2.grid(row=0,column=1,sticky=W)
        
        norprof_entry_2of2 = tk.Entry(self,font=('helvetica',10))
        norprof_entry_2of2.grid(row=1,column=1,sticky=W)

        sprprof_entry_2of2 = tk.Entry(self,font=('helvetica',10))
        sprprof_entry_2of2.grid(row=2,column=1,sticky=W)
        
        noofyrpur_entry_2of2 = tk.Entry(self,font=('helvetica',10))
        noofyrpur_entry_2of2.grid(row=4,column=1,sticky=W)
        
        gwill_entry_2of2 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_2of2.grid(row=5,column=1,sticky=W)

        sprprof_button_2of2 = tk.Button(self, text="Super Profit",font=('helvetica',14),command=calculatesprprof_2of2).grid(row=3,column=1,sticky=W) 
        gwill_button_2of2 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_2of2).grid(row=6,column=1,sticky=W) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageTwo)).grid(sticky=W)
class Page_2of3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Capital Employed is ( Asset - Liabilities)",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="> If Capital Employes is (Capital + Reversed)",font=('helvetica',14)).grid(row=1,column=0,sticky=W)

        
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_2of3of1)).grid(row=0,column=1)      
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_2of3of2)).grid(row=1,column=1)     

        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)
class Page_2of3of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global gwill_entry_2of3of1,noyrpur_entry_2of3of1,sprprof_entry_2of3of1,asset_entry_2of3of1,liab_entry_2of3of1,capemp_entry_2of3of1,rate_entry_2of3of1,norprof_entry_2of3of1,avgprof_entry_2of3of1
        def calculatecapemp_2of3of1():
            calasset_entry_2of3of1= int(asset_entry_2of3of1.get())
            calliab_entry_2of3of1 = int(liab_entry_2of3of1.get())
            calcapemp_2of3of1 = calasset_entry_2of3of1 - calliab_entry_2of3of1
            capemp_entry_2of3of1.insert(10,calcapemp_2of3of1)
        def calculatenorprof_2of3of1():
            calcapemp_entry_2of3of1 = float(capemp_entry_2of3of1.get())
            calrate_entry_2of3of1 = float(rate_entry_2of3of1.get())
            calnorprof_2of3of1 = calcapemp_entry_2of3of1 * calrate_entry_2of3of1 / 100
            norprof_entry_2of3of1.insert(10,calnorprof_2of3of1)
        def calculatesprprof_2of3of1():
            calavgprof_entry_2of3of1 = int(avgprof_entry_2of3of1.get())
            calnorprof_entry_2of3of1 = float(norprof_entry_2of3of1.get())
            calsprprof_2of3of1 = calavgprof_entry_2of3of1 - calnorprof_entry_2of3of1
            sprprof_entry_2of3of1.insert(10,calsprprof_2of3of1)
        def calculatenoyrpur_entry_2of3of1():
            calnoyrpur_entry_2of3of1 = int(noyrpur_entry_2of3of1.get())
            calsprprof_entry_2of3of1 = float(sprprof_entry_2of3of1.get())
            calgwill_entry_2of3of1 = calnoyrpur_entry_2of3of1 * calsprprof_entry_2of3of1
            gwill_entry_2of3of1.insert(10,calgwill_entry_2of3of1)
            
        tk.Label(self, text="Enter Asset",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Liabilites",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Employed is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Rate",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="Normal Profit is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=7,column=0,sticky=W)
        tk.Label(self, text="Super Profit is",font=('helvetica',14)).grid(row=8,column=0,sticky=W)
        tk.Label(self, text="Enter No Of Year Purchase",font=('helvetica',14)).grid(row=10,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=11,column=0,sticky=W)

        asset_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        asset_entry_2of3of1.grid(row=0,column=1,sticky=W)
        
        liab_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        liab_entry_2of3of1.grid(row=1,column=1,sticky=W)
        
        capemp_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_2of3of1.grid(row=2,column=1,sticky=W)

        rate_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        rate_entry_2of3of1.grid(row=4,column=1,sticky=W)

        norprof_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        norprof_entry_2of3of1.grid(row=5,column=1,sticky=W)

        avgprof_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_2of3of1.grid(row=7,column=1,sticky=W)
                                                    
        sprprof_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        sprprof_entry_2of3of1.grid(row=8,column=1,sticky=W)

        noyrpur_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        noyrpur_entry_2of3of1.grid(row=10,column=1,sticky=W)

        gwill_entry_2of3of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_2of3of1.grid(row=11,column=1,sticky=W)

        tk.Button(self, text="Capital Employed",font=('helvetica',14),command=calculatecapemp_2of3of1).grid(row=3,column=1) 
        tk.Button(self, text="Normal Profit",font=('helvetica',14),command=calculatenorprof_2of3of1).grid(row=6,column=1) 
        tk.Button(self, text="Super Profit",font=('helvetica',14),command=calculatesprprof_2of3of1).grid(row=9,column=1) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculatenoyrpur_entry_2of3of1).grid(row=12,column=1) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(Page_2of3)).grid(sticky=W)

class Page_2of3of2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global gwill_entry_2of3of2,noyrpur_entry_2of3of2,sprprof_entry_2of3of2,asset_entry_2of3of2,liab_entry_2of3of2,capemp_entry_2of3of2,rate_entry_2of3of2,norprof_entry_2of3of2,avgprof_entry_2of3of2

        def calculatecapemp_2of3of2():
            calcap_entry_2of3of2= int(cap_entry_2of3of2.get())
            calrev_entry_2of3of2 = int(rev_entry_2of3of2.get())
            calcapemp_2of3of2 = calcap_entry_2of3of2 + calrev_entry_2of3of2
            capemp_entry_2of3of2.insert(10,calcapemp_2of3of2)
        def calculatenorprof_2of3of2():
            calcapemp_entry_2of3of2 = float(capemp_entry_2of3of2.get())
            calrate_entry_2of3of2 = float(rate_entry_2of3of2.get())
            calnorprof_2of3of2 = calcapemp_entry_2of3of2 * calrate_entry_2of3of2 / 100
            norprof_entry_2of3of2.insert(10,calnorprof_2of3of2)
        def calculatesprprof_2of3of2():
            calavgprof_entry_2of3of2 = int(avgprof_entry_2of3of2.get())
            calnorprof_entry_2of3of2 = float(norprof_entry_2of3of2.get())
            calsprprof_2of3of2 = calavgprof_entry_2of3of2 - calnorprof_entry_2of3of2
            sprprof_entry_2of3of2.insert(10,calsprprof_2of3of2)
        def calculatenoyrpur_entry_2of3of2():
            calnoyrpur_entry_2of3of2 = int(noyrpur_entry_2of3of2.get())
            calsprprof_entry_2of3of2 = float(sprprof_entry_2of3of2.get())
            calgwill_entry_2of3of2 = calnoyrpur_entry_2of3of2 * calsprprof_entry_2of3of2
            gwill_entry_2of3of2.insert(10,calgwill_entry_2of3of2)
            
        tk.Label(self, text="Enter Capital",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Reserve",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Employed is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Rate",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="Normal Profit is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=7,column=0,sticky=W)
        tk.Label(self, text="Super Profit is",font=('helvetica',14)).grid(row=8,column=0,sticky=W)
        tk.Label(self, text="Enter No Of Year Purchase",font=('helvetica',14)).grid(row=10,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=11,column=0,sticky=W)

        cap_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        cap_entry_2of3of2.grid(row=0,column=1,sticky=W)
        
        rev_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        rev_entry_2of3of2.grid(row=1,column=1,sticky=W)
        
        capemp_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_2of3of2.grid(row=2,column=1,sticky=W)

        rate_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        rate_entry_2of3of2.grid(row=4,column=1,sticky=W)

        norprof_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        norprof_entry_2of3of2.grid(row=5,column=1,sticky=W)

        avgprof_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_2of3of2.grid(row=7,column=1,sticky=W)
                                                    
        sprprof_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        sprprof_entry_2of3of2.grid(row=8,column=1,sticky=W)

        noyrpur_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        noyrpur_entry_2of3of2.grid(row=10,column=1,sticky=W)

        gwill_entry_2of3of2 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_2of3of2.grid(row=11,column=1,sticky=W)

        tk.Button(self, text="Capital Employed",font=('helvetica',14),command=calculatecapemp_2of3of2).grid(row=3,column=1) 
        tk.Button(self, text="Normal Profit",font=('helvetica',14),command=calculatenorprof_2of3of2).grid(row=6,column=1) 
        tk.Button(self, text="Super Profit",font=('helvetica',14),command=calculatesprprof_2of3of2).grid(row=9,column=1) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculatenoyrpur_entry_2of3of2).grid(row=12,column=1) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(Page_2of3)).grid(sticky=W)
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Super Profit Is Given",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="> If Super Profit Is Not Given",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="> If Normal Profit Is Not Given",font=('helvetica',14)).grid(row=2,column=0,sticky=W)


        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_3of1)).grid(row=0,column=1)      
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_3of2)).grid(row=1,column=1)     
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_3of3)).grid(row=2,column=1)      

        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)

        
class Page_3of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global sprprofit_entry_3of1, rateofpur_entry_3of1, gwill_entry_3of1
        def calculategwill_3of1():
            calsprprofit_entry_3of1 = float(sprprofit_entry_3of1.get())
            calrateofpur_entry_3of1 = float(rateofpur_entry_3of1.get())
            calgwill_3of1 = calsprprofit_entry_3of1 / calrateofpur_entry_3of1 * 100
            gwill_entry_3of1.insert(10,calgwill_3of1)
            
        tk.Label(self, text="Enter Super Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Rate Of Purchase",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)

        sprprofit_entry_3of1 = tk.Entry(self,font=('helvetica',10))
        sprprofit_entry_3of1.grid(row=0,column=1,sticky=W)
        
        rateofpur_entry_3of1 = tk.Entry(self,font=('helvetica',10))
        rateofpur_entry_3of1.grid(row=1,column=1,sticky=W)

        gwill_entry_3of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_3of1.grid(row=2,column=1,sticky=W)

        gwill_button_3of1 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_3of1).grid(row=4,column=1,sticky=W) 
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageThree)).grid(sticky=W)

class Page_3of2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global noofyrpur_entry_3of2,sprprof_entry_3of2, avgprof_entry_3of2, gwill_entry_3of2,norprof_entry_3of2

        def calculatesprprof_3of2():
            calavgprof_entry_3of2 = int(avgprof_entry_3of2.get())
            calnormalprof_entry_3of2 = int(norprof_entry_3of2.get())
            calsprprof_3of2 = calavgprof_entry_3of2 -  calnormalprof_entry_3of2
            sprprof_entry_3of2.insert(10,calsprprof_3of2)
        def calculategwill_3of2():
            calsprprof_entry_3of2_again = float(sprprof_entry_3of2.get())
            calrateofpur_entry_3of2 = float(rateofpur_entry_3of2.get())
            calgwill_3of2 = calsprprof_entry_3of2_again / calrateofpur_entry_3of2 * 100
            gwill_entry_3of2.insert(10,calgwill_3of2)
            
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Normal Profit",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Super Profit is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Rate Of Purchase",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        avgprof_entry_3of2 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_3of2.grid(row=0,column=1,sticky=W)
        
        norprof_entry_3of2 = tk.Entry(self,font=('helvetica',10))
        norprof_entry_3of2.grid(row=1,column=1,sticky=W)

        sprprof_entry_3of2 = tk.Entry(self,font=('helvetica',10))
        sprprof_entry_3of2.grid(row=2,column=1,sticky=W)
        
        rateofpur_entry_3of2 = tk.Entry(self,font=('helvetica',10))
        rateofpur_entry_3of2.grid(row=4,column=1,sticky=W)
        
        gwill_entry_3of2 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_3of2.grid(row=5,column=1,sticky=W)

        sprprof_button_3of2 = tk.Button(self, text="Super Profit",font=('helvetica',14),command=calculatesprprof_3of2).grid(row=3,column=1,sticky=W) 
        gwill_button_3of2 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_3of2).grid(row=6,column=1,sticky=W) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageThree)).grid(sticky=W)
class Page_3of3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Capital Employed is ( Asset - Liabilities)",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="> If Capital Employes is (Capital + Reserved)",font=('helvetica',14)).grid(row=1,column=0,sticky=W)

        
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_3of3of1)).grid(row=0,column=1)      
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_3of3of2)).grid(row=1,column=1)     

        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)
class Page_3of3of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global rateofpur_entry_3of3of1,gwill_entry_3of3of1,rate_entry_3of3of1,sprprof_entry_3of3of1,asset_entry_3of3of1,liab_entry_3of3of1,capemp_entry_3of3of1,avgprof_entry_3of3of1,norprof_entry_3of3of1
        def calculatecapemp_3of3of1():
            calasset_entry_3of3of1= int(asset_entry_3of3of1.get())
            calliab_entry_3of3of1 = int(liab_entry_3of3of1.get())
            calcapemp_3of3of1 = calasset_entry_3of3of1 - calliab_entry_3of3of1
            capemp_entry_3of3of1.insert(10,calcapemp_3of3of1)
        def calculatenorprof_3of3of1():
            calcapemp_entry_3of3of1 = float(capemp_entry_3of3of1.get())
            calrate_entry_3of3of1 = float(rate_entry_3of3of1.get())
            calnorprof_3of3of1 = calcapemp_entry_3of3of1 * calrate_entry_3of3of1 / 100
            norprof_entry_3of3of1.insert(10,calnorprof_3of3of1)
        def calculatesprprof_3of3of1():
            calavgprof_entry_3of3of1 = int(avgprof_entry_3of3of1.get())
            calnorprof_entry_3of3of1 = float(norprof_entry_3of3of1.get())
            calsprprof_3of3of1 = calavgprof_entry_3of3of1 - calnorprof_entry_3of3of1
            sprprof_entry_3of3of1.insert(10,calsprprof_3of3of1)
        def calculategwill_entry_3of3of1():
            calrateofpur_entry_3of3of1 = int(rateofpur_entry_3of3of1.get())
            calsprprof_entry_3of3of1 = float(sprprof_entry_3of3of1.get())
            calgwill_entry_3of3of1 = calsprprof_entry_3of3of1 / rateofpur_entry_3of3of1 * 100 
            gwill_entry_3of3of1.insert(10,calgwill_entry_3of3of1)
            
        tk.Label(self, text="Enter Asset",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Liabilites",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Employed is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Rate",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="Normal Profit is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=7,column=0,sticky=W)
        tk.Label(self, text="Super Profit is",font=('helvetica',14)).grid(row=8,column=0,sticky=W)
        tk.Label(self, text="Enter Rate Of Purchase",font=('helvetica',14)).grid(row=10,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=11,column=0,sticky=W)

        asset_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        asset_entry_3of3of1.grid(row=0,column=1,sticky=W)
        
        liab_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        liab_entry_3of3of1.grid(row=1,column=1,sticky=W)
        
        capemp_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_3of3of1.grid(row=2,column=1,sticky=W)

        rate_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        rate_entry_3of3of1.grid(row=4,column=1,sticky=W)

        norprof_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        norprof_entry_3of3of1.grid(row=5,column=1,sticky=W)

        avgprof_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_3of3of1.grid(row=7,column=1,sticky=W)
                                                    
        sprprof_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        sprprof_entry_3of3of1.grid(row=8,column=1,sticky=W)

        rateofpur_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        rateofpur_entry_3of3of1.grid(row=10,column=1,sticky=W)

        gwill_entry_3of3of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_3of3of1.grid(row=11,column=1,sticky=W)

        tk.Button(self, text="Capital Employed",font=('helvetica',14),command=calculatecapemp_3of3of1).grid(row=3,column=1) 
        tk.Button(self, text="Normal Profit",font=('helvetica',14),command=calculatenorprof_3of3of1).grid(row=6,column=1) 
        tk.Button(self, text="Super Profit",font=('helvetica',14),command=calculatesprprof_3of3of1).grid(row=9,column=1) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_entry_3of3of1).grid(row=12,column=1) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(Page_3of3)).grid(sticky=W)
class Page_3of3of2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global rateofpur_entry_3of3of2,gwill_entry_3of3of2,rate_entry_3of3of2,sprprof_entry_3of3of2,cap_entry_3of3of1,res_entry_3of3of2,capemp_entry_3of3of2,avgprof_entry_3of3of2,norprof_entry_3of3of2
        def calculatecapemp_3of3of2():
            calcap_entry_3of3of2= int(cap_entry_3of3of2.get())
            calres_entry_3of3of2 = int(res_entry_3of3of2.get())
            calcapemp_3of3of2 = calcap_entry_3of3of2 + calres_entry_3of3of2
            capemp_entry_3of3of2.insert(10,calcapemp_3of3of2)
        def calculatenorprof_3of3of2():
            calcapemp_entry_3of3of2 = float(capemp_entry_3of3of2.get())
            calrate_entry_3of3of2 = float(rate_entry_3of3of2.get())
            calnorprof_3of3of2 = calcapemp_entry_3of3of2 * calrate_entry_3of3of2 / 100
            norprof_entry_3of3of2.insert(10,calnorprof_3of3of2)
        def calculatesprprof_3of3of2():
            calavgprof_entry_3of3of2 = float(avgprof_entry_3of3of2.get())
            calnorprof_entry_3of3of2 = float(norprof_entry_3of3of2.get())
            calsprprof_3of3of2 = calavgprof_entry_3of3of2 - calnorprof_entry_3of3of2
            sprprof_entry_3of3of2.insert(10,calsprprof_3of3of2)
        def calculategwill_entry_3of3of2():
            calrateofpur_entry_3of3of2 = float(rateofpur_entry_3of3of2.get())
            calsprprof_entry_3of3of2 = float(sprprof_entry_3of3of2.get())
            calgwill_entry_3of3of2 = calsprprof_entry_3of3of2 / calrateofpur_entry_3of3of2 * 100 
            gwill_entry_3of3of2.insert(10,calgwill_entry_3of3of2)
            
        tk.Label(self, text="Enter Capital",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Reserve",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Employed is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Rate",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="Normal Profit is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=7,column=0,sticky=W)
        tk.Label(self, text="Super Profit is",font=('helvetica',14)).grid(row=8,column=0,sticky=W)
        tk.Label(self, text="Enter Rate Of Purchase",font=('helvetica',14)).grid(row=10,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=11,column=0,sticky=W)

        cap_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        cap_entry_3of3of2.grid(row=0,column=1,sticky=W)
        
        res_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        res_entry_3of3of2.grid(row=1,column=1,sticky=W)
        
        capemp_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_3of3of2.grid(row=2,column=1,sticky=W)

        rate_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        rate_entry_3of3of2.grid(row=4,column=1,sticky=W)

        norprof_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        norprof_entry_3of3of2.grid(row=5,column=1,sticky=W)

        avgprof_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_3of3of2.grid(row=7,column=1,sticky=W)
                                                    
        sprprof_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        sprprof_entry_3of3of2.grid(row=8,column=1,sticky=W)

        rateofpur_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        rateofpur_entry_3of3of2.grid(row=10,column=1,sticky=W)

        gwill_entry_3of3of2 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_3of3of2.grid(row=11,column=1,sticky=W)

        tk.Button(self, text="Capital Employed",font=('helvetica',14),command=calculatecapemp_3of3of2).grid(row=3,column=1) 
        tk.Button(self, text="Normal Profit",font=('helvetica',14),command=calculatenorprof_3of3of2).grid(row=6,column=1) 
        tk.Button(self, text="Super Profit",font=('helvetica',14),command=calculatesprprof_3of3of2).grid(row=9,column=1) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_entry_3of3of2).grid(row=12,column=1) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(Page_3of3)).grid(sticky=W)



class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Capital Value And Capital Employed Is Given",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="> If Capital Value Is Not Given",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="> If Capital Employed Is Not Given ",font=('helvetica',14)).grid(row=2,column=0,sticky=W)


        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_4of1)).grid(row=0,column=1)      
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_4of2)).grid(row=1,column=1)     
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_4of3)).grid(row=2,column=1)      

        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)

class Page_4of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global capval_entry_4of1, capemp_entry_4of1, gwill_entry_4of1
        def calculategwill_4of1():
            calsprprofit_entry_4of1 = float(capval_entry_4of1.get())
            calrateofpur_entry_4of1 = float(capemp_entry_4of1.get())
            calgwill_4of1 = calsprprofit_entry_4of1 - calrateofpur_entry_4of1 
            gwill_entry_4of1.insert(10,calgwill_4of1)
            
        tk.Label(self, text="Enter Capital Value",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Capital Employed",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)

        capval_entry_4of1 = tk.Entry(self,font=('helvetica',10))
        capval_entry_4of1.grid(row=0,column=1,sticky=W)
        
        capemp_entry_4of1 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_4of1.grid(row=1,column=1,sticky=W)

        gwill_entry_4of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_4of1.grid(row=2,column=1,sticky=W)

        gwill_button_4of1 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_4of1).grid(row=4,column=1,sticky=W) 
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFour)).grid(sticky=W)

class Page_4of2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global capemp_entry_4of2,rate_entry_4of2, avgprof_entry_4of2, gwill_entry_4of2,capval_entry_4of2 

        def calculatecapval_4of2():
            calavgprof_entry_4of2 = float(avgprof_entry_4of2.get())
            calrate_entry_4of2 = float(rate_entry_4of2.get())
            calcapval_4of2 = calavgprof_entry_4of2 * 100 / calrate_entry_4of2
            capval_entry_4of2.insert(10,calcapval_4of2)
        def calculategwill_4of2():
            calcapval_entry_4of2= float(capval_entry_4of2.get())
            calcapemp_entry_4of2 = float(capemp_entry_4of2.get())
            calgwill_4of2 = calcapval_entry_4of2 - calcapemp_entry_4of2
            gwill_entry_4of2.insert(10,calgwill_4of2)
            
        tk.Label(self, text="Enter Average Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Rate",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Value is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Capital Employed",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        avgprof_entry_4of2 = tk.Entry(self,font=('helvetica',10))
        avgprof_entry_4of2.grid(row=0,column=1,sticky=W)
        
        rate_entry_4of2 = tk.Entry(self,font=('helvetica',10))
        rate_entry_4of2.grid(row=1,column=1,sticky=W)

        capval_entry_4of2 = tk.Entry(self,font=('helvetica',10))
        capval_entry_4of2.grid(row=2,column=1,sticky=W)

        capemp_entry_4of2 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_4of2.grid(row=4,column=1,sticky=W)
        
        gwill_entry_4of2 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_4of2.grid(row=5,column=1,sticky=W)

        sprprof_button_4of2 = tk.Button(self, text="Capital Value",font=('helvetica',14),command=calculatecapval_4of2).grid(row=3,column=1,sticky=W) 
        gwill_button_4of2 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_4of2).grid(row=6,column=1,sticky=W) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFour)).grid(sticky=W)
class Page_4of3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Capital Employed is ( Asset - Liabilities)",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="> If Capital Employes is (Capital + Reserved)",font=('helvetica',14)).grid(row=1,column=0,sticky=W)

        
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_4of3of1)).grid(row=0,column=1)      
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_4of3of2)).grid(row=1,column=1)     

        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)


class Page_4of3of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global capval_entry_4of3of1,asset_entry_4of3of1,liab_entry_4of3of1,capemp_entry_4of3of1,noofyrpur_entry_4of3of1,gwill_entry_4of3of1
        def calculatecapemp_4of3of1():
            calasset_entry_4of3of1= int(asset_entry_4of3of1.get())
            calliab_entry_4of3of1 = int(liab_entry_4of3of1.get())
            calcapemp_4of3of1 = calasset_entry_4of3of1 - calliab_entry_4of3of1
            capemp_entry_4of3of1.insert(10,calcapemp_4of3of1)

        def calculategwill_4of3of1():
            calcapemp_entry_4of3of1 = float(capemp_entry_4of3of1.get())
            calcapval_entry_4of3of1 = float(capval_entry_4of3of1.get())
            calgwill_4of3of1 = calcapval_entry_4of3of1 - calcapemp_entry_4of3of1
            gwill_entry_4of3of1.insert(10,calgwill_4of3of1)
    
            
        tk.Label(self, text="Enter Asset",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Liabilites",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Employed is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Capital Value ",font=('helvetica',14)).grid(row=4,column=0,sticky=W)

        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        asset_entry_4of3of1 = tk.Entry(self,font=('helvetica',10))
        asset_entry_4of3of1.grid(row=0,column=1,sticky=W)
        
        liab_entry_4of3of1 = tk.Entry(self,font=('helvetica',10))
        liab_entry_4of3of1.grid(row=1,column=1,sticky=W)
        
        capemp_entry_4of3of1 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_4of3of1.grid(row=2,column=1,sticky=W)

        capval_entry_4of3of1 = tk.Entry(self,font=('helvetica',10))
        capval_entry_4of3of1.grid(row=4,column=1,sticky=W)

       
        gwill_entry_4of3of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_4of3of1.grid(row=5,column=1,sticky=W)

        tk.Button(self, text="Capital Employed",font=('helvetica',14),command=calculatecapemp_4of3of1).grid(row=3,column=1) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_4of3of1).grid(row=6,column=1) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(Page_4of3)).grid(sticky=W)

class Page_4of3of2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global capval_entry_4of3of2,cap_entry_4of3of2,res_entry_4of3of2,capemp_entry_4of3of2,noofyrpur_entry_4of3of2,gwill_entry_4of3of2
        def calculatecapemp_4of3of2():
            calcap_entry_4of3of2= int(cap_entry_4of3of2.get())
            calres_entry_4of3of2 = int(res_entry_4of3of2.get())
            calcapemp_4of3of2 = calcap_entry_4of3of2 + calres_entry_4of3of2
            capemp_entry_4of3of2.insert(10,calcapemp_4of3of2)

        def calculategwill_4of3of2():
            calcapemp_entry_4of3of2 = float(capemp_entry_4of3of2.get())
            calcapval_entry_4of3of2 = float(capval_entry_4of3of2.get())
            calgwill_4of3of2 = calcapval_entry_4of3of2 - calcapemp_entry_4of3of2
            gwill_entry_4of3of2.insert(10,calgwill_4of3of2)
    
            
        tk.Label(self, text="Enter Capital",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Reserve",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Capital Employed is",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="Enter Capital Value ",font=('helvetica',14)).grid(row=4,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=5,column=0,sticky=W)

        cap_entry_4of3of2 = tk.Entry(self,font=('helvetica',10))
        cap_entry_4of3of2.grid(row=0,column=1,sticky=W)
        
        res_entry_4of3of2 = tk.Entry(self,font=('helvetica',10))
        res_entry_4of3of2.grid(row=1,column=1,sticky=W)
        
        capemp_entry_4of3of2 = tk.Entry(self,font=('helvetica',10))
        capemp_entry_4of3of2.grid(row=2,column=1,sticky=W)

        capval_entry_4of3of2 = tk.Entry(self,font=('helvetica',10))
        capval_entry_4of3of2.grid(row=4,column=1,sticky=W)

       
        gwill_entry_4of3of2 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_4of3of2.grid(row=5,column=1,sticky=W)

        tk.Button(self, text="Capital Employed",font=('helvetica',14),command=calculatecapemp_4of3of2).grid(row=3,column=1) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_4of3of2).grid(row=6,column=1) 


        
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(Page_4of3)).grid(sticky=W)



class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="> If Total Profit and Total Weight Is Given",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        #tk.Label(self, text="> If Total Profit and Total Weight Is Not Given",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="> If Total Profit and Total Weight Is Not Given",font=('helvetica',14)).grid(row=2,column=0,sticky=W)

        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_5of1)).grid(row=0,column=1)      
        #tk.Button(self, text="Find",font=('helvetica',14),
                                #command=lambda:master.switch_frame(Page_5of2)).grid(row=1,column=1)     
        tk.Button(self, text="Find",font=('helvetica',14),
                                command=lambda:master.switch_frame(Page_5of3)).grid(row=2,column=1)
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(StartPage)).grid(sticky=W)

class Page_5of1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        global totprod_entry_5of1, wei_entry_5of1, gwill_entry_5of1,noofyrpur_entry_5of1
        
        def calculategwill_5of1():
            caltotprod_entry_5of1 = float(totprod_entry_5of1.get())
            calwei_entry_5of1 = float(wei_entry_5of1.get())
            calnoofyrpur_entry_5of1 = float(noofyrpur_entry_5of1.get())
            calgwill_5of1 = (caltotprod_entry_5of1 / calwei_entry_5of1 ) * calnoofyrpur_entry_5of1
            gwill_entry_5of1.insert(10,calgwill_5of1)
            
        tk.Label(self, text="Enter Total Product",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Total Weight",font=('helvetica',14)).grid(row=1,column=0,sticky=W)
        tk.Label(self, text="Enter No Of Year Purchase",font=('helvetica',14)).grid(row=2,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=3,column=0,sticky=W)

        totprod_entry_5of1 = tk.Entry(self,font=('helvetica',10))
        totprod_entry_5of1.grid(row=0,column=1,sticky=W)
        
        wei_entry_5of1 = tk.Entry(self,font=('helvetica',10))
        wei_entry_5of1.grid(row=1,column=1,sticky=W)
        
        noofyrpur_entry_5of1 = tk.Entry(self,font=('helvetica',10))
        noofyrpur_entry_5of1.grid(row=2,column=1,sticky=W) 
        

        gwill_entry_5of1 = tk.Entry(self,font=('helvetica',10))
        gwill_entry_5of1.grid(row=3,column=1,sticky=W)

        gwill_button_4of1 = tk.Button(self, text="Goodwill",font=('helvetica',14),command=calculategwill_5of1).grid(row=4,column=1,sticky=W) 
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFive)).grid(sticky=W)
'''
class Page_5of2(tk.Frame):
    def __init__(self, master):
        global noofyrs_entry_5of2,createentry_5of2
        tk.Frame.__init__(self, master)
        def nnoofentry():
            global ent,ynt
            root = Tk()
            calnoofyrs_entry_5of2 = int(noofyrs_entry_5of2.get())
            def netprof():
                calent = int(ent.get())
                calynt = int(ynt.get())
                print(calent)
                print(calynt)
                
            for i in range(calnoofyrs_entry_5of2):
               
                Label(root,text="Enter Profit ",font=('helvetica',14)).grid(sticky=W)
                
                ent = Entry(root)
                ent.grid(sticky=W)
                Label(root,text="Enter Weight",font=('helvetica',14)).grid(sticky=W)
                ynt = Entry(root)
                ynt.grid(sticky=W)
                
                
            
            btn_ent = Button(root,text="Net Profit",command=netprof).grid(sticky=W)
            Btn_ynt = Button(root,text="Net Weight").grid(sticky=W)
                
                
        

        tk.Label(self, text="Enter No of years",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        noofyrs_entry_5of2 = tk.Entry(self,font=('helvetica',10))
        noofyrs_entry_5of2.grid(row=0,column=1,sticky=W)
        
        
        tk.Button(self, text="create",font=('helvetica',14),command=nnoofentry).grid(row=2,column=1,sticky=W) 
        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFive)).grid(sticky=W)
'''
class Page_5of3(tk.Frame):
    def __init__(self, master):
        global gwill_5of3,calnoofyrpur_5of3,calins1_5of3,calins_5of3,entry1_5of3,entry2_5of3,entry3_5of3,entry4_5of3,entry5_5of3,entry11_5of3,entry22_5of3,entry33_5of3,entry44_5of3,entry55_5of3
        tk.Frame.__init__(self, master)

        def gwill():
            calculateins_5of3 = float(calins_5of3.get())
            calculateins1_5of3 = float(calins1_5of3.get())
            calculatenoofyrpur_5of3 = int(calnoofyrpur_5of3.get())
            calnetval = (calculateins_5of3/calculateins1_5of3) * calculatenoofyrpur_5of3
            gwill_5of3.insert(10,calnetval)
            
            
        def netprof():
            try:
                try:
                    try:
                        try:
                            calentry1_5of3 = int(entry1_5of3.get())
                            calentry2_5of3 = int(entry2_5of3.get())
                            calentry3_5of3 = int(entry3_5of3.get())
                            calentry4_5of3 = int(entry4_5of3.get())
                            calentry5_5of3 = int(entry5_5of3.get())
                            calnetprof_5of3 = calentry1_5of3 + calentry2_5of3 + calentry3_5of3 + calentry4_5of3 + calentry5_5of3
                            calins_5of3.insert(10,calnetprof_5of3)
                        except:
                            calentry1_5of3 = int(entry1_5of3.get())
                            calentry2_5of3 = int(entry2_5of3.get())
                            calentry3_5of3 = int(entry3_5of3.get())
                            calentry4_5of3 = int(entry4_5of3.get())
                            calnetprof_5of3 = calentry1_5of3 + calentry2_5of3 + calentry3_5of3 + calentry4_5of3 
                            calins_5of3.insert(10,calnetprof_5of3)
                    except:
                        calentry1_5of3 = int(entry1_5of3.get())
                        calentry2_5of3 = int(entry2_5of3.get())
                        calentry3_5of3 = int(entry3_5of3.get())
                        calnetprof_5of3 = calentry1_5of3 + calentry2_5of3 + calentry3_5of3
                        calins_5of3.insert(10,calnetprof_5of3)
                except:
                    calentry1_5of3 = int(entry1_5of3.get())
                    calentry2_5of3 = int(entry2_5of3.get())
                    calnetprof_5of3 = calentry1_5of3 + calentry2_5of3 
                    calins_5of3.insert(10,calnetprof_5of3)
            except:
                calentry1_5of3 = int(entry1_5of3.get())
                calins_5of3.insert(10,calentry1_5of3)


                
                                      
        def netweight():
            try:
                try:
                    try:
                        try:
                            calentry11_5of3 = int(entry11_5of3.get())
                            calentry22_5of3 = int(entry22_5of3.get())
                            calentry33_5of3 = int(entry33_5of3.get())
                            calentry44_5of3 = int(entry44_5of3.get())
                            calentry55_5of3 = int(entry55_5of3.get())
                            calnetprof_5of3 = calentry11_5of3 + calentry22_5of3 + calentry33_5of3 + calentry44_5of3 + calentry55_5of3
                            calins1_5of3.insert(10,calnetprof_5of3)
                        except:
                            calentry11_5of3 = int(entry11_5of3.get())
                            calentry22_5of3 = int(entry22_5of3.get())
                            calentry33_5of3 = int(entry33_5of3.get())
                            calentry44_5of3 = int(entry44_5of3.get())
                            calnetprof_5of3 = calentry11_5of3 + calentry22_5of3 + calentry33_5of3 + calentry44_5of3
                            calins1_5of3.insert(10,calnetprof_5of3)
            
            
                    except:
                        calentry11_5of3 = int(entry11_5of3.get())
                        calentry22_5of3 = int(entry22_5of3.get())
                        calentry33_5of3 = int(entry33_5of3.get())
                        calnetprof_5of3 = calentry11_5of3 + calentry22_5of3 + calentry33_5of3
                        calins1_5of3.insert(10,calnetprof_5of3)
                
         
                except:
                    calentry11_5of3 = int(entry11_5of3.get())
                    calentry22_5of3 = int(entry22_5of3.get())
                    calnetprof_5of3 = calentry11_5of3 + calentry22_5of3 
                    calins1_5of3.insert(10,calnetprof_5of3)
            except:
                calentry11_5of3 = int(entry11_5of3.get())
                calins1_5of3.insert(10,calentry11_5of3)
                    


                                                    
          

                            
                
                
                      
        tk.Label(self, text="Enter Profit",font=('helvetica',14)).grid(row=0,column=0,sticky=W)
        tk.Label(self, text="Enter Weight",font=('helvetica',14)).grid(row=0,column=1,sticky=E,pady=10)
        tk.Label(self, text="Enter No Of Year Purchase",font=('helvetica',14)).grid(row=8,column=0,sticky=W)
        tk.Label(self, text="The Calculated Goodwill is",font=('helvetica',14)).grid(row=9,column=0)

        entry1_5of3 = tk.Entry(self,font=('helvetica',10))
        entry1_5of3.grid(row=1,column=0,sticky=W)

        entry2_5of3 = tk.Entry(self,font=('helvetica',10))
        entry2_5of3.grid(row=2,column=0,sticky=W)
        
        entry3_5of3 = tk.Entry(self,font=('helvetica',10))
        entry3_5of3.grid(row=3,column=0,sticky=W)
        
        entry4_5of3 = tk.Entry(self,font=('helvetica',10))
        entry4_5of3.grid(row=4,column=0,sticky=W)

        entry5_5of3 = tk.Entry(self,font=('helvetica',10))
        entry5_5of3.grid(row=5,column=0,sticky=W)
        
        calins_5of3 = tk.Entry(self,font=('helvetica',10))
        calins_5of3.grid(row=7,column=0,sticky=W,pady=10)
        
        entry11_5of3 = tk.Entry(self,font=('helvetica',10))
        entry11_5of3.grid(row=1,column=1,sticky=E)

        entry22_5of3 = tk.Entry(self,font=('helvetica',10))
        entry22_5of3.grid(row=2,column=1,sticky=E)
        
        entry33_5of3 = tk.Entry(self,font=('helvetica',10))
        entry33_5of3.grid(row=3,column=1,sticky=E)
        
        entry44_5of3 = tk.Entry(self,font=('helvetica',10))
        entry44_5of3.grid(row=4,column=1,sticky=E)

        entry55_5of3 = tk.Entry(self,font=('helvetica',10))
        entry55_5of3.grid(row=5,column=1,sticky=E)
        
        calins1_5of3 = tk.Entry(self,font=('helvetica',10))
        calins1_5of3.grid(row=7,column=1,sticky=W)

        calnoofyrpur_5of3 = tk.Entry(self,font=('helvetica',10))
        calnoofyrpur_5of3.grid(row=8,column=1)
        
        gwill_5of3 = tk.Entry(self,font=('helvetica',10))
        gwill_5of3.grid(row=9,column=1)
        
        tk.Button(self, text="Net Profit",font=('helvetica',14),command=netprof).grid(row=6,column=0,sticky=W)
        tk.Button(self, text="Net Weight",font=('helvetica',14),command=netweight).grid(row=6,column=1,sticky=E) 
        tk.Button(self, text="Goodwill",font=('helvetica',14),command=gwill).grid(row=10,column=1) 


        tk.Button(self, text="Back",font=('helvetica',14),
                  command=lambda: master.switch_frame(PageFive)).grid(sticky=W,pady=10)




if __name__ == "__main__":

    

    app = SampleApp()
    app.title("Goodwill Calculator")
    app.iconbitmap('icon.ico')
    app.mainloop()

