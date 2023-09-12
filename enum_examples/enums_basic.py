# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     04/05/23 12:48 pm
# File:             enums_basic.py
# -----------------------------------------------------------------------
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


if __name__ == '__main__':
    print(Color.RED.value)
    print(Color.RED.name)
    print(Color.GREEN.value)
    print(Color.GREEN.name)
    print(Color.BLUE.value)
    print(Color.BLUE.name)