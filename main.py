from flask import Flask, send_file, Response
from concurrent.futures import ThreadPoolExecutor
import threading
import time
import requests

app = Flask(__name__)

def get_proxy(web):
    response = requests.get(web)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return None
def main():
    while True:
    try:
        with open('http.txt', 'w') as file:
            file.write('http.txt')
        with open(file_path, 'r') as file:
            file_content = file.read()
        return Response(file_content, content_type='text/plain')
    except Exception as e:
        return str(e)
@app.route('/only', methods=['GET'])
def mot_proxy():
    try:
        file_path = 'proxy.txt'
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
        return Response(first_line, content_type='text/plain')
    except Exception as e:
        return str(e)
@app.route('/nocheck', methods=['GET'])
def proxy_chua_check():
    try:
        file_path = 'http.txt'
        with open(file_path, 'r') as file:
            file_content = file.read()
        return Response(file_content, content_type='text/plain')
    except Exception as e:
        return str(e)
@app.route('/', methods=['GET'])
def index():
    try:
        file_path = 'README.md'
        with open(file_path, 'r') as file:
            file_content = file.read()
        return Response(file_content, content_type='text/plain')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(app.run(host='0.0.0.0'))
        executor.submit(main)
