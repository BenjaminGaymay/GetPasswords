#!/usr/bin/env python3
""" Envoyer un mail """

import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
except:
    print('Something went wrong...')