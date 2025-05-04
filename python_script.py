#!/usr/bin/env python3
import requests
import sys

def make_request(url):
    try:
        response = requests.get(url)
        
        if response.status_code // 100 in (1, 2, 3):
            print(f"Успешный ответ [{response.status_code}]: {response.text}")
        else:
            raise Exception(f"Ошибка [{response.status_code}]: {response.text}")
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Ошибка запроса: {str(e)}")

def main():
    endpoints = [
        'https://httpstat.us/200',
        'https://httpstat.us/201',
        'https://httpstat.us/301',
        'https://httpstat.us/404',
        'https://httpstat.us/500'
    ]
    
    for url in endpoints:
        try:
            print(f"\nЗапрос к {url}")
            make_request(url)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()