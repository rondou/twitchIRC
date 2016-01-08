import socket, string

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "" #your nick name
PASS = "oauth:" #your irc pass word
readbuffer = ""
MODT = False

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN #asiagodtonegg3be0 \r\n") #Want to join the chat room name

def sendMessage(message):
    s.send("PRIVMSG #asiagodtonegg3be0:" + message + "\r\n")

while(True):
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        if (line[0] == "PING"):
            s.send("PONG %s\r\n" % line[1])
        else:
            parts = string.split(line, ":")

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    message = parts[2][:len(parts[2]) - 1]
                except:
                    message = ""

                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]

                if MODT:
                    print (username + ": " + message)

                    if message == "Hey":
                        sendMessage("Welcome to my stream, " + username)

                for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True