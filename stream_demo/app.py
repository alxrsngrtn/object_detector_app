from object_detection_app import worker, detect_objects

import tornado.ioloop
import tornado.web
from stream_demo.settings import config


class MainHandler(tornado.web.RedirectHandler):
    def get(self):
        self.render('index.html')


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler)
    ], **config.SETTINGS)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()