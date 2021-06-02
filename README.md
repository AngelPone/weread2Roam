# 微信读书导出至Roam

借助TamperMonkey + Alfred + python实现半自动微信读书笔记**增量**导出至Roam Research.

## 安装

```
git clone https://github.com/AngelPone/weread2Roam
```

1. 在TamperMonkey中安装脚本：`weread.js`
2. 安装Alfred插件，`weread2RR.alfredworkflow`
3. 将Alfred中`bash`脚本中的路径修改成`weread2Roam`的路径

## Usage

1. 打开微信读书网页版需要导出笔记的书籍
2. 点击TamperMonkey图标，`导出笔记`
3. 在Alfred输入`weread`关键词然后回车
4. 将内容粘贴到Roam Research

## requirements

* Python3
* Alfred


## 已知问题

若微信读书的划线存在跨段落的情况，粘贴至Roam层级会错乱，难以避免。