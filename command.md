## python命令集

### 字符串

- Str.title() 以 首 字 母 大 写 的 方 式 显 示 每 个 单 词；
- str.upper() 全部大写；
- str.lower() 全部小写；
- str.rstrip() 去掉字符串末尾(右边)的空白；
- str.lstrip() 去掉字符串开头(左边)的空白；
- str.strip() 去掉字符串开头和末尾多余的空白；
- Str() 将非字符串转换为字符串；

### 模块

- csv
- datetime
- json
- os
- pygal
- pygame
- sys
- time



------

### 列表

- Array.append( ) 列表末尾添加元素 ；
- Array.insert(index,  ) 在指定索引位置添加元素；
- del array[index] 删除指定位置的元素；
- Array.pop( ) 删除末尾的元素；
- Array.pop(index,  ) 删除指定位置的元素；
- Array.remove( ) 删除指定值的元素；
- Array.sort(reverse=False/True)  按字母顺序排序，改变原顺序
- sorted(array) 临时按字母顺序排序，不改变原顺序
- Array.reverse() 反转列表元素的排列顺序（不是字母顺序相反，是倒着排）
- len(array) 列表的长度
- range() 生成一系列的数字
- min() 找出最小值
- max() 找出最大值
- sum() 找出总和

### 字典

- del hash[key] 删除键值队
- 切 片 表 示 法[:] 创 建 列 表 的 副 本


### 导入函数

- import module_name导入模块
- module_name.function_name()来使用模块中任何一个函数
- from module_name import function_name  导入特定的函数
- from module_name import  \*  导入模块中的所有函数  
- import module_name as p 指定模块的别名
- from module_name import function_name as fn 指定函数的别名

### 文件

- windows系统的文件路径用\，Linux和OS X系统等文件路径用/

### 测试unittest

| 方法                    |        用途        |
| :---------------------- | :----------------: |
| assertEqual(a, b)       |     核实a == b     |
| assertNotEqual(a, b)    |     核实a != b     |
| assertTrue(x)           |    核实x为True     |
| assertFalse(x)          |    核实x为False    |
| assertIn(item, list)    |  核实item在list中  |
| assertNotIn(item, list) | 核实item不在list中 |

- 测试通过时打印一个句点；
- 测试引发错误时打印一个E；
- 测试导致断言失败时打印一个F。



------

## django project

```python
django-admin startproject mysite
```

这行代码将会在当前目录下创建一个 `mysite` 目录。

```python
python manage.py runserver
```

[`runserver`](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/#django-admin-runserver) 命令会将服务器设置为监听本机内部 IP 的 8000 端口。

```python
python manage.py startapp polls
```

创建一个 `polls` 目录，包括了投票应用的全部内容。

```python
python manage.py migrate
```

这个 [`migrate`](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/#django-admin-migrate) 命令检查 [`INSTALLED_APPS`](https://docs.djangoproject.com/zh-hans/2.0/ref/settings/#std:setting-INSTALLED_APPS) 设置，为其中的每个应用创建需要的数据表，至于具体会创建什么，这取决于你的 `mysite/settings.py` 设置文件和每个应用的数据库迁移文件。

```python
python manage.py makemigrations polls
```

通过运行 `makemigrations` 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 *迁移*。

```python
python manage.py sqlmigrate polls 0001
```

[`sqlmigrate`](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/#django-admin-sqlmigrate) 命令接收一个迁移的名称，然后返回对应的 SQL。

[`python manage.py check`](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/#django-admin-check)

这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作。



改变模型需要这三步：

- 编辑 `models.py` 文件，改变模型。
- 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/#django-admin-makemigrations) 为模型的改变生成迁移文件。
- 运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/2.0/ref/django-admin/#django-admin-migrate) 来应用数据库迁移。



```python
python manage.py shell
```

尝试一下 Django 为你创建的各种 API

```python
python manage.py createsuperuser
```

创建一个能登录管理页面的用户