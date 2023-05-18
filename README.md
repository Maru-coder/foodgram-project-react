## Проект Foodgram

![workflow](https://github.com/Maru-coder/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.

Проект доступен по [адресу](http://158.160.46.231)

Данные суперюзера:

```
email: ejowa32@yandex.ru
password: 159753000aaa
```

Документация к API доступна [здесь](http://158.160.46.231/api/docs/)

В документации описаны возможные запросы к API и структура ожидаемых ответов. Для каждого запроса указаны уровни прав доступа.

### Технологии:

Python, Django, Django Rest Framework, Docker, Gunicorn, NGINX, PostgreSQL, Yandex Cloud, Continuous Integration, Continuous Deployment

### Развернуть проект на удаленном сервере:

- Клонировать репозиторий:

```
https://github.com/Maru-coder/foodgram-project-react.git
```

- Установить на сервере Docker, Docker Compose:

```
sudo apt update                                         # установка обновлений
sudo apt upgrade -y
sudo apt install docker.io                              # установка Докер
sudo mkdir -p /usr/local/lib/docker/cli-plugins         # установка Докер-компос
sudo curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
sudo chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
```

- Скопировать на сервер файлы docker-compose.yml, default.conf из папки infra (команды выполнять, находясь в папке infra):

```
scp docker-compose.yml default.conf username@IP:/home/username/   # username - имя пользователя на сервере
                                                                  # IP - публичный IP сервера
```

- Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:

```
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
PASSPHRASE              # *если ssh-ключ защищен паролем
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

- Создать и запустить контейнеры Docker, выполнить команду на сервере
*(версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):*

```
sudo docker compose up -d
```

- После успешной сборки выполнить миграции:

```
sudo docker compose exec backend python manage.py migrate
```

- Создать суперпользователя:

```
sudo docker compose exec backend python manage.py createsuperuser
```

- Собрать статику:

```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

- Для остановки контейнеров Docker:

```
sudo docker compose down -v      # с их удалением
sudo docker compose stop         # без удаления
```

### После каждого обновления репозитория (push в ветку master) будет происходить:

1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
2. Сборка и доставка докер-образов frontend и backend на Docker Hub
3. Разворачивание проекта на удаленном сервере
4. Отправка сообщения в Telegram в случае успеха


### Автор backend'а:

Марина Ежова
