#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        """Обработка GET запроса"""
        if self.path == '/':
            # отправка успешного статуса
            self.send_response(200)
            # тип контента
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            # тело ответа
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            # если запрошен не корневой путь
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        """переопределние логирования"""
        pass

def main():
    """главная функция запуска сервера"""
    PORT = 8080
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, HelloHandler)
    print(f"Сервер запущен на порту {PORT}")
    print(f"Проверка: curl http://localhost:{PORT}")
    print("Остановка: Ctrl+C")
    httpd.serve_forever()

if __name__ == '__main__':
    main()