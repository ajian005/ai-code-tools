#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_numbers(a, b):
    """计算两个数的和"""
    c = a + b
    return c

def main():
    """主函数，输出hello world!和加法运算"""
    print("hello world!")
    
    # 加法功能演示
    a = 10
    b = 20
    c = add_numbers(a, b)
    print(f"{a} + {b} = {c}")
    
    # 也可以让用户输入数字
    try:
        print("\n请输入两个数字进行加法运算：")
        user_a = float(input("请输入第一个数字 a: "))
        user_b = float(input("请输入第二个数字 b: "))
        user_c = add_numbers(user_a, user_b)
        print(f"{user_a} + {user_b} = {user_c}")
    except ValueError:
        print("输入无效，请输入有效的数字！")

if __name__ == "__main__":
    main()