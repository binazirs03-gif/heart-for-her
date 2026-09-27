# heart-for-her ♥

Анимация «сердце из слов Love You» с музыкой.

Добавлены веб-версия (`index.html`), рендер в видео (`render_video.py`) и поиск музыки рядом со скриптом.

## Как посмотреть (для неё) — самый простой способ

**Вариант 1. Видео.** Открой файл [`heart.mp4`](heart.mp4) — скачай его и запусти. Ничего устанавливать не надо. Работает на Mac, iPad, iPhone, Windows.

**Вариант 2. Страница в браузере.** Открой ссылку:

> https://binazirs03-gif.github.io/heart-for-her/

Нажми кнопку **«Открыть ♥»** — музыка и анимация начнутся. На iPad и iPhone звук включается только после нажатия, поэтому кнопка нужна.

## Как запустить программу на Mac (необязательно)

1. Открой **Терминал** (Cmd + Пробел → «Terminal»).
2. Проверь Python: `python3 --version`. Если его нет, скачай с https://www.python.org/downloads/
3. Скачай проект: на странице репозитория нажми **Code → Download ZIP**, распакуй.
4. В Терминале перейди в папку и установи pygame:
   ```
   cd ~/Downloads/heart-for-her-main
   python3 -m pip install pygame-ce
   ```
5. Запусти:
   ```
   python3 heart.py
   ```
6. Выход — клавиша **Esc**.

Окно большое (2000×1200). Если не помещается на экран, поменяй `WIDTH, HEIGHT` и `SCALE` вверху `heart.py` (например, `1000, 600` и `10`).

На Windows то же самое, только запуск командой `py heart.py`.

## Пересобрать видео

```
python3 -m pip install pygame-ce imageio-ffmpeg
python3 render_video.py
```
