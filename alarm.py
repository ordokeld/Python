import time
import datetime
import pygame

def run_alarm(alarm_time):
    print(f"Будильник восстановлен на {alarm_time}")
    sound=r"media\1.mp3"
    is_running=True
    while is_running:
     current_time=datetime.datetime.now().strftime("%H:%M:%S")
     print(current_time)

     if current_time==alarm_time:
         print("Просыпайся друг!")

         pygame.mixer.init()
         pygame.mixer.music.load()
         pygame.mixer.music.play()

         while pygame.mixer.music.get_busy():
               time.sleep(1)
        
    is_running=False

    time.sleep(1)

run_alarm("13:07:10")

