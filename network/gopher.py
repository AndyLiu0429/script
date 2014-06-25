# -*- coding: utf-8 -*-
__author__ = 'liutianyuan'

import sys, urllib2
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase


msg = """dada"""
msg = MIMEText(msg)
msg["TO"] = 'dad'
print msg.as_string()