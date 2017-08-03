#!/usr/bin/env python
#coding=utf-8
#__author__:Administrator
#__date__:2017/7/19


#异常
while True:
    try:
        x=int(input("please enter a number:"))
        break
    except ValueError as e:
        print("Oops! That was no vaild number.Try again")
    except IndexError as  e:
        print("Oops! IndexError")
    except Exception as e:
        print("Oops!ERROR")
    else:
        print()
    finally:
        print()


