from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

	class Meta():
		model = Customer
		widgets = {'registered_date': forms.HiddenInput()}
		fields = ('validation', 'first_name', 'last_name', 'customer_id', 'email', 'phone_number',
		'address', 'registered_date')		