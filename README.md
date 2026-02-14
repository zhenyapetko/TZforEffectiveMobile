## Описание:
### 1. Как запустить проект?
    
    - Клонируем репозиторий 
    git clone git@github.com:zhenyapetko/TZforEffectiveMobile.git
    
    - Переходим в директорию
    cd TZforEffectiveMobile

    - Поднимаем контейнеры
    docker-compose up -d

    -Проверям, что оба зпустились
    docker-compose ps

### 2. Как проверить результат?

    - Проверка результата
    curl http://localhost

    - Результат должен быть таким
    Hello from Effective Mobile!

### 3. Схема (_nginx_ → _backend_)
```mermaid
    flowchart LR
    subgraph Host
        Client["curl http://localhost"] --> Port["Порт 80"]
    end
    
    subgraph Docker["Docker контейнеры"]
        subgraph Network["em-network"]
            Nginx["Nginx\n:80"] --> Backend["Backend\n:8080"]
        end
    end
    
    Port -.-> Nginx
    Backend -->|"Hello from Effective Mobile!"| Client

    