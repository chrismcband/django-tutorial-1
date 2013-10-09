import datetime
from django.utils import timezone
from django.test import TestCase
from signup.models import Signup, Survey
from django.core.urlresolvers import reverse


class SignupViewTests(TestCase):

    def test_signup_view_with_no_contents(self):
        response = self.client.get(reverse('signup:form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First name")

    def test_signup_view_invalid_form(self):
        resp = self.client.post(reverse('signup:form'), {
            'sub_domain': u'J\xf5e Tanav 19-7!'})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('Contains unsupported characters' in str(resp))

    def test_signup_view_valid_form(self):
        resp = self.client.post(reverse('signup:form'), {\
            'first_name': 'Mark',
            'last_name': 'Lit',
            'email_address': 'mark@stickyworld.com',
            'password': 'testing123',
            'sub_domain': 'stickyworld-tallinn',
        })
        self.assertEqual(resp.status_code, 302)
        self.assertTrue('/signup/questions/1' in resp['Location'])
