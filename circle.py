import tkinter as tk





class myapps:
        
    def __init__(self,root:tk.Tk,widths:int,heights:int,backgrounds:str,colors:list,divs:int):
        self.root=root
        self.root.title("oval")
        self.root.geometry(str(widths)+"x"+str(heights))
        self.root.configure(background=backgrounds)
        self.colors=colors
        self.canvas=tk.Canvas(background=backgrounds,width=widths,height=heights)
        self.canvas.pack(padx=0,pady=0)
        canv=self.canvas
        self.divs=widths//divs//2
        counters=0
        for a in range(divs):
            aa=a*self.divs
            aaa=widths-aa
            b=a & 1
            canv.create_oval(aa,aa,aaa,aaa,fill=self.colors[counters])
            counters=counters+1
            if counters>len(self.colors)-1:
                counters=0




def starts(widths:int,heights:int,backgrounds:str,colors:list,divs:int):
    root=tk.Tk()
    apps=myapps(root,widths,heights,backgrounds,colors,divs)
    root.mainloop()



colors=["white","black"]
divs=10
backgrounds="black"
widths=480
heights=480
starts(widths,heights,backgrounds,colors,divs)