FROM python:3.11-alpine

# создание пользователя для запуска не от root
RUN addgroup -g 1000 -S appgroup && \
    adduser -u 1000 -S appuser -G appgroup

WORKDIR /app
COPY app.py .

# изменение владельца
RUN chown -R appuser:appgroup /app

# переключение на user
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]