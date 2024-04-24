from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=10)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентичным названию."
            )

        return cleaned_data