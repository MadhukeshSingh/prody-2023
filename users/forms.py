from django.contrib.auth.models import User
from .models import Profile
from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'email', 'password1', 'password2')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field,
                                   'label') else 'Error', error)
    return msg
