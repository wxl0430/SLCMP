# SLCMP
地铁配线图绘制器，使用python编写，基于pygame，程序高度模块化，扩展简单

## 目前拥有功能
- 绘制节点
- 绘制直线
- 移动节点
- 节点放置辅助线显示
- 调节屏幕缩放，位置
- 导入导出.slcm项目文件

## 官方交流群： QQ：124660148 加群验证：SLCMP

## 部署项目

目前已知项目能在windows环境下部署，其他环境部署请自行尝试。

1. 安装python3，并配置环境变量
2. 安装pygame库
3. `pip install pygame`
4. 克隆项目（`git clone https://github.com/wxl0430/SLCMP.git`）或手动下载项目代码，解压到任意目录
5. `cd`到项目目录
6. 使用`python SLCMP.py`运行

## 快捷键
- `↑↓←→`移动屏幕位置
- `n`新建节点
- `l`新建直线
- `Ctrl+z`撤销
- `Ctrl+y`恢复
- `Ctrl+s`保存
- `Ctrl+o`打开
- `Ctrl+n`新建

## .slcm项目文件结构
实际为一个`.zip`，内部文件结构如下
```
.slcm
├── data
│   ├── idlist.json  # ID列表
│   ├── main.json    # 屏幕位置信息等
└───┴── maindata.json    # 节点，直线主要等信息
```