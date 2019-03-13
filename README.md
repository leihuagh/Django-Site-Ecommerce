# Django Site Ecommerce

## Resources

- [Video Playlist](https://www.youtube.com/watch?v=LzI3B-8ps2c&list=PLV2_Iivd4jxYVDWCcxmccusNaUx2kWCg1&index=2)
- [GitHub](https://github.com/codingforentrepreneurs/eCommerce)

## Packages in Global Environment

- python 3.7.2
- virtualenv 6.4.3
- pylint
- autopep8
- flake8

## Packages in Virtual Environment

- Django 2.1.7
- mysqlclient 1.4.2
- pillow

## File Structure

### Project

- config

### Apps

- core
- authentication
- accounts

## Commands Used in Project

- Start Project

```shell
django-admin startproject config .
```

- Start App

```shell
python manage.py startapp <app name>
```

- Migrations

```shell
python manage.py makemigrations
python manage.py migrate
```

- Create Super User

```shell
python manage.py createsuperuser
```

- Dump Data Example

```shell
python manage.py dumpdata auth.User --format json --indent 4 > texture/users.json
```

- Seed Data Example

```shell
python manage.py loaddata texture/users.json
```

- Collect Static Files

```shell
python manage.py collectstatic
```

## Pagination Variables

```python
<ul>
    <li>{{ <app>.has_previous}}</li>
    <li>{{ <app>.number }}</li>
    <li>{{ <app>.paginator.count }}</li>
    <li>{{ <app>.paginator.page_range }}</li>
    <li>{{ <app>.has_next }}</li>
</ul>
```
