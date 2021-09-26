import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            "Accept": "application/json",
            "Authorization": f"OAuth {token}"
        }

        params = {
            'path': os.path.basename(file_path)
        }

        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        link = requests.get(url=url, params=params, headers=headers).json()
        if 'href' in link:
            try:
                r = requests.put(url=link['href'], data=open(file_path, 'rb'), params=params, headers=headers)
                print(f"После отправки файла на Яндекс диск, получили от сервера код ответа:", r.status_code)
            except FileNotFoundError:
                print("Файл с указанным именем не найден!")
        else:
            print(link['message'])


if __name__ == '__main__':
    path_to_file = input("Введите имя файла или полный путь к файлу: ")
    token = # здесь OAuth-токен
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
