from django import forms
from django.forms import fields

from database.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super(StyleFormMixin, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data_name = self.cleaned_data['name']

        err = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
               'обман', 'полиция', 'радар']

        for el in err:
            if cleaned_data_name == el:
               raise forms.ValidationError('Ошибка, связанная с названием продукта')

        return cleaned_data_name


    def clean_decrp(self):
        cleaned_data_decrp = self.cleaned_data['decrp']

        err = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
               'обман', 'полиция', 'радар']

        if cleaned_data_decrp in err:
               raise forms.ValidationError('Ошибка, связанная с описанием продукта продукта')

        return cleaned_data_decrp


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'