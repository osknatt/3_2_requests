import requests
import json

def traslate(input_path, output_path, input_lang, output_lang='ru'):
        with open (input_path, encoding= 'utf-8') as f:
            text = f.read()
        URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
        params = {'lang': f'{input_lang.lower()}-{output_lang.lower()}',
                  'format': 'text',
                  'srv': 'tr-text',
                  'id': 'a5d9004b.5e5b7a74.858c5939-8-0    '
                  }
        data = {
            'text': text
        }

        res = requests.post(URL, params=params, data=data)

        with open(output_path, 'w') as f:
            for s in text.split('.'):
                URL = 'https://translate.yandex.net/api/v1/tr.json/translate'
                params = {'lang': f'{input_lang.lower()}-{output_lang.lower()}',
                          'format': 'text',
                          'srv': 'tr-text',
                          'id': 'a5d9004b.5e5b7a74.858c5939-8-0    '
                          }
                data = {
                    'text': s
                }

                res = requests.post(URL, params=params, data=data)
                # print(res)
                res.encoding = 'utf-8'
                res = res.json()
                f.write(res['text'][0] if 'text' in res else s)
                f.write('\n')


input_path = input('Введите путь к файлу: ')
output_path = input('Введите путь для сохранения перевода: ')
input_lang = input("Введите язык оригинала в формате 'xx': ")
output_lang = input("Введите язык для перевода в формате 'yy': ")
traslate(input_path, output_path, input_lang, output_lang)
