# API YATUBE
## Описание
Для уже ранее созданного проекта Yatube разработано API, с помощью которого пользователям
предоставляется возможность получить информацию о конкретном ресурсе сервиса.

## Как запустить проект 

Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/Maxon57/api_final_yatube.git```

```cd yatube_api```

Cоздать и активировать виртуальное окружение:

```python3 -m venv env```

```source env/bin/activate```

Установить зависимости из файла requirements.txt:

```python3 -m pip install --upgrade pip```

```pip install -r requirements.txt```

Выполнить миграции:

```python3 manage.py migrate```

Запустить проект:

```python3 manage.py runserver```

##Примеры получения API

###Неавторизованный пользователь
Неавторизироанным пользователям доступен ограниченный функционал сервиса Yatube.
Клиент может получить только разрешенные запросы, как GET, HEAD и OPTIONS.

`GET api/v1/posts/` - Получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией

```JSON
{
    "count": 123,
    "next": "link",
    "previous": "link",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
                ]
}
```
`GET api/v1/posts/{id}/` - Получение публикации по id

`GET api/v1/groups/` - Получение списка доступных сообществ
`GET api/v1/groups/{id}/` - Получение информации о сообществе по id

`GET api/v1/{post_id}/comments/` - Получение всех комментариев к публикации
`GET api/v1/{post_id}/comments/{id}/` Получение комментария к публикации по id

###Авторизированный пользователь
Для авторизированного пользователя доступен полный функционал сервиса. В данном случае
можно делать такие запросы, как POST, PATCH, PUT и DELETE. При этом необходимо при каждом
запросе проходить аутентификацию. Для этого необходимо получить личный token, 
который указывается в заголовке запроса. Но перед этим создается пользователь
(Все запросы делались в приложении [Postman](https://www.postman.com/)):

`POST /api/v1/auth/users/` - В body передаются username и password пользователя.
```JSON
{
    "username": "string",
    "password": "string"
}
```

`POST /api/v1/auth/jwt/create/` - В body передаются username и password пользователя.
Передается уникальный ключ access и refresh.

При создании поста дается возможность указать группу, к которой он принадлежит.
Для этого в `http://localhost:8000/admin/` создается группа.  

Для создания нового поста, воспользуемся POST запрсом:
```JSON
{
    "text": "string",
    "group": 0
}
```
Таким же образом создется комментарий под постом и подписка на автора - `POST /api/v1/follow/`.

Для подробной информации обращайтесь к документации API(http://localhost:8000/redoc/)

Авторы

[Maxon57](https://github.com/Maxon57)