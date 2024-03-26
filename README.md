## Развертывание

Под виртуальным окружением или в Docker установить зависимости:

$ pip install -r requirements.txt

### Авторизация (получение и сохранение JWT токена в файл (либо токен можно прописать в файле 'jwt_token.txt' вручную)):

$ python azs.py auth **LOGIN** **PASSWORD**

### Получение списка карт либо одной конкретной карты (необходимо указать ее ID):

$ python azs.py cards

$ python azs.py cards 2717 

### Получение списка событий по карте за период (даты указаны в Unix timestamp, начало и конец соответственно):

$ python azs.py events 3147 1708528733 1711488733
