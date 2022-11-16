# argparse
- argparse是Python的一个模块，用于脚本命令行参数解析。
  - argparse提供定义命令行的友好界面。
  - 还可以生成帮助信息。
- 本文在持续更新中，最新版本见[这里](https://github.com/yangdaweihit/haohaolearn/tree/master/python/doc/argparse.md)。
- 对应的实验代码见[这里](https://github.com/yangdaweihit/haohaolearn/blob/master/python/practice/p004-argparse.py)。
- 内容来源
  - [Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)：一个简短的教程，帮助我们了解主要概念，体验其用法。
  - [Manual](https://docs.python.org/3/library/argparse.html#module-argparse)：完整的语法手册。

## 概念

当我们执行一个Python脚本时，可能需要通过参数，使得脚本行为更加丰富或实现行为的完整定义。argparse提供了一套方式，使脚本可以接受并解析参数。如：

```
ls -l  # -l 就是所谓的可选参数(optional argument)
cp src dst # src 和 dst 就是所谓的位置参数(positional argument)
```

- 可选参数：旨在丰富脚本行为；
- 位置参数：旨在实现行为的完整定义。

## 基本步骤

```
import argparse
parser = argparse.ArgumentParser() # 定义一解析器对象
parser.add_argument(..)  # 定义参数
args = parser.parse_args() # 将当前参数解析
args.xxx   # 定义参数相应的行为
```

1. ArgumentParser创建解析器
2. add_argument定义参数
3. parse_args解析参数

接上来就分别对上述3个步骤详细说明。

## [ArgumentParser对象](https://docs.python.org/3/library/argparse.html#parsing-arguments)



## [add_argument()方法](https://docs.python.org/3/library/argparse.html#the-add-argument-method)

```
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```

add_argument方法定义参数及如何被解析。每个参数的定义都有更具体的细节，在add_argument方法的参数中被定义。

- name or flags：参数名 或 可选字符串列表，如`foo`或`-f, --foo`。
- action: 基本动作类型， 即如何处理该参数。
- nargs：参数的数量。
- const：常量。需要某些`action`和`nargs`被选定后定义该参数。
- default: 若该参数在脚本执行时被忽略，则取用的值。
- type：参数被转换为的类型。
- choices：参数允许的值。
- required：是否允许被忽略。
- help：对该参数简短的说明。
- metavar：在用法消息中该参数的名称。
- dest：由parse_args()返回对象中属性的名字。

### [name of flags](https://docs.python.org/3/library/argparse.html#name-or-flags)

```
parser.add_argument('-f', '--foo')  # 定义可选参数
parser.add_argument('bar') # 定义位置参数
```

在解析时候，有`-`前缀的参数被理解为可选参数，其它的则被理解为位置参数。如：

```
parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)  # 参数bar的值为'BAR'
parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO') # 设定了可选参数的值
parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: the following arguments are required: bar  # 出现错误，因为没有设定位置参数
```

### [action](https://docs.python.org/3/library/argparse.html#action)

- `'store'`：默认动作，存储参数值。例：

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo')
  >>> parser.parse_args('--foo 1'.split())  # 将foo参数存储为1
  Namespace(foo='1')  
  ```

- `'store_const'` ： 存储常量，常量的值由`const`参数定义。在可选参数，这个动作最为常见。

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', action='store_const', const=42)
  >>> parser.parse_args(['--foo'])
  Namespace(foo=42)
  ```

- `'store_true'` 和` 'store_false'`是`store_const`的特殊情况，即存储常量`True`或`False`。

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', action='store_true')
  >>> parser.add_argument('--bar', action='store_false')
  >>> parser.add_argument('--baz', action='store_false')
  >>> parser.parse_args('--foo --bar'.split())
  Namespace(foo=True, bar=False, baz=True)
  ```

- `'append'`存储一个列表，将每个参数值附加到一个列表中。这在一个参数多次被赋值时有用处。

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', action='append')
  >>> parser.parse_args('--foo 1 --foo 2'.split())
  Namespace(foo=['1', '2'])
  ```

- `'append_const'`存储一个列表，并将`const`定义的值附加到列表中。

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--str', dest='types', action='append_const', const=str) # 注意参数dest
  >>> parser.add_argument('--int', dest='types', action='append_const', const=int)
  >>> parser.parse_args('--str --int'.split())
  Namespace(types=[<class 'str'>, <class 'int'>]) # 
  ```

- `'count`统计一个参数发生的次数，在增长参数详细程度时，这个参数有用处。

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--verbose', '-v', action='count', default=0)
  >>> parser.parse_args(['-vvv'])
  Namespace(verbose=3)  # 将概据详细程度做出相应的行为
  ```

- `'help'`打印所有参数选项并退出程序。

- `'version'`配合后面`version=`定义，显示版本信息，并退出程序。

  ```
  >>> import argparse
  >>> parser = argparse.ArgumentParser(prog='PROG')
  >>> parser.add_argument('--version', action='version', version='%(prog)s 2.0')
  >>> parser.parse_args(['--version'])
  PROG 2.0
  ```

- `'extend'`存储一个列表，将每个参数值都放在这个列表中。这是在38版本中新出现的。

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument("--foo", action="extend", nargs="+", type=str)
  >>> parser.parse_args(["--foo", "f1", "--foo", "f2", "f3", "f4"])
  Namespace(foo=['f1', 'f2', 'f3', 'f4'])
  ```

### [nargs](https://docs.python.org/3/library/argparse.html#nargs)

通常一个参数和一个动作关联。`nargs`参数将若干个参数关联到一个动作上。该参数支持的值如下：

- `N`(一个整数)：

  ```
  >>> parser = argparse.ArgumentParser()
  >>> parser.add_argument('--foo', nargs=2)  # 将 --foo 后面2个值存储到foo参数。
  >>> parser.add_argument('bar', nargs=1)
  >>> parser.parse_args('c --foo a b'.split())
  Namespace(bar=['c'], foo=['a', 'b'])
  ```

  

### const



### default



### type



### choices



### required



### help



### metavar



### dest



## [parse_args()方法](https://docs.python.org/3/library/argparse.html#the-parse-args-method)

