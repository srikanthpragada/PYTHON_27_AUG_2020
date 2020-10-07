from django import forms


class InterestForm(forms.Form):
    amount = forms.FloatField(label='Amount')
    rate = forms.FloatField(label='Interest Rate', min_value = 5, max_value = 50)


class AuthorForm(forms.Form):
    fullname = forms.CharField(label="Fullname", max_length=30, required=True)
    email = forms.EmailField(label="Email", required=True)
    mobile = forms.RegexField(label="Mobile", regex=r"\d+", required=True)

