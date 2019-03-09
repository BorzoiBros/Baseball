# ~/Project/Baseball/test.py;

import os
import unittest 

from views import app, db
from config import basedir
from models import User

TEST_DB = 'test.db'

class AllTests(unittest.TestCase):

	# executed prior to each test
	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
		os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()

	# executed after each test
	def tearDown(self):
		db.session.remove()
		db.drop_all()

	# each test should start with 'test'
	def test_user_setup(self):
		new_user = User('Borzoi Bros', "borzoibros3@gmail.com", "borzoibros")
		db.session.add(new_user)
		db.session.commit()
		test = db.session.query(User).all()
		for t in test:
			t.name
		assert t.name == "Borzoi Bros"

	# check if the landing page returns expected contents
	def test_home_page_contents(self):
		response = self.app.get('/')
		print(response.data)
		expected_string = '野球'.encode('utf-8')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Borzoi Bros', response.data)

	# helper method to register a user
	def register(self, name, email, password, confirm):
		return self.app.post(
			'/register',
			data=dict(name=name, email=email,password=password,confirm=confirm),
			follow_redirects=True)

	# helper method to see if a user can login
	def login(self, name, password):
		return self.app.post('/login', data=dict(
			name=name, password=password, follow_redirects=True))

	# Check if user cannot login unless registered
	def test_users_cannot_login_unless_registered(self):
		response = self.login('foo', 'bar')
		self.assertIn(b'Login', response.data)

	# Test that user can log in:
	def test_users_can_login(self):
		self.register('Borzoi Bros', 'borzoibros3@gmail.com', 'borzoibros', 'borzoibros')
		response = self.login('Borzoi Bros', 'borzoibros')
		self.assertIn(b'demo', response.data)

if __name__ == '__main__':
	unittest.main()
