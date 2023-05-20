# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/05/23 1:50 pm
# File:             alternative.py.py
# -----------------------------------------------------------------------
class A:
    __public_magic__ = "something"

    def __init__(self):
        self._dont_touch_me = "subscribe"
        self.__attr__ = "something"
        self._A__var = "manually mangled"
