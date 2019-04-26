from django import template
from django.utils.safestring import mark_safe

import markdown2

from courses.models import Course


register = template.Library()

@register.simple_tag
def newest_course():
    """ Gets most recent course added to library """
    return Course.objects.latest('created_at')

#register.simple_tag('newest_course')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    """ Returns dict of courses to display as navigatin pane"""
    courses = Course.objects.all()
    return {'courses': courses}

#register.inclusion_tag('courses/course_nav.html')(nav_courses_list)


@register.filter('time_estimate')
def time_estimate(word_count):
    """Est the number of minutes to complete step based on wordcount"""
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML """
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
