# Python

## 题目

写一个函数实现如下功能：

1. 首先打开附件中的data.txt文件；

2. 然后统计文件中数字、字母、空格出现的次数

3. 关闭文件

提示：open()函数打开文件；close()函数关闭文件；判断是否为数字、字符和空格的函数分别为：isdigit(),isalpha(),isspace()

## 代码

```python
# 0. 导入路径存在性判断模块
from os.path import exists as file_exists

# 1. 申请存储空间
alpha = {chr(ord('a')+i) for i in range(26)}
alpha.update({chr(ord('A')+i) for i in range(26)})
digit = {str(i) for i in range(10)}
space = ' '
outcome = [0] * 3

# 2. 定义判断函数
def isalpha(char):
    return char in alpha
def isdigit(char):
    return char in digit
def isspace(char):
    return char == space

# 3. 文件读取操作函数
def countTimes(outcome, path = "data.txt"):
    if not file_exists("data.txt"):
        print("File Not Exists")
        return 1
    with open (path, 'r') as f:
        temp = f.read(1)
        while(temp):
            if isdigit(temp):
                outcome[0] += 1
            elif isalpha(temp):
                outcome[1] += 1
            elif isspace(temp):
                outcome[2] += 1
            temp = f.read(1)
    print("文件中各项出现的次数如下：\n数字: {0}\n字母：{1}\n空格：{2}".format(*outcome))
    
# 4. 主函数/测试函数
if __name__ == "__main__":
    countTimes(outcome)
```

