from django.core.urlresolvers import reverse
from django.forms import ModelForm, CharField
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from signup.models import Signup, Survey


class SignupForm(ModelForm):

    first_name = CharField(label='First name',
        help_text="Your first name")

    class Meta:
        model = Signup
        fields = ('first_name', 'last_name', 'email_address', 'password',
            'sub_domain')


def form(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signup = form.save()
            return HttpResponseRedirect(
                reverse('signup:questions', args=(signup.id,)))
    else:
        form = SignupForm()

    return render(request, 'signup/form.html', {
        'form': form,
    })


class SurveyForm(ModelForm):

    class Meta:
        model = Survey
        exclude = ('signup', 'survey_time')


def questions(request, signup_id):
    if request.method == 'POST':
        form = SurveyForm(request.POST)

        if form.is_valid():
            survey = form.save(commit=False)
            survey.signup = Signup.objects.get(pk=signup_id)
            survey.save()
            return HttpResponseRedirect(reverse('signup:thanks'))
    else:
        form = SurveyForm()

    return render(request, 'signup/questions.html', {
        'form': form,
        'signup_id': signup_id
    })


class ThanksView(generic.TemplateView):
    template_name = 'signup/thanks.html'
