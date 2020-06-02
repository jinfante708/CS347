from tkinter import *
from car import Car
import time

root = Tk()
car = Car()
speed_var = StringVar()
cc_status = StringVar()
cc_speed = StringVar()
text_box = Listbox(root, width = 100, height = 15)
text_box.pack(side='bottom')

def update_car_speed():
    speed_var.set(str(car.get_current_speed()))

def update_cc_status():
    if car.get_cc_status():
        cc_status.set("ON")
    else:
        cc_status.set("OFF")

def update_cc_speed():
    cc_speed.set(car.get_cc_speed())

def add_text(message):
    text_box.insert(END, message + "\n")
    
def activate():
    car.activate_cc()
    update_cc_speed()
    update_cc_status()

def deactivate():
    car.deactivate_cc()
    car.clear_cc_speed()
    update_cc_speed()
    update_cc_status()

def cancel(event):
    deactivate()
    
def set_cc(event):
    if car.set_cc_speed():
        activate()
    else: 
        add_text("Error: Current speed not in range. (>= 10 && <= 90)")

def incr_cc(event):
    if car.get_cc_status():
        car.increment_cc()
        update_cc_speed()
        car.increment()
        update_car_speed()

        if not car._cruise_control.check_range(car.get_cc_speed()):
            deactivate()
    else:
        add_text("Error: Cannot increment cruise control speed. Cruise control is not activated.")

def decr_cc(event):
    if car.get_cc_status():
        car.decrement_cc()
        update_cc_speed()
        car.decrement()
        update_car_speed()

        if not car._cruise_control.check_range(car.get_cc_speed()):
            deactivate()
    else:
         add_text("Error: Cannot decrement cruise control speed. Cruise control is not activated.")

def apply_gas_pedal(event):
    car.increment()
    update_car_speed()

def apply_brake(event):
    if car.get_current_speed() > 0:
        car.decrement()
        update_car_speed()
    car.deactivate_cc()
    car.clear_cc_speed()
    update_cc_speed()
    update_cc_status()

def download(event):
    file_name = "log_file.txt"
    file = open(file_name, "w")

    logs = car.get_logs()
    for log in logs:
        file.write(log.__str__() + "\n")
    file.close()
    add_text("Logs have been saved to file: " + file_name)

def main():
    root.title("Cruise Control Software")
    root.geometry("1000x750")
    root.configure(background="grey")

    speed_var.set(str(car.get_current_speed()))
    cc_status.set("OFF")
    cc_speed.set(car.get_cc_speed())

    speed_frame = LabelFrame(root, text="Current Speed")
    speed_label = Label(speed_frame, textvariable=speed_var, width=25, height=3)
    speed_frame.pack(side='top')
    speed_label.pack()

    cc_speed_frame = LabelFrame(root, text="Cruise Control Speed")
    cc_speed_label = Label(cc_speed_frame, textvariable=cc_speed, width=25, height=3)
    cc_speed_frame.pack(side='top')
    cc_speed_label.pack()

    cc_frame = LabelFrame(root, text="Cruise Control Status")
    cc_label = Label(cc_frame, textvariable=cc_status, width=25, height=3)
    cc_frame.pack(side='top')
    cc_label.pack()

    acc_btn = Button(root, text="Gas Pedal", width=10, height=2)
    acc_btn.bind("<ButtonRelease-1>", apply_gas_pedal)
    acc_btn.pack(side='top')

    dcc_btn = Button(root, text="Brake", width=10, height=2)
    dcc_btn.bind("<ButtonRelease-1>", apply_brake)
    dcc_btn.pack(side='top')

    set_btn = Button(root, text="Set Cruise Control", width=15, height=2)
    set_btn.bind("<ButtonRelease-1>", set_cc)
    set_btn.pack(side='top')

    cancel_btn = Button(root, text="Cancel Cruise Control", width=15, height=2)
    cancel_btn.bind("<ButtonRelease-1>", cancel)
    cancel_btn.pack(side='top')

    incr_btn = Button(root, text="Increment CC Speed", width=15, height=2)
    incr_btn.bind("<ButtonRelease-1>", incr_cc)
    incr_btn.pack(side='top')

    decr_btn = Button(root, text="Decrement CC Speed", width=15, height=2)
    decr_btn.bind("<ButtonRelease-1>", decr_cc)
    decr_btn.pack(side='top')

    download_btn = Button(root, text="Download Logs", width=15, height=2)
    download_btn.bind("<ButtonRelease-1>", download)
    download_btn.pack(side='top')

    root.mainloop()

if __name__ == "__main__":
    main()