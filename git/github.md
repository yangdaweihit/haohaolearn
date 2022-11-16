# GitHub

- [GitHub Docs](https://docs.github.com/cn/github)

- github提交方式改变

```
remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
```

## PAT
- [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- Copy PAT
- use PAT insead of password
- copy PAT and paste it into .git/config as:

  ```
  url = https://[PAT]@[github_project_address]
  ```

 ## 参考

 - [How to Setup Passwordless Authentication to GitHub Private Repository?](https://geekflare.com/github-setup-passwordless-auth/)
