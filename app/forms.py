from django import forms
from .models import Customer, Category, Product

class CustomerForm(forms.ModelForm):

    class Meta():
        model = Customer
        widgets = {'registered_date': forms.HiddenInput()}
        fields = ('validation', 'first_name', 'last_name', 'customer_id', 'email', 'phone_number',
        'address', 'registered_date')

class CategoryForm(forms.ModelForm):

    class Meta():
        model = Category
        fields = ('name', 'description', 'slug', 'image')


class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        widgets = {'created_at': forms.HiddenInput(), 'modified_at':forms.HiddenInput()}
        fields = ('name', 'description', 'slug', 'price', 'category', 'image', 'created_at',
            'modified_at')          