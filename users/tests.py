from django.test import TestCase
from .models import  Profile, CustomUser
from datetime import date


class TestCaseCustomProfile(TestCase):
    def setUp(self):
        self.user=CustomUser.objects.create_user(
            username='azam',
            email='test@gmail.com',
            phone_number='+998335337061',
        )

        self.profile=Profile.objects.create(
            user=self.user,
            bio='assalomu aleykum',
            avatar=None,
            birth_date=date(2000,11,12)
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username,'azam')
        self.assertEqual(self.user.email,'test@gmail.com')
        self.assertEqual(self.user.phone_number,'+998335337061')


    def test_profil(self):
        self.assertEqual(self.profile.user,self.user)
        self.assertEqual(self.profile.bio,'assalomu aleykum')
        self.assertFalse(self.profile.avatar)
        self.assertEqual(self.profile.birth_date,date(2000,11,12))

    def test_profile(self):
        self.assertEqual(str(self.profile),self.user.username)
