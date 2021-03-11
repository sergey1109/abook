from django import forms
from adbook1.models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"