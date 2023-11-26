class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        model._meta.get_field('email')._unique = True
        fields = ("username", "email", "password1", "password2")
