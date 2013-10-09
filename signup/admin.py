from django.contrib import admin
from signup.models import Signup, Survey

class SurveyAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'user_')
    list_filter = ('used_for_planning_consultation',
        'used_for_neighbourhood_planning',
        'used_for_arts_and_cultural_engagement',
        'used_for_collaborative_design_review',
        'used_for_property_marketing',
        'used_for_education',
        'used_for_other',
        'get_feedback_from_friends_and_colleagues',
        'get_feedback_from_clients_and_customers',
        'get_feedback_from_all_staff',
        'get_feedback_from_local_community',
        'get_feedback_from_anyone',
        'find_me_via_email_invite',
        'find_me_via_my_website',
        'find_me_via_my_intranet',
        'find_me_via_stickyworld')
        
    def user_(self, obj):
        return '%s %s' % (obj.signup.first_name, obj.signup.last_name)

admin.site.register(Signup)
admin.site.register(Survey, SurveyAdminConfig)
