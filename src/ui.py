# SsTeX - Screenshot to LaTeX tool
# Copyright (C) 2026 mmichaellangelo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk

import config
import webbrowser

cfg: config.SsTeXConfig = None

root = tk.Tk()
root.withdraw()

# String variable for dynamic error/success messages
msg = tk.StringVar(root, value='')

label_link_apikey = tk.Label(root, text="Get a Gemini API key", cursor='hand2', fg='blue')
label_link_apikey.pack()
label_link_apikey.bind('<Button-1>', lambda e: webbrowser.open('https://ai.google.dev/gemini-api/docs/api-key'))

tk.Label(root, text="Gemini API Key:").pack()
entry_apikey = tk.Entry(root, show='*')
entry_apikey.pack()

def update_api_key():
    api_key = entry_apikey.get()
    api_key = api_key.strip()
    if api_key == '':
        msg.set("Invalid API Key.")
        return
    cfg.api_key = api_key
    cfg.save()
    msg.set("API key updated.")
    

button_update_apikey = tk.Button(root, text="Update API key", command=update_api_key)
button_update_apikey.pack()
tk.Label(root, textvariable=msg).pack()

def start_hidden():
    root.mainloop()

def show(conf: config.SsTeXConfig):
    global cfg
    cfg = conf
    root.mainloop()

def hide():
    root.withdraw()
