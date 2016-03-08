from django import forms
from .models import Customer, Category

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