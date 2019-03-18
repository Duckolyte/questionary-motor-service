from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def data_received(self, chunk):
        pass

    def set_default_headers(self):
        print('set headers!!')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header(
            'Access-Control-Allow-Headers',
            'Content-Type, Access-Control-Allow-Origin, '
            'Access-Control-Allow-Headers, X-Requested-By,'
            ' Access-Control-Allow-Methods'
        )

    def options(self):
        pass


