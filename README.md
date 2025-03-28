---

# Задание и выполненные по ним пункты

Создать полный глоссарий употребляемых терминов и спроектировать доступ к нему в виде GRPC-севрера в докер-контейнере с использованием **gRPC**, **protobuf**
Глоссарий должен поддерживать следующие операции:
- Получение списка всех терминов.
- Получение информации о конкретном термине по ключевому слову.
- Добавление нового термина с описанием.
- Обновление существующего термина.
- Удаление термина из глоссария.

## Выполненные пункты:
✅ Реализовать решение с использованием **gRPC**, **protobuf**

✅ реализуйте  решение в виде контейнера (Dockerfile) или реализуйте решение с помощью Docker Compose; 

✅ обеспечите автоматическую миграцию структуры данных при старте приложения. 

🟩 разверните grpc-сервис на публичном сервере в вебе. 

## Описание API:

- `glossary.GlossaryService.CreateWord`  Добавить новое слово в глоссарий.
- `glossary.GlossaryService.GetWord` Получить данные о слове по параметру `name`
- `glossary.GlossaryService.DeleteWord`  Удалить слово из глоссария по идентификатору 
- `glossary.GlossaryService.UpdateWord` Изменить определение текущего слова  
- `glossary.GlossaryService.ListAllWords` Получение всех терминов в глоссарии

## Как запускать?

Склонировать проект себе на машину и перейти в директорию проекта (там где расположен Readme.md)
Далее, запустить venv (чтобы не ставить локально зависимости) и установить все зависимости
   ```bash
   virtualenv env
   source env/bin/activate
   pip install -r req.txt

   #чтобы сгенерировать python-методы из написанных proto-спецификаций, запускалась команда (можно пропустить этот пункт тк файлы уже есть в репозитории)
   python -m grpc_tools.protoc \
       --proto_path=./protobufs \
       --python_out=. \
       --grpc_python_out=. \
       protobufs/app.proto
   ```

Приложение запустится и будет доступно по локально на порту 8000
   ```bash
   python -m app.server
   ```

## Как тестировать?

1) Запустить тесты, которые проверяют все методы сервиса
   ```bash
   python -m app.test
   ```

2) Внучную черз утилиту командной строки grpcurl. Примеры запросов:
   ```bash
   grpcurl --plaintext localhost:8000 list #список сервисов
   grpcurl --plaintext localhost:8000 list glossary.GlossaryService

   #создать термин
   grpcurl --plaintext\
   -d '{"word":{"name":"python","definition":"Язык программирования"}}' \
   localhost:8000 \
   glossary.GlossaryService/CreateWord

   #обновить определение термин
   grpcurl --plaintext\
   -d '{"word":{"name":"python","definition":"Язык Программирования"}}' \
   localhost:8000 \
   glossary.GlossaryService/UpdateWord

   #показать термин по имени
   grpcurl --plaintext\
   -d '{"name":"python"}' \
   localhost:8000 \
   glossary.GlossaryService/GetWord

   #список всех терминов
   grpcurl --plaintext \ 
   localhost:8000 \
   glossary.GlossaryService/ListAllWords

   #удалить термин 
   grpcurl --plaintext\ 
   -d '{"id":1}' \
   localhost:8000 \                     
   glossary.GlossaryService/DeleteWord
   ```

Eсть возможность поднять приложение в Docker-контейнере. Для этого запустить команды из той же главное директории команду:
   ```bash
   docker build -t glossary-app . #собрать образ
   docker run -d --name glossary_container -p 8000:8000 glossary-app #поднять контейнер с приложением
   ```

