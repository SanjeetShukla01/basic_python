# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     04/05/23 12:49 pm
# File:             enums_better.py
# -----------------------------------------------------------------------
from enum import Enum, auto


class OrderStatus(Enum):
    OPEN = auto()
    CLOSE = auto()


if __name__ == '__main__':
    print(OrderStatus.OPEN.value)
    print(OrderStatus.OPEN.name)
