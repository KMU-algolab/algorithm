from django.shortcuts import render_to_response

from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        if sociallogin.account.extra_data['email'].split('@')[1] not in ['kookmin.ac.kr', 'cs.kookmin.ac.kr']:
            raise ImmediateHttpResponse(render_to_response('error.html'))
