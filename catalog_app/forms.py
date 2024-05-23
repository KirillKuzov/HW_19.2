from django import forms

from catalog_app.models import Product, Version
from common.views import StyleFormMixin


class ProductForm(StyleFormMixin):
    class Meta:
        model = Product
        exclude = ('views_count', 'created_at', 'updated_at')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        if cleaned_data in prohibited_words:
            raise forms.ValidationError('Данное слово нельзя использовать в карточке')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        if cleaned_data in prohibited_words:
            raise forms.ValidationError('Данное слово нельзя использовать в карточке')

        return cleaned_data


class VersionForm(StyleFormMixin):
    class Meta:
        model = Version
        fields = ('version_number', 'version_title', 'version_is_active')
