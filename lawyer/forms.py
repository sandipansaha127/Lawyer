from django import forms
from django.utils.text import slugify

from lawyer.models import Lawyer, Category
CATEGORY_CHOICES = (
    ('CRIMINAL', 'Criminal'),
    ('EMPLOYMENT', 'Employment'),
    ('CORPORATE', 'Corporate'),)


class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(max_length=3,
                                    widget=forms.Select(choices=CATEGORY_CHOICES),)

    class Meta:
        model = Category
        fields = (
            'category_name',
            'city',
        )
    # def __init__(self,profile):
    #     super(CategoryForm, self).__init__()
    #     self.profile=profile


    # def save(self, commit=True):
    #     instancec = super(CategoryForm, self).save(commit=False)
    #     instancec.category_name=self.cleaned_data['category_name']
    #     instancec.city=self.cleaned_data['city']
    #     instancec.slug = slugify(instancec.category_name)
    #     if commit:
    #         instancec.save()

    #     return instancec


class LawyerForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = (
            'name',
            'description',
            'charge',
            'available',
        )

    # def save(self, commit=True):
    #     #instance_1 = super(CategoryForm, self).save(commit=False)
    #     instance = super(LawyerForm, self).save(commit=False)
    #     instance._name=self.cleaned_data['name']
    #     instance._description=self.cleaned_data['description']
    #     instance._charge=self.cleaned_data['charge']
    #     instance._available=self.cleaned_data['available']
    #     instance.slug = slugify(instance.name)
    #     if commit:
    #         instance.save()
    #     return instance