#! /usr/bin/python3
# -*- coding: utf-8 -*-
# 来源
# https://docs.python.org/3/howto/argparse.html
# 

import argparse

if __name__ == '__main__':

    # 示例1: 基本功能
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum',
                        dest='accumulate',
                        action='store_const',
                        const=sum,
                        default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

    # # 示例2: prog
    # parser = argparse.ArgumentParser(prog='myprogram')
    # parser.print_help()

    # # %(prog) 可引用程序名
    # parser = argparse.ArgumentParser(prog='myprogram')
    # parser.add_argument('--foo', help='foo of the %(prog)s program')
    # parser.print_help()

    # # usage 定义可以覆盖默认描述
    # parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
    # parser.add_argument('--foo', nargs='?', help='foo help')
    # parser.add_argument('bar', nargs='+', help='bar help')
    # parser.print_help()

    # # description= 用来对程序功能做简单描述
    # parser = argparse.ArgumentParser(description='A foo that bars')
    # parser.print_help()

    # # 对程序描述做额外补充
    # parser = argparse.ArgumentParser(
    # description='A foo that bars',
    # epilog="And that's how you'd foo a bar")
    # parser.print_help()

    # # 公共参数的应用
    # parent_parser = argparse.ArgumentParser(add_help=False)
    # parent_parser.add_argument('--parent', type=int)

    # foo_parser = argparse.ArgumentParser(parents=[parent_parser])
    # foo_parser.add_argument('foo')
    # foo_parser.parse_args(['--parent', '2', 'XXX'])

    # bar_parser = argparse.ArgumentParser(parents=[parent_parser])
    # bar_parser.add_argument('--bar')
    # bar_parser.parse_args(['--bar', 'YYY'])

    # # name
    # # 定义了一个解析器
    # parser = argparse.ArgumentParser(prog='PROG')

    # # 定义了一个可选参数foo
    # parser.add_argument('-f', '--foo')

    # # 定义了一个bar位置参数
    # parser.add_argument('bar')

    # # 解析时，只有一个位置参数，故bar='BAR'
    # parser.parse_args(['BAR'])

    # # 解析时，一个位置参数，故bar='BAR'，另一个可选参数foo='FOO'
    # parser.parse_args(['BAR', '--foo', 'FOO'])
    # parser.parse_args(['BAR', '-f=FOO'])

    # # 运行错误，没有位置参数设置
    # parser.parse_args(['--foo', 'FOO'])

    # store动作，即默认动作
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo')
    # parser.parse_args('--foo 1'.split())

    # # store_const动作，搭配const赋值使用
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo', action='store_const', const=42)
    # parser.parse_args(['--foo'])

    # # 当store_const的值为True或False时，动作为store_false或store_true
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo', action='store_true')
    # parser.add_argument('--bar', action='store_false')
    # parser.add_argument('--baz', action='store_false')
    # parser.parse_args('--foo --bar'.split())

    # # append将参数当作一个列表，将每个参数数加在列表之中
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo', action='append')
    # parser.parse_args('--foo 1 --foo 2'.split())

    # # 将const定义的常量加到参数列表之中
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--str',
    #                     dest='types',
    #                     action='append_const',
    #                     const=str)
    # parser.add_argument('--int',
    #                     dest='types',
    #                     action='append_const',
    #                     const=int)
    # parser.parse_args('--str --int'.split())

    # # count用来统计一个关键定参数的个数
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--verbose', '-v', action='count')
    # parser.parse_args(['-vvv'])

    # # 针对version参数，返回版本信息
    # # 运行时有错误
    # parser = argparse.ArgumentParser(prog='PROG')
    # parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    # parser.parse_args(['--version'])

    # nargs选项 --------------------------------------------------------
    # 用以描述参数的数量

    # # N个参数将归于一个列表。注意，当nargs=1时，产生了一个容量为1的列表。
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo', nargs=2)
    # parser.add_argument('bar', nargs=1)
    # parser.parse_args('c --foo a b'.split())

    # # '?'参数
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo', nargs='?', const='c', default='d')
    # parser.add_argument('bar', nargs='?', default='d')
    # parser.parse_args(['XX', '--foo', 'YY'])
    # parser.parse_args(['XX', '--foo'])
    # parser.parse_args([])

    # # '*'参数，将参数赋予一个列表
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--foo', nargs='*')
    # parser.add_argument('--bar', nargs='*')
    # parser.add_argument('baz', nargs='*')
    # parser.parse_args('a b --foo x y z --bar 1 2 3 4'.split())
    
