#kivy files
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
from kivy.uix.image import Image
#mobile phone
#from android.storage import primary_external_storage_path
#primary_ext_storage = primary_external_storage_path()

#importing needed files
import requests
from bs4 import BeautifulSoup
import sys
import urllib3
import domain

class DomainWindow(TabbedPanel, Screen):
    domains = []
    def add(self, value):

        if value != "" and ".com" in value:
            DomainWindow.domains.append(value)
            self.ids.H_input.text = ""
            self.ids.status.text= f"List : {DomainWindow.domains}"
        else:
            self.ids.status.text = "Error: The Domain Must include .com with it"

    def remove(self, value):
        try:
            if ".com" in value:
                   DomainWindow.domains.remove(value)
                   self.ids.status.text = f"List: {DomainWindow.domains}"
                   self.ids.remove_text.text = ""
            else:
                self.ids.status.text = f"Error: The domain must comtain .com"
                self.ids.remove_text.text = ""
        except:
            self.ids.status.text = f"Error: The domain you entered not found -->{value}"
            self.ids.remove_text.text = ""

    def exit(self):
        sys.exit(1)
    
    def clear(self):
        DomainWindow.domains.clear()
        self.ids.status.text= f"List Cleared: {DomainWindow.domains}"


    def show(self):
        self.ids.status.text= f"List: {DomainWindow.domains}"

    def Attack(self, name):
        if ".txt" in name:
            name = f"/storage/emulated/0/{name}"
            self.ids.host_input.text = ""
        elif "." not in name or name == "":
            name = f"/storage/emulated/0/{name}Generator.txt"
            self.ids.host_input.text = ""
        else:
            self.ids.status.text = f"Enter extention .txt only -->{name}"
            self.ids.host_input.text = ""
            name = f"/storage/emulated/0/Generator.txt"
        subdomains = []    
        ips =['0.0.0.0', '0.0.0.1', '127.0.0.1' , '8.8.8.8' , '8.8.4.4']
                       
        domain.first(name)
        self.ids.status.text=("\n░█▀▀█ █▀▀ ▀▀█▀▀ █──█ █▀▀ █▀▀█ ─▀─ █▀▀▄ █▀▀▀ 　 ▀█▀ █▀▀▄ █▀▀ █▀▀█ ─ ─ ─ \n░█─▄▄ █▀▀ ──█── █▀▀█ █▀▀ █▄▄▀ ▀█▀ █──█ █─▀█ 　 ░█─ █──█ █▀▀ █──█ ▄ ▄ ▄  \n░█▄▄█ ▀▀▀ ──▀── ▀──▀ ▀▀▀ ▀─▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▄█▄ ▀──▀ ▀── ▀▀▀▀ █ █ █\n\n")
    
        for t in DomainWindow.domains:
            target = t
            try:
                req2 = requests.get(f'https://webiplookup.com/{target}/domain.htm')
            except:
                self.ids.status.text=("[*]CONNECTION FAILED PLEASE CHECK YOUR NETWORK CONNECTION [*]")
            #req2
            try:
                website = req2.text
                soup = BeautifulSoup(website, features = "html.parser")
            except:
                self.ids.status.text=("[*] GETTING ERROR! ")

            if req2.status_code != 200:
                self.ids.status.text=(f'[*] Information not Available For that Target: {target}')

            #req2
            for link in soup.find_all("a", attrs={"target": "_blank"}):
                d = str(link.get_text())
                if target in d:
                    subdomains.append(d)
                else:
                    pass
            self.ids.status.text=(f"\n[!] TARGETED ATTACK : {target}\n")
            Tries = sorted(set(subdomains))
        old = ""
        for w in Tries:
            old = f"{old}\n{w}\n"
            self.ids.status.text=(f'{old}\n')
            if name is not None:
                domain.Make_file3(w, name,ips)
            else:
                self.ids.status.text="Enter file name"

        domain.Last(name)
        self.ids.status.text=(f"{old}\n\n[!!]Data collected Subscribe(youtube.com/channel/UCP-5_1vvVXzjbF4iLm5Yb4w) for more tools [Request for any tools]\n")

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("design.kv")
class DomainConfigApp(App):
    def build(self):
        Window.clearcolor = (28/255, 33/255, 38/255, 1)
        return kv


if __name__ == "__main__":
    DomainConfigApp().run()