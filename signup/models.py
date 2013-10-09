import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Model, CharField, DateTimeField, \
    ForeignKey, IntegerField, BooleanField
from django.utils import timezone
import pytz
import re
import string


def good_subdomain(value):
    value = value.strip().lower()
    count = Signup.objects.filter(sub_domain=value).count()

    if count:
        raise ValidationError('Sub-domain is taken')

    if value != re.sub(r'[^a-zA-Z0-9\-]+', '', value, re.UNICODE):
        raise ValidationError('Contains unsupported characters')

    if len(value) > 75:
        raise ValidationError('Is too long')

    if len(value) < 2:
        raise ValidationError('Is too short')


class Signup(Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)
    email_address = CharField(max_length=200, validators=[validate_email])
    password = CharField(max_length=1024)
    sub_domain = CharField(max_length=75, validators=[good_subdomain])
    signup_time = DateTimeField('Time of Signup')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def was_signed_up_in_last_thirty_days(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.pub_date < now

    def save(self, *args, **kwargs):
        if not self.signup_time:
            self.signup_time = \
                datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

        return super(Signup, self).save(*args, **kwargs)


class Survey(Model):
    signup = ForeignKey(Signup)
    survey_time = DateTimeField('Time of Survey')

    used_for_planning_consultation = BooleanField(default=False)
    used_for_neighbourhood_planning = BooleanField(default=False)
    used_for_arts_and_cultural_engagement = BooleanField(default=False)
    used_for_collaborative_design_review = BooleanField(default=False)
    used_for_property_marketing = BooleanField(default=False)
    used_for_education = BooleanField(default=False)
    used_for_other = BooleanField(default=False)
    used_for_other_specified = \
        CharField(max_length=200, default='', blank=True)

    get_feedback_from_friends_and_colleagues = BooleanField(default=False)
    get_feedback_from_clients_and_customers = BooleanField(default=False)
    get_feedback_from_all_staff = BooleanField(default=False)
    get_feedback_from_local_community = BooleanField(default=False)
    get_feedback_from_anyone = BooleanField(default=False)

    find_me_via_email_invite = BooleanField(default=False)
    find_me_via_my_website = BooleanField(default=False)
    find_me_via_my_website_url = \
        CharField(max_length=200, default='', blank=True)
    find_me_via_my_intranet = BooleanField(default=False)
    find_me_via_my_intranet_org_name = \
        CharField(max_length=200, default='', blank=True)
    find_me_via_stickyworld = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.survey_time:
            self.survey_time = \
                datetime.datetime.utcnow().replace(tzinfo=pytz.utc)

        return super(Survey, self).save(*args, **kwargs)
