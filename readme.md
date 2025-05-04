# Ansible Playbook для автоматизации Docker и проверки скриптов

## Описание проекта

Этот проект предоставляет решение для автоматизации:
1. Установки Docker на целевой хост (локальный или удаленный)
2. Сборки Docker-образа с Python-скриптом для проверки HTTP-статусов
3. Запуска и проверки работы скрипта в контейнере

## Структура проекта

```
ansible-docker-automation/
├── inventory.ini          # Файл инвентаризации хостов
├── playbook.yml           # Основной playbook
├── roles/
│   ├── docker_install/    # Роль для установки Docker
│   └── script_check/      # Роль для проверки скрипта
├── Dockerfile             # Dockerfile для образа со скриптом
README.md              # Инструкция
```

## Требования

- Ansible 2.9+
- Python 3.6+

## Установка

Установите необходимые коллекции Ansible:
```bash
sudo apt install ansible-core
ansible-galaxy collection install community.docker
```

## Запуск

```bash
ansible-playbook -i inventory.ini playbook.yml --ask-become-pass
```

## Что делает playbook

1. **Установка Docker**:
   - Добавляет официальные репозитории Docker
   - Устанавливает необходимые пакеты
   - Настраивает права пользователя

2. **Проверка скрипта**:
   - Копирует Python-скрипт и Dockerfile на хост
   - Собирает Docker-образ
   - Запускает контейнер со скриптом
   - Проверяет результат выполнения

3. **Логирование**:
   - Выводит логи выполнения скрипта
   - Проверяет код завершения контейнера

## Python-скрипт

Скрипт `python_script.py` проверяет различные HTTP-статусы:
- Логирует успешные ответы (1xx, 2xx, 3xx)
- Генерирует исключения для ошибок (4xx, 5xx)
- Проверяет 5 различных эндпоинтов

### Отдельный запуск скрипта

```bash
pip install requests
python3 python_script.py
```

## Логирование

Результаты работы можно посмотреть:
1. В выводе Ansible (docker logs)
2. Вручную проверить контейнер:
```bash
docker logs script-checker
```
