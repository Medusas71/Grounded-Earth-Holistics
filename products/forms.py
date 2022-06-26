""" Import forms, products and categories """

from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Product Form """

    class Meta:
        """ Meta """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    """ Review Form """

    class Meta:
        """ Meta """
        model = Review
        fields = ['review_title', 'review']


class CommentForm(forms.ModelForm):
    """ Comment Form """

    class Meta:
        """ Meta """
        model = Comment
        fields = ['comment']
