import unittest
from unittest.mock import patch
from employee import Employee


class MockTestTrue:
    text = 'response.ok = True'
    ok = True
    status_code = 200


class MockTestFalse:
    text = 'response.ok = False'
    ok = False
    status_code = 200


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.test_employee = Employee('Jan', 'Kolos', 143)

    def test_email(self):
        self.assertEqual(self.test_employee.email, 'Jan.Kolos@email.com')

    def test_fullname(self):
        self.assertEqual(self.test_employee.fullname, 'Jan Kolos')

    def test_apply_raise(self):
        self.test_employee.apply_raise()
        self.assertEqual(self.test_employee.pay, 150)

    @patch("employee.requests.get")
    def test_monthly_schedule(self, mocker):
        mocker.monthly_schedule = MockTestTrue
        print(self.test_employee.monthly_schedule('may'), 'response.ok = True')
        mocker.monthly_schedule = MockTestFalse
        print(self.test_employee.monthly_schedule('may'))
        self.assertEqual(self.test_employee.monthly_schedule('may'), 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
