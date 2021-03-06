## dedup-img

### 描述
 dedup-img是一个基于imagededup库做封装的图片去重库，使用本地web做UI展示，所以该库依赖于:
 1. imagededup: 图片去重
 2. flask: 生成本地web，用于展示和操作图片去重后的分类展示
 3. pillow: 生成缩略图

### 安装
> pip install dedup-img

### 使用

图片去重命令
> dedup -P -d e:/Pictures

选项解析

-P 图片去重算法

| 选项 | 使用说明 |
| --- | --- |
| -P | 感知哈希（PHash） |
| -A | 平均哈希（AHash） |
| -D | 差异哈希（DHash） |
| -W | 小波哈希（WHash） |

-d 后接需要去重的图片的所在文件夹

执行去重命令后会在图片所在文件夹里生成若干文件

浏览去重后的图片数据展示
> flask-web e:/Pictures

