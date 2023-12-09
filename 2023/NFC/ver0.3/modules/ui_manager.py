# coding: utf-8

import tkinter as tk
import tkinter.ttk as ttk



class UIManager():

	def __init__(self, on_start, on_stop):
		print("UIManager")

		# Main Window
		root = tk.Tk()
		root.title("= NFC System =")
		root.geometry("480x320")

		# Frame
		frame = ttk.Frame(root)
		frame.pack(fill=tk.BOTH, padx=20,pady=10)

		# Btn
		self.set_btn(frame, "Start", on_start)
		self.set_btn(frame, "Stop", on_stop)
		self.set_btn(frame, "Quit", lambda: exit(0))

		root.mainloop()

	def set_btn(self, frame, label, on_start):

		# Label
		text = tk.StringVar(frame)
		text.set(label)

		# Button
		button = tk.Button(frame, textvariable=text, command=on_start)
		button.pack()
