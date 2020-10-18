from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = ('email',) # add any custom attributes here
        exclude = ('username',)
        fields = UserCreationForm.Meta.fields + ('nick',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = ('email',) # add any custom attributes here
        exclude = ('username',)
        fields = UserChangeForm.Meta.fields
