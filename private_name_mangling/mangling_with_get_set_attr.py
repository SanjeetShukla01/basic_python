# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/05/23 1:48 pm
# File:             mangling_with_get_set_attr.py
# -----------------------------------------------------------------------
class A:
    def __init__(self):
        self.__x = 0
        print(getattr(self, "__x"))
        setattr(self, "__x", 42)
        print(self.__x)


def main():
    a = A()


if __name__ == '__main__':
    main()