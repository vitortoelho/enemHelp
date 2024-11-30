from authtools.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = ['email', 'password1', 'password2']
