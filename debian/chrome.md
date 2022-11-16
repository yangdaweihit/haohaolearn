# google-chrome

- 打开浏览器时弹出对话框，要求输入`Default Keyring`
- 不输入任何内容，按`continue`后`next`
- seahorse打开密码列表时，若已有很多`Default Keyring`，就删除已有密码文件：
```
rm ~/.local/share/keyrings/*
```