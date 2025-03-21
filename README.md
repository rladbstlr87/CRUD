# CRUD logic
- 정말정말정말정말 중요함

## 0. settings
- 가상환경 설정/활성화
- `.gitignore` (python, windows, macOS, Django)

## 1. Django

- `pip install django`

- 프로젝트 생성
```shell
django-admin startproject crud .
```
---
- app 생성 / 등록
```shell
django-admin startapp posts
```
settings.py 에 `posts` 등록

## 2. CRUD
- modeling(skiima를 정의한다)
    `models.py`
```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

- migration
    1. **번역본 만들기**
        ```shell
        python manage.py makemigrations
        ```
    2. **DB에 반영**
        ```shell
        python manage.py migrate
        ```
    3. Super user 생성
        ```shell
        python manage.py createsuperuser
        ```
    4. admin 페이지에 models 등록
        `admin.py`
        ```python
        from django.contrib import admin
        from .models import Post

        admin.site.register(Post)
        ```