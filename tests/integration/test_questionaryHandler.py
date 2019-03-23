from tornado.testing import AsyncHTTPTestCase, gen_test

from questionary_service.tornado_questionary import setup_server


class TestQuestionaryHandler(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_get(self):
        response = self.fetch('/questionary/test_000321')
        self.assertEquals(response.code, 200)

    def test_get_invalid_url(self):
        response = self.fetch('/questionary/more/more')
        self.assertEquals(response.code, 404)

    def test_get_item_not_found(self):
        response = self.fetch('/questionary/-1')
        self.assertEquals(response.code, 404)


    def test_post(self):
        response = self.fetch(
            path='/questionary/create',
            method='POST',
            body='{"key": "value"}'
        )
        self.assertEquals(response.code, 200)

    def test_post_bad_payload_format(self):
        response = self.fetch(
            path='/questionary/create',
            method='POST',
            body='{key: "value"}'
        )
        self.assertEquals(response.code, 500)

    def test_post_empty_body(self):
        response = self.fetch(
            path='/questionary/1',
            method='POST',
            body=''
        )
        self.assertEquals(response.code, 500)
