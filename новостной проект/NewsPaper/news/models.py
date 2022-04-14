from allauth.account.forms import newsForm
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

@method_decorator(login_required, name='dispatch')
class ProtectedView(TemplateView):
    template_name = 'prodected_page.html'

class BasicSignupForm( newsForm ):

    def save(self, request):
        user = super( BasicSignupForm, self ).save( request )
        basic_group = Group.objects.get( name='basic' )
        basic_group.user_set.add( user )
        return user

