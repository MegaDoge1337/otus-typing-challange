# Python Type Challenges (готовые упражнения)

Домашнее задание для курса `Python Developer. Professional`. Проект содержит решенные задачи [тренажера по аннотированию](https://python-type-challenges.zeabur.app). Были решены 2 блока: `Basic` и `Intermediate`.

## Системные требования
- `Python` версии `3.11` или выше
- `Poetry` версии `1.8.3` или выше


## Статический анализатор

Проект `Python Type Challenges` использует `pyright` в качестве статического анализатора. В рамках проекта был использован `mypy`.

## Установка

1. Склонируйте репозиторий:
```
git clone https://github.com/MegaDoge1337/otus-typing-challange
```

2. Перейдите в директорию с проектом:
```
cd otus-typing-challange
```

3. Установите зависимости:
```
poery install
```

## Проверка типов

Для того, чтобы проверить правильность типизации, запустите mypy вручную, или при помощи Makefile:
```
make typing
```
