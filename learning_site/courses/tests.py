#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Course, Step


class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title='Python RegEx',
            description='Learn RegEx'
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python RegEx',
            description='Learn RegEx'
        )
        self.course2 = Course.objects.create(
            title='Python RegEx 2',
            description='Learn RegEx 2'
        )
        self.step = Step.objects.create(
            title = "Intro to Doctests",
            description = 'Learn to write tests',
            course = self.course,
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:course_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)
