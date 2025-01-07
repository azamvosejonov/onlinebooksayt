from django.test import TestCase

from users.models import CustomUser
from .models import Author,Book,Publisher,Review,Category
from datetime import date

class ModelTestCase(TestCase):
    def setUp(self):
        self.author=Author.objects.create(
            first_name='azam',
            last_name='vosejonov',
            bio='Men dunyo durdonasi haqida kitob yozdin',
            birth_day=date(1982,10,4),
            death_date=date(2010,12,2),
            web_site='www.test.com',
            author_avatar=None,
        )



        self.publisher=Publisher.objects.create(
            name='azam',
            address='Samarqand',
            web_site='www.test.com',
        )



        self.category=Category.objects.create(
            name='tarixiy',
            description='tarixiy asarlar haqida'
        )


        self.book=Book.objects.create(
            title='yoshlik',
            slug='yoshlik',
            category=self.category,
            author=self.author,
            publisher=self.publisher,
            price=10.0,
            last_price=90.0,
            cover_pic=None,
            ebook=None,
            audio_book=None,
            description='malumotlar',
            stock=1
        )


        self.review=Review.objects.create(
            user=CustomUser.objects.create_user('azam','test@gmail.com'),
            book=self.book,
            comment='salom',
            rate='malumot'
        )



    def test_author(self):
        self.assertEqual(self.author.first_name,'azam')
        self.assertEqual(self.author.last_name,'vosejonov')
        self.assertEqual(self.author.bio,'Men dunyo durdonasi haqida kitob yozdin')
        self.assertEqual(self.author.birth_day,date(1982,10,4))
        self.assertEqual(self.author.death_date,date(2010,12,2))
        self.assertEqual(self.author.web_site,'www.test.com')
        self.assertFalse(self.author.author_avatar)


    def test_publisher(self):
        self.assertEqual(self.publisher.name,'azam')
        self.assertEqual(self.publisher.address,'Samarqand')
        self.assertEqual(self.publisher.web_site,'www.test.com')


    def test_category(self):
        self.assertEqual(self.category.name,'tarixiy')
        self.assertEqual(self.category.description,'tarixiy asarlar haqida')

    def test_book(self):
        self.assertEqual(self.book.title,'yoshlik')
        self.assertEqual(self.book.slug,'yoshlik')
        self.assertEqual(self.book.category,self.category)
        self.assertEqual(self.book.author,self.author)
        self.assertEqual(self.book.publisher,self.publisher)
        self.assertEqual(self.book.price,10.0)
        self.assertEqual(self.book.last_price,90.0)
        self.assertFalse(self.book.cover_pic)
        self.assertFalse(self.book.ebook)
        self.assertFalse(self.book.audio_book)
        self.assertEqual(self.book.description,'malumotlar')
        self.assertEqual(self.book.stock,1)

    def test_review(self):
        self.assertEqual(self.review.book,self.book)
        self.assertEqual(self.review.comment,'salom')
        self.assertEqual(self.review.rate,'malumot')



