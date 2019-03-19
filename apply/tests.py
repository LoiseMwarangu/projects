
from django.test import TestCase
from .models import Project, Profile
from django.core.files.uploadedfile import SimpleUploadedFile


class ProjectTestClass(TestCase):

    def setUp(self):

        self.loise = .objects.create(title="loise")
        self.picture = Image.objects.create(screenshots='image1', user=self.loise)
        self.description = project.objects.create(description = 'so ugly')


        self.test_project = project.objects.create(title=self.loise, screenshots=self.image1, description='so ugly')
        self.test_project.save()

    #Testing instance

    def test_instance(self):

        self.assertTrue(isinstance(self.test_projects, project))

    #Testing Save method

    def test_save_method(self):
        projects = project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_save_project(self):
        self.assertEqual(len(project.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        project.objects.all().delete()

        # Testing delete method

    def test_delete_project(self):
        self.test_project.delete()
        self.assertEqual(len(project.objects.all()), 0)


class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):


        self.nairobi = profile.objects.create(profile="nairobi")
        self.funny=bio.objects.create(bio='funny')
        self.picture = photo.objects.create(photo='image1', user=self.loise)

        self.test_profile = profile.objects.create(profile='profilesef', description='This is a description', , )

        self.test_profile.save()

    def test_save_method(self):
        self.test_profile.save()
        test_profiles = profile.objects.all()
        self.assertTrue(len(test_profiles) > 0)

    # Testing save method
    def test_save_profile(self):
        self.assertEqual(len(profile.objects.all()), 1)

    # Tear down method
    def tearDown(self):
        profile.objects.all().delete()

    def test_delete_profile(self):
        profile.delete_profile_by_id(self.test_profile.id)
        self.assertEqual(len(profile.objects.all()), 0)



