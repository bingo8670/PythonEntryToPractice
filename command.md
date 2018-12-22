# python命令集

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