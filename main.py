import winreg

def get_license_server_info():
    # Путь к реестру для x86 и x64 систем
    reg_paths = [
        r"SOFTWARE\FLEXlm License Manager",
        r"SOFTWARE\Wow6432Node\FLEXlm License Manager"
    ]

    license_file_found = False

    for reg_path in reg_paths:
        try:
            # Открываем соответствующий путь реестра
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as key:
                # Получаем значение @CSOFT_LICENSE_FILE
                try:
                    license_file = winreg.QueryValueEx(key, "@CSOFT_LICENSE_FILE")[0]
                    print("Путь к файлу лицензии:", license_file)
                    license_file_found = True
                except FileNotFoundError:
                    pass
        except FileNotFoundError:
            pass

    if not license_file_found:
        print("Путь к серверу лицензий не найден.")

    input("Нажмите любую клавишу для выхода...")

if __name__ == "__main__":
    get_license_server_info()
