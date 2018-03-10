import random
import time
import webbrowser

while True:
    pages = random.choice(["trollface.dk", "www.youtube.com/watch?v=2VXacYLcjGA",\  # Websites to open
    "media.giphy.com/media/eVy46EWyclTIA/giphy.gif"])
    visit = "https://{}".format(pages)
    timeWait = random.randrange(1, 3)  # Delay
    time.sleep(timeWait)
    webbrowser.open(pages)  # Open Pages
