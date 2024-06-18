
import tornado.web
import tornado.websocket
import tornado.ioloop


active_clients = set()


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        active_clients.add(self)
        print("WebSocket opened")

    def on_message(self, message):
        for client in active_clients:
            print(message)
            client.write_message(message)  # will be written to every client

    def on_close(self):
        active_clients.discard(self)
        print("WebSocket closed")


app = tornado.web.Application([(r'/ws', WebSocketHandler)])

if __name__ == "__main__":
    app.listen(8765)
    tornado.ioloop.IOLoop.current().start()
