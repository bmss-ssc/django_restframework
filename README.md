# drfdemo

#### 虚拟环境

mkvirtualenv virtualenvname

workon virtualenvname

deactivate

#### 创建项目及子目录

django-admin startproject drfdemo

django-admin startapp stuapi

django-admin startapp students

django-admin startapp students

#### 环境要求

pip install django==3.2.4 -i https://pypi.douban.com/simple/

pip install pymsql https://pypi.douban.com/simple/

pip install djangorestframework

pip install  django-filter==21.1(22.1 这样设置 filterset_fields )

pip install coreapi

pip install drf-yasg

#### 数据迁移

python manage.py makemigrations 

python manage.py migrate







