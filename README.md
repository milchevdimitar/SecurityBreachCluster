# HTTPS Security Breach Detection using AI

## Описание

Този проект представлява система за детектиране на потенциални нарушения в сигурността чрез анализ на HTTPS заявки към устройства. Използва TensorFlow базирани модели, които разглеждат както четими (readable), така и нечетими (unreadable) HTTPS заявки и предсказват дали една заявка е опасна или не.

## Структура на проекта

* `readable_https_model.py` – Дефиниция на модел за readable HTTPS заявки
* `unreadable_https_model.py` – Дефиниция на модел за unreadable HTTPS заявки
* `normalization.py` – Функции за нормализация и превръщане на сурови заявки в числови вектори
* `interface.py` – Унифициран интерфейс за работа с двата модела (предсказване и дообучение)
* `main.py` – Основен скрипт за демонстрация на нормализация, предсказание и обучение на моделите

## Технологии (до момента)

* Python 3.8+
* TensorFlow 2.x
* NumPy

## Архитектура на клъстъра

* Входните заявки преминават през функции за нормализация, които трансформират raw данните в числови вектори с фиксиран размер.
* Векторите се подават към съответния модел (readable/unreadable).
* Моделът връща вероятност за опасност (`score` между 0 и 1).
* Моделите се съхраняват като `.h5` файлове и се презареждат при стартиране.

## Варианти за архитектура на цялата система
<img width="281" height="541" alt="VAR1" src="https://github.com/user-attachments/assets/e2b7d3e9-af25-4cd5-8a67-1b70fce3b64f" />
<img width="541" height="312" alt="VAR2" src="https://github.com/user-attachments/assets/be5face4-4f05-49b7-a048-f0ee4ea81cb5" />
