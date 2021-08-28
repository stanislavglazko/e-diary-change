# e-diary-change

Набор скриптов для изменения оценок 
и другой информации в электронном дневнике школы.

### Как установить

1) Скачать код электронного дневника. 
   Репозиторий:
   https://github.com/devmanorg/e-diary/tree/master
2) Положить файл с базой данной 
   в каталог с кодом электронного дневника 
3) Положить файл scripts.py в папку с кодом электронного дневника.
   Рядом с файлом manage.py.
4) Чтобы запустить shell, написать в терминале: 
    ```
    python3 manage.py shell
    ```
5) Импортировать скрипты:
    ```
    import scripts
    from scripts import find_schoolkid, find_lesson, fix_marks, remove_chastisements, create_commendation
    ```

### How to use
1) Исправить оценки любому ученику: 
    ```
    fix_marks(name) 
    ```
2) Удалить все замечания:
    ```
    remove_chastisements(name) 
    ```
3) Добавить похвалу:
    ```
    create_commendation(name, subject)
    ```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).