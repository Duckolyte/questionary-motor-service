import tornado.ioloop
import tornado.web

import motor

# import ui templates
# from view import partials

# import controllers
from questionary_service.controller.questionary import QuestionaryHandler


class ApplicationContext(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/questionary/([^/]+)?", QuestionaryHandler)
        ]

        settings = dict(
            db=motor.motor_tornado.MotorClient(
                'mongodb://localhost:27017'
            ).questionary
            # xsrf_cookies=True,
            # cookie_secret='123456789',
            # login_url='/login'
        )

        tornado.web.Application.__init__(self, handlers, **settings)
