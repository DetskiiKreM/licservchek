import os
import winreg

def get_license_server_info():
    # Путь к реестру для x86 и x64 систем
    reg_paths = [
        r"SOFTWARE\FLEXlm License Manager",
        r"SOFTWARE\Wow6432Node\FLEXlm License Manager"
    ]

    for reg_path in reg_paths:
        try:
            # Открываем соответствующий путь реестра
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                print("Информация из", reg_path)
                print("=" * 40)
                for i in range(winreg.QueryInfoKey(key)[1]):
                    name, value, _ = winreg.EnumValue(key, i)
                    print(f"{name}: {value}")
                print("=" * 40)
        except Exception as e:
            print("Ошибка при доступе к реестру:", e)

    input("Нажмите любую клавишу для выхода...")

if __name__ == "__main__":
    get_license_server_info()
