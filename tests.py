import unittest
import hello as tested_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get(self):
        r = self.app.get('/')
        self.assertEqual(r.data.decode('utf-8'), 'У меня получилось!? \
            Работает 2021 01 28 10:58')

    def test_post(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)


if __name__ == '__main__':
    unittest.main()
