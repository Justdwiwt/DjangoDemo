# Django

## 目录构成

```
DjangoDemo/
    |_DjangoDemo/
    |_templates/
    |_venv/
    |_db.sqlite3
    |_manage.py
        |___init__.py
        |_settings.py
        |_urls.py
        |_wsgi.py
```

* manage.py：是Django用于管理本项目的命令行工具，之后进行站点运行、数据库自动生成、静态文件收集等都要通过该文件完成。
* DjangoDemo/：目录中包含了本项目的实际文件，同时因为其中包含__init__.py文件，所以该目录也是一个Python包。
* DjangoDemo/__init__.py：告诉Python该目录是一个Python包，其中暂无内容。
* DjangoDemo/settings.py：Django的项目配置文件。默认时，在其中定义了本项目引用的Django组件、Django项目名等。在之后的开发中，还需在其中配置数据库参数、导入其他Python包等信息。
* DjangoDemo/urls.py：维护项目的URL路由映射，即定义客户端访问的URL由哪一个Python模块解释并提供反馈。在默认情况下，其中只定义了“/admin”即管理员站点的解释器。
* DjangoDemo/wsgi.py：定义WSGI的接口信息，用于与其他Web服务器集成，一般本文件生成后无须改动。

```
app/
    |_migrations/
        |___init__.py
    |___init__.py
    |_admin.py
    |_apps.py
    |_models.py
    |_tests.py
    |_views.py
```

* migrations/：用于在之后定义引用迁移功能。
* __init__.py：其中暂无内容，该文件的存在使得app成为一个Python包。
* admin.py：管理站点模型的声明文件，默认为空。
* apps.py：应用信息定义文件。在其中生成了类AppConfig，该类用于定义应用名等Meta数据。
* models.py：添加模型层数据类的文件。
* tests.py：测试代码文件。
* views.py：定义URL响应函数。
