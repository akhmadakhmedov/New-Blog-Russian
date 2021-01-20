from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label = "Имя ползователья")
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label = "Имя ползователья")
    name = forms.CharField(max_length=50, label = "Имя")
    surname = forms.CharField(max_length=50, label="Фамилия")
    email = forms.EmailField(max_length=50, label = "Элект почта")
    password = forms.CharField(max_length=70, label="Пароль", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=70, label='Потверждение паролья', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        name = self.cleaned_data.get('name')
        surname = self.cleaned_data.get('surname')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Пароли не совпадает")
        values = {
            'username': username,
            'name': name,
            'surname': surname,
            'email': email,
            'password': password
        }
        return values