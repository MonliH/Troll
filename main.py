import random
import time
import webbrowser

while True:
    pages = random.choice(["trollface.dk", "www.youtube.com/watch?v=2VXacYLcjGA",\
    "media.giphy.com/media/eVy46EWyclTIA/giphy.gif"])
    visit = "https://{}".format(pages)
    timeWait = random.randrange(1, 3)
    time.sleep(timeWait)
    webbrowser.open(pages)
