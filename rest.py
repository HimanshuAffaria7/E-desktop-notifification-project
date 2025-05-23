from plyer import notification
import time 

if __name__== '__main__':
    while True:
       notification.notify(
         title ="*** ALERT!!! ALERT!!!***",
         message = "rest is vital for better mental health,increased concentration and memory, a healtier imune system, reduced stress, improved mood and even better metabolism.",
         app_icon ="E:/desktop notifification project/rest.ico",
         timeout = 5)
       time.sleep(10)
       