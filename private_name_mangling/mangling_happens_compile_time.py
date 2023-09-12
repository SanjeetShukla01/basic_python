# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/05/23 1:25 pm
# File:             mangling_happens_compile_time.py
# -----------------------------------------------------------------------

def get_count(self):
    return self.__count


class A:
    __count = 0

    # def get_count(self):
    #     return self.__count

    get_count = get_count


def main():
    a = A()
    A.__count = 21
    print(a.get_count())


if __name__ == '__main__':
    main()