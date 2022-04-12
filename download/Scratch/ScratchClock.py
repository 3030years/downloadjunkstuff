from scratchclient import ScratchSession

Session = ScratchSession("YOUR USERNAME", "YOUR PASSWORD")
connection = Session.create_cloud_connection("PROJECT ID")


@connection.on("set")
def on_set(variable):
    print(variable.name, variable.value)
