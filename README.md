## Инструкция по развертыванию Flask-приложения с PostgreSQL в Docker

1. **Клонирование репозитория**:

   ```bash
   git clone https://github.com/artcherenkov/itmo-flask-postgres.git
   cd itmo-flask-postgres
   ```

2. **Сборка и запуск контейнеров**:

   ```bash
   docker-compose up --build
   ```

3. **Доступ к приложению**:

   Приложение доступно по адресу:

   ```
   http://localhost:5050
   ```

4. **Описание сервисов**:

   - **web**: Flask-приложение, которое подключается к PostgreSQL и ведет счетчик запросов.
   - **db**: СУБД PostgreSQL для хранения данных.

5. **Инициализация базы данных**:

   При старте контейнера `web` автоматически выполняется инициализация таблицы `table_counter`, если она не существует.

6. **Остановка контейнеров**:

   ```bash
   docker-compose down
   ```
