import unittest
from faker import Faker
from  unittest.mock import MagicMock, patch
from app import create_app


fake = Faker()

class TestCustomer(unittest.TestCase):

    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()

    # def test_case_customer_full(self):
    #     name = fake.name()
    #     phone = fake.basic_phone_number()
    #     username = fake.user_name()
    #     email = fake.email()
    #     password = fake.password()
    #     role_id = 1

    #     payload = {
    #         "name": name,
    #         "phone": phone,
    #         'email': email,
    #         'username': username,
    #         'password': password,
    #         'role_id': role_id
    #     }

    #     response = self.app.post('/customers/', json=payload) #need trailing / or get 306 error
    #     print(response.json)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.json['name'], name)


    @patch('services.customerService.save') #patching save from customer service so we don't actually interact with db
    def test_case_customer(self, mock_save):
        name = fake.name()
        phone = fake.basic_phone_number()
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        role_id = 1

        mock_customer = MagicMock() #using our random data to create an instance of Customer
        mock_customer.name = name
        mock_customer.phone = phone
        mock_customer.username = username
        mock_customer.email = email
        mock_customer.password = password
        mock_customer.role_id = role_id

        mock_save.returns = mock_customer #Running fake function to return fake customer to mimic our save service

        payload = {
            "name": name,
            "phone": phone,
            'email': email,
            'username': username,
            'password': password,
            'role_id': role_id
        }

        response = self.app.post('/customers/', json=payload) #need trailing / or get 306 error
        print(response.json)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], mock_customer.name)

    @patch('services.customerService.login')
    def test_customer_login(self, mock_login):

        response_object = {
            "status": "success",
            "message": "Successfully Logged In",
            "auth_token": '12345'
        }
        
        mock_login.return_value = response_object

        payload ={
            'username': fake.user_name(),
            'password': fake.password()
        }

        response = self.app.post('/customers/login', json=payload)
        print(response.json)
        self.assertEqual(response.status_code, 200) 
       





if __name__ == '__main__':
    unittest.main()