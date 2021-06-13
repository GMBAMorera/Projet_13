from authentification.queries import create_user
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium.webdriver.firefox.webdriver import WebDriver

from authentification.models import User

class SeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_first_log(self):
        self.user = create_user({
            'username': 'admintest',
            'email': 'email',
            'password': 'password',
            'status': 'Ad',
            'job': 'job'
        })

        # Go to home page
        self.selenium.get(f'{self.live_server_url}')
        # Click on login button
        self.selenium.find_element_by_id('login').click()
        # Fill login form
        username = self.selenium.find_element_by_name('username')
        username.clear()
        username.send_keys('admintest')

        password = self.selenium.find_element_by_name('password')
        password.clear()
        password.send_keys('password')

        self.selenium.find_element_by_id('submit').click()

        # Verify that update page is loaded
        self.selenium.find_element_by_id('update-account')

        # Fill update page
        first_name = self.selenium.find_element_by_name('first_name')
        first_name.clear()
        first_name.send_keys('name')

        surname = self.selenium.find_element_by_name('surname')
        surname.clear()
        surname.send_keys('name')

        photo = self.selenium.find_element_by_name('photo')
        photo.clear()
        photo.send_keys('photo.test')

        email = self.selenium.find_element_by_name('email')
        email.clear()
        email.send_keys('email@test.test')

        street = self.selenium.find_element_by_name('street')
        street.clear()
        street.send_keys('street')

        number = self.selenium.find_element_by_name('number')
        number.clear()
        number.send_keys('number')

        city = self.selenium.find_element_by_name('city')
        city.clear()
        city.send_keys('city')

        state = self.selenium.find_element_by_name('state')
        state.clear()
        state.send_keys('state')

        country = self.selenium.find_element_by_name('country')
        country.clear()
        country.send_keys('country')

        postal_code = self.selenium.find_element_by_name('postal_code')
        postal_code.clear()
        postal_code.send_keys('postal_code')

        self.selenium.find_element_by_id('submit').click()

        assert self.selenium.find_element_by_id('job').text == 'job'

    def test_add_content(self):
        # Connect
        self.test_first_log()

        # Add Customer
        # self.selenium.find_element_by_id('add-customer').click()
        self.selenium.get(f'{self.live_server_url}/update_customers/0')

        company = self.selenium.find_element_by_name('company')
        company.clear()
        company.send_keys('company')

        street = self.selenium.find_element_by_name('street')
        street.clear()
        street.send_keys('street')

        number = self.selenium.find_element_by_name('number')
        number.clear()
        number.send_keys('number')

        city = self.selenium.find_element_by_name('city')
        city.clear()
        city.send_keys('city')

        country = self.selenium.find_element_by_name('country')
        country.clear()
        country.send_keys('country')

        postal_code = self.selenium.find_element_by_name('postal_code')
        postal_code.clear()
        postal_code.send_keys('postal_code')

        self.selenium.find_element_by_id("submit").click()
        # Look at Customer
        assert self.selenium.find_element_by_id('company').text == 'company'

        # Add Product
        self.selenium.get(f'{self.live_server_url}/update_products/0')

        name = self.selenium.find_element_by_name('name')
        name.clear()
        name.send_keys('name')

        price = self.selenium.find_element_by_name('off_the_shelf_price')
        price.clear()
        price.send_keys('10')

        cost = self.selenium.find_element_by_name('production_cost')
        cost.clear()
        cost.send_keys('5')

        desc = self.selenium.find_element_by_name('description')
        desc.clear()
        desc.send_keys('description')

        stock = self.selenium.find_element_by_name('stock')
        stock.clear()
        stock.send_keys('2')

        unit = self.selenium.find_element_by_name('stock_unit')
        unit.clear()
        unit.send_keys('unit_stock')

        photo = self.selenium.find_element_by_name('photo')
        photo.clear()
        photo.send_keys('photo.test')

        self.selenium.find_element_by_id("submit").click()
        # Look at Product
        assert self.selenium.find_element_by_id('description').text == 'description'

        # Add Employee
        self.selenium.get(f'{self.live_server_url}/register')

        username = self.selenium.find_element_by_name('username')
        username.clear()
        username.send_keys('test_employee')

        job = self.selenium.find_element_by_name('job')
        job.clear()
        job.send_keys('job')

        email = self.selenium.find_element_by_name('email')
        email.clear()
        email.send_keys('email@email.test')

        password = self.selenium.find_element_by_name('password')
        password.clear()
        password.send_keys('password')

        password2 = self.selenium.find_element_by_name('password2')
        password2.clear()
        password2.send_keys('password')

        self.selenium.find_element_by_id("submit").click()

        # Look at Employee list
        print(self.selenium.find_element_by_id('job').text)
        assert self.selenium.find_element_by_id('job').text == 'Job: job'