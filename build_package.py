import shutil
import os
import datetime


def create_archive():
    """
    Скрипт для сборки артефакта (ZIP-архива) с кодом сервиса. fgd
    """

    # 1. Генерируем имя файла с текущей датой
    # ПРИМЕЧАНИЕ: В конфигурации GitHub Actions мы используем шаблон "microshop_release_*.zip",
    # чтобы робот мог найти этот файл, какая бы дата ни стояла в названии.
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    base_name = f"microshop_release_{today}"

    # Папка, которую хотим упаковать
    source_dir = "orders_service"

    # 2. Проверка безопасности: существует ли папка?
    if not os.path.exists(source_dir):
        print(f"ОШИБКА: Папка '{source_dir}' не найдена!")
        print("Убедитесь, что вы запускаете этот скрипт из корня проекта (microshop-monorepo).")
        return

    print(f"--- Начинаю упаковку сервиса: {source_dir} ---")

    try:
        # 3. Создаем архив
        # make_archive сама добавит расширение .zip к base_name
        output_path = shutil.make_archive(base_name, 'zip', source_dir)

        # Получаем чистое имя файла (например, microshop_release_2023-10-05.zip)
        filename = os.path.basename(output_path)

        print(f"УСПЕХ: Архив создан -> {filename}")
        print("Этот файл готов к отправке в GitHub Releases.")

    except Exception as e:
        print(f"ОШИБКА при создании архива: {e}")


if __name__ == "__main__":
    create_archive()