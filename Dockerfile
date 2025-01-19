# Используем официальный образ PostgreSQL
FROM postgres:15

# Устанавливаем переменные окружения по умолчанию
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=queue 

# (Опционально) Копируем скрипт для начальной инициализации базы данных
# ADD ./init.sql /docker-entrypoint-initdb.d/

# Открываем порт 5432
EXPOSE 5432