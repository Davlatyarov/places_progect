from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user

class ProfileViewTestCase(TestCase):
    def test_profile(self):
        user = User.objects.create(username='javohir', first_name='Javohir', last_name='Hoshimov', email='javohir@mail.ru')
        user.save()
        self.client.post(
            reverse("users:profile"), 
            data = {
                'username':'javohir',
                'email': 'javohir@mail.ru',
            }
        )
        user = get_user(self.client)
        self.assertEqual(user.status_code, 200)
        self.assertContains(user, self.user.username)
        self.assertContains(user, self.user.first_name)
        self.assertContains(user, self.user.last_name)
        self.assertContains(user, self.user.email)

    def test_update_profile(self):
        db_user = User.objects.create(username="murodjon", first_name="Murodjon", last_name="Tokhirov", email="m@gmail.com")
        db_user.set_password("1234")
        db_user.save()
        self.client.login(username='murodjon', password='1234')
        response = self.client.post(
            reverse("users: profile"),
            data={
                "username": "murodjon",
                "first_name": "Murodjon",
                "last_name": "Zokirov",
                'email': 'm@gmail.com'
            }
        )
        user = User.objects.get(pk=db_user.pk)
        self.assertEqual(user.last_name, 'Zokirov')
