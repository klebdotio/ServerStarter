import shlex
import subprocess
from appJar import gui
import sys
import time

# *********** INSTALLATION ************
# Run the following commands to ensure
# the program runs correctly:
# pip install shlex
# pip install subprocess
# pip install appJar
# pip install sys
# pip install time
# Thanks to DataCorruption for the server starting code!

# DANGER! DO NOT EDIT THIS LINE
app = gui("ServerStarter")
# Well almost certainly break the program!

app.addLabel("title", "ServerStarter by klebdotio")
app.setLabelBg("title", "red")
app.addLabelEntry("RAM (GB)")
app.addLabelEntry("Server Jar")
app.addLabel("l1", "")


def press(button):
    if button == "Start Server":
        print("Starting...")
        ram = app.getEntry("RAM (GB)")
        srv = app.getEntry("Server Jar")
        serverstart = "java -Xmx" + ram + "G -Xms" + ram + "G -jar " + srv
        app.setLabel("l1", "Starting " + srv + " with " + ram + "GB of RAM")
        time.sleep(2)
        app.hide()
        process = subprocess.Popen(shlex.split(serverstart), stdout=subprocess.PIPE, bufsize=1)
        for line in iter(process.stdout.readline, b''):
            line = line.decode()
            print(line, end="")

    elif button == "Close":
        sys.exit()


app.addButtons(["Start Server", "Close"], press)

app.go()
