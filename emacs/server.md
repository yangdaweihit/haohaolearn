# Using Emacs as a Server

## 启动服务器

有若干种启动服务器的方式：

- 在当前Emacs进程中运行`server-start`命令，有2种方式：
  + `M-x server-start`
  + 将`(server-start)`表达式写入初始化文件
  则当前进程就成为了服务器。当退出当前Emacs时，服务器随进程而退出工作。
- 以守护进程方式运行Emacs，用`--daemon`选项之一。此时，初始化后调用
  `server-start`且不打开窗口，等待客户端的编辑请求。
- 若系统用`systemd`管理启动时，可通过守护模式启动Emacs：
```
systemctl --user enable emacs
```

原理上，这样启动是可以的，但这样操作会带一个问题，即在系统退出时无法正常
退出该进程。接下来给出真正应用时的方案。

## 服务配置

将如下内容拷贝到`~/.config/systemd/user/emacs.service`中：
```
[Unit]
Description=Emacs text editor
Documentation=info:emacs man:emacs(1) https://gnu.org/software/emacs/

[Service]
Type=forking
ExecStart=/usr/bin/emacs --daemon
ExecStop=/usr/bin/emacsclient --eval "(kill-emacs)"
Environment=SSH_AUTH_SOCK=%t/keyring/ssh
Restart=on-failure

[Install]
WantedBy=default.target
```
注意，在脚本中，退出服务时，通过emacsclient以外部方式运行了
`(kill-emacs)`函数，即退出emacs守护进程。

然后启动该项服务：
```
systemctl enable --user emacs
systemctl start --user emacs
```


## emacsclient

在我的系统中，采用了`systemd`启动Emacs服务器的方式。每次开机后，Emacs服
务器便运行在后台。当需要打开Emacs窗口时，便可运行`emacsclient`。为了方便
调用这条命令，设置了`Ctrl-Alt-e`快捷键，对应的命令为：

```
emacsclient -create-frame --alternate-editor=""
```


## 参考

- [Emacs Server](https://www.gnu.org/software/emacs/manual/html_node/emacs/Emacs-Server.html)
- [emacsclient Options](https://www.gnu.org/software/emacs/manual/html_node/emacs/emacsclient-Options.html#emacsclient-Options)
- [Emacs As Dameon](https://www.emacswiki.org/emacs/EmacsAsDaemon)
- [Emacs Client](https://www.emacswiki.org/emacs/EmacsClient)