from tkinter import *
import pyshorteners
import paperclip

def url_shortner():
    shortener = pyshorteners.Shortener()
    url_short = shortener.tinyurl.short(main_url.get())
  
    short_url.set(url_short)

def copy_url():
    #copy short url on clipboard
    paperclip.copy( short_url.get())

if __name__=="__main__":
    root = Tk()
    root.geometry("700x400")
    root.title("My URL Shortener App")
    root.configure(bg="lavender")

    main_url = StringVar()
    short_url= StringVar()
    
    Label(root, text="Enter The Main URL", font="timesnewroman").pack(pady=5)
    Entry(root,textvariable=main_url, width =100).pack(pady=5)
    Button(root, text="Generate Short URL", command =url_shortner).pack(pady=5)

    Label(root, text="The Short URL ", font="timesnewroman").pack(pady=5)
    Entry(root, textvariable= short_url, width=50).pack(pady=5)
    Button(root, text="Copy the Short URL", command= copy_url).pack(pady=5)
    root.mainloop()
