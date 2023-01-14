import tkinter as tk
import tkinter.ttk

import FMCLView.Const
import FMCLView.Pages.AccountPage
import FMCLView.Pages.UnderDevelop
import FMCLView.Pages.LaunchPage



def main():
    root = tk.Tk()
    root.title("First Minecraft Launcher")
    root.geometry("500x375")
    root.resizable(False, False)

    maintab = tk.ttk.Notebook(root, width=480, height=330)

    maintab.add(FMCLView.Pages.LaunchPage.main(), text=FMCLView.Const.get("Main.Notebook.Launch"))
    maintab.add(FMCLView.Pages.UnderDevelop.main(), text=FMCLView.Const.get("Main.Notebook.Download"))
    maintab.add(FMCLView.Pages.UnderDevelop.main(), text=FMCLView.Const.get("Main.Notebook.Option"))
    maintab.add(FMCLView.Pages.AccountPage.main(), text=FMCLView.Const.get("Main.Notebook.Accounts"))
    maintab.add(FMCLView.Pages.UnderDevelop.main(), text=FMCLView.Const.get("Main.Notebook.Gaming"))
    maintab.add(FMCLView.Pages.UnderDevelop.main(), text=FMCLView.Const.get("Main.Notebook.About"))


    maintab.place(x=10, y=10)

    root.mainloop()
