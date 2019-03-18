
from django.test import TestCase
from .models import Comments, Image, Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class ProjectTestClass(TestCase):

    def setUp(self):

        self.loise = .objects.create(username="loise")
        self.picture = Image.objects.create(image='image1', user=self.loise)
        self.comment = Review.objects.create(comment = 'so ugly')
        self.test_review = Review.objects.create(user=self.loise, image=self.image1, comment='so ugly')
        self.test_review.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_reviews, Review))

    #Testing Save method

    def test_save_method(self):
        reviews = Review.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_save_review(self):
        self.assertEqual(len(Review.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Review.objects.all().delete()

        # Testing delete method

    def test_delete_review(self):
        self.test_review.delete()
        self.assertEqual(len(Review.objects.all()), 0)


class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.nairobi = Location.objects.create(name="nairobi")
        self.funny= tags.objects.create(name='funny')


        self.test_image = Image.objects.create(image='imagesef', name='cat', description='This is a description', location=self.nairobi, )

        self.test_image.save()

    def test_save_method(self):
        self.test_image.save()
        test_images = Image.objects.all()
        self.assertTrue(len(test_images) > 0)

    # Testing save method
    def test_save_image(self):
        self.assertEqual(len(Image.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        Image.objects.all().delete()

    def test_delete_image(self):
        Image.delete_image_by_id(self.test_image.id)
        self.assertEqual(len(Image.objects.all()), 0)



