from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# -------------snippets for signup -----------------#
from singupApp.models import UserAdditionInfo


class SignUpForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.is_member = True
            if commit:
                user.save()
                return user


# --------------snippets for adding new username ----------------#
class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# -------------------snippets for assigning addition info to user -----------#
class CreateAdditionInfo(forms.ModelForm):
    class Meta:
        model = UserAdditionInfo
        fields = '__all__'
