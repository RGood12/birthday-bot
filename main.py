# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import json
from bd.messages import date_suffix, David_and_Alex, send_bday_message

if __name__ == "__main__":
    
    f = open('bd/birthdays.json')
    data = json.load(f)    
    
    send_bday_message(data)


