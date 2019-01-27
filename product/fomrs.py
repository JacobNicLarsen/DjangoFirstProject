from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your title"
        }
    ))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        else:
            return title


class RawProductFrom(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Your title"
        }
    ))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "placeholder": "Your Description",
                "id": "my-id-for-textarea",
                "rows": 20,
                'cos': 20
            }
        ))
    price = forms.DecimalField()