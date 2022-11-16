# grep 

## sources
- info grep
- man grep
- [grep.pdf](http://www.gnu.org/software/grep/manual/grep.pdf)
- [A Beginner’s Guide to Grep: Basics and Regular Expressions](https://opensourceforu.com/2012/06/beginners-guide-gnu-grep-basics/)


## notes

### Grep
- 'grep'
- Grep是系统管理员瑞士军刀工具集中的一个，在一组文件，甚至子文件夹中搜索字符串或模式(一类字符串)极为有用。
- Grep是Global Regular Expression Print的缩写。
- Grep从给定的文件或输入中寻找字符串。
- 两种使用方式：
  + 从给定文件或多个文件中搜索；
  + 通过管道接收输入，在输入中搜索。

### Regular expressions

- 正则表达式，通常缩写为'regex'和'regexp'，是定义一种模式的方式。
- 正则表达式是一组字符串。
- 利用正则表达式，可以找出输入中所有匹配所定义的模式的复现样本。
- 正则表达式通常出现在grep命令中：
  + grep [options] [regexp] [filename]
- 正则表达式有很多变种，它们只是在脱离符、元字符或特殊操作符方面有差异。
- 两类表达功能集：
  + 基本:在正则基本表达式中，元字符`?`，`+`，`{`，`(`，和`)`失去特殊意义。
  + 扩展:在grep命令中加选项`-E`切换到扩展正则表达式。
- 通常把正则表达式用单引号包围起来，以防止在prep处理之前被壳语言解释或扩
  展。
  
### 基本用法
- 查找`abcd`，忽略大小写。
```
grep -i 'abcd' testfile 
```
- 查找`abcd`，且仅为一个独立的词。
```
grep -w 'abcd' testfile 
```
- 在某个路径中找查找特定模式。
```
grep -r 'abcd' /root/ 
```
- 反向输出，即不输出匹配的行。
```
grep -v 'practical' testfile 
```
- 在路径中查找所有不含`Network`的文件。`L`即`--files-without-match`，
`l`是`L`相反选项，即`--files-with-matches`
```
grep -r -L "Network" /var/log/* 
```
- 打印出匹配的行及后序的num行。`-A[num]`。打印之前的若干行，用`-B[num]`。
之前和之后若干行，用`-C[num]`。
```
grep -A1 '123'  testfile
```
- 打印出匹配的行及文件名。
```
grep -H 'a' testfile
```
- 安静选项，不输出匹配结果，只输出是否找到。
```
grep -q '456' testfile 
echo $?  #查寻结果
```



