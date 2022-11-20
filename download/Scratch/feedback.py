import scratchattach as scratch3
from scratchattach import Encoding


events = scratch3.CloudEvents("(Your project ID)")

@events.event
def on_set(event):
    if event.var == "FeedBack":
        print(Encoding.decode(event.value))


@events.event
def on_ready():
    print("Feedback listener ready!")


events.start()
