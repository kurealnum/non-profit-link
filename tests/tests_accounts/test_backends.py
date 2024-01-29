from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from apps.accounts.backends import OrgBackend

UserModel = get_user_model()

class OrgBackendTest(TestCase):
    def setUp(self):
        self.backend = OrgBackend()
        self.user = UserModel.objects.create_user(username='testuser', password='password123')

    def test_authenticate_valid_credentials(self):
        user = self.backend.authenticate(request=None, username='testuser', password='password123')
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_authenticate_invalid_username(self):
        with self.assertRaises(ValidationError) as cm:
            self.backend.authenticate(request=None, username='nonexistentuser', password='password123')
        self.assertEqual(str(cm.exception), "['Invalid Username']")

    def test_authenticate_invalid_password(self):
        with self.assertRaises(ValidationError) as cm:
            self.backend.authenticate(request=None, username='testuser', password='wrongpassword')
        self.assertEqual(str(cm.exception), "['Invalid Password']")

    def test_get_user_existing_user(self):
        user = self.backend.get_user(user_id=self.user.id)
        self.assertIsNotNone(user)
        self.assertEqual(user, self.user)

    def test_get_user_non_existing_user(self):
        user = self.backend.get_user(user_id=self.user.id + 1)
        self.assertIsNone(user)