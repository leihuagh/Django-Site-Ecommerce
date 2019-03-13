from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Full Name",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Email",
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Content",
                "rows": "4",
            }
        )
    )
