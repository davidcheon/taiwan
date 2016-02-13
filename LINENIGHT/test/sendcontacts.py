#!/usr/bin/python
#!-*- coding:utf-8 -*-
import sys
import contactstools

id,pwd,device=sys.argv[1:]
client=contactstools.mycontactsender(id,pwd,device)
client.sendaction()

