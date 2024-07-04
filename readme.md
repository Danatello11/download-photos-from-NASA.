# Telegram Photo Publisher Bot

Этот проект предоставляет скрипт для автоматической публикации фотографий из заданной директории в Telegram-канал с заданной частотой.

## Установка

1. **Клонирование репозитория или загрузка файлов проекта:**

    ```sh
    git clone https://github.com/your-repo/telegram-photo-publisher-bot.git
    cd telegram-photo-publisher-bot
    ```

2. **Установка необходимых зависимостей:**

    ```sh
    pip install python-telegram-bot python-dotenv schedule
    ```

3. **Создание файла `.env` в корневой директории проекта:**

    ```sh
    touch .env
    ```

    Добавьте в файл `.env` следующие переменные окружения:

    ```env
    BOT_TOKEN=Ваш_Telegram_Bot_Token
    GROUP_CHAT_ID=Ваш_ID_группы_или_канала
    PUBLICATION_INTERVAL=4  # Интервал публикации в часах (по умолчанию 4 часа)
    ```

## Настройка

1. **Получение токена бота:**
    - Создайте Telegram-бота с помощью [BotFather](https://core.telegram.org/bots#botfather) и получите токен для вашего бота.

2. **Получение ID группы или канала:**
    - Добавьте вашего бота в группу или канал.
    - Получите ID группы или канала. Для этого можно использовать [этот бот](https://t.me/get_id_bot).

3. **Создание директории для изображений:**

    ```sh
    mkdir downloaded_images
    ```

    Поместите в эту директорию папки с изображениями от разных источников (например, `nasa`, `spacex`, `earth`).

## Использование

1. **Проверка переменных окружения:**
    Убедитесь, что файл `.env` содержит правильные значения для `BOT_TOKEN`, `GROUP_CHAT_ID` и `PUBLICATION_INTERVAL`.

2. **Запуск скрипта для публикации фотографий:**

    ```sh
    python publish_photos.py
    ```

### Примеры запуска скриптов для скачивания фотографий

1. **Скачивание фотографий Земли (EPIC):**

    ```sh
    python fetch_epic_earth_photos.py --num_photos 5 --output_folder downloaded_images/earth
    ```

    **Пример вывода:**

    ```plaintext
    Загрузка переменных окружения из файла .env
    Фотография Земли 1 сохранена: downloaded_images/earth/earth_photo_1.png
    Фотография Земли 2 сохранена: downloaded_images/earth/earth_photo_2.png
    Фотография Земли 3 сохранена: downloaded_images/earth/earth_photo_3.png
    Фотография Земли 4 сохранена: downloaded_images/earth/earth_photo_4.png
    Фотография Земли 5 сохранена: downloaded_images/earth/earth_photo_5.png
    ```

2. **Скачивание фотографий SpaceX:**

    ```sh
    python fetch_spacex_images.py --launch_id latest
    ```

    **Пример вывода:**

    ```plaintext
    Загрузка переменных окружения из файла .env
    Найдено 10 изображений
    SpaceX image saved: downloaded_images/spacex/spacex_0.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_1.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_2.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_3.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_4.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_5.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_6.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_7.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_8.jpg
    SpaceX image saved: downloaded_images/spacex/spacex_9.jpg
    ```

3. **Скачивание фотографий APOD (Astronomy Picture of the Day):**

    ```sh
    python fetch_nasa_apod.py --count 5 --output_folder downloaded_images/nasa
    ```

    **Пример вывода:**

    ```plaintext
    Загрузка переменных окружения из файла .env
    Фотография NASA 1 сохранена: downloaded_images/nasa/nasa_apod_1.jpg
    Фотография NASA 2 сохранена: downloaded_images/nasa/nasa_apod_2.jpg
    Фотография NASA 3 сохранена: downloaded_images/nasa/nasa_apod_3.jpg
    Фотография NASA 4 сохранена: downloaded_images/nasa/nasa_apod_4.jpg
    Фотография NASA 5 сохранена: downloaded_images/nasa/nasa_apod_5.jpg
    ```

### Пример запуска и вывода в консоль

```sh
$ python publish_photos.py
Загрузка переменных окружения из файла .env
Найдено 10 изображений в директории downloaded_images
Запуск публикации фотографий с интервалом 4 часа
Фотография nasa1.jpg успешно опубликована в канал
Следующая публикация через 4 часа


### Как это работает

```
Скрипт загружает переменные окружения из файла .env.
Скрипт получает все изображения из директории downloaded_images и перемешивает их.
Скрипт использует библиотеку schedule для публикации фотографий с заданной частотой.
Скрипт публикует фотографии в указанном Telegram-канале или группе. Когда все фотографии будут опубликованы, скрипт снова перемешивает изображения и начинает публикацию заново.
```
### Зависимости
```
python-telegram-bot: Для взаимодействия с Telegram API.
python-dotenv: Для загрузки переменных окружения из файла .env.
schedule: Для управления расписанием публикаций.
```