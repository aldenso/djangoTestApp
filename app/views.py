from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Category, Product
from .forms import CustomerForm

# Create your views here.

def index(request):
	return render(request, 'app/index.html', {})

# Views for customers
def customer_list(request):
	try:
		customers = Customer.objects.all() 
		return render(request, 'app/customer_list.html', {'customers': customers})
	except:
		return render(request, 'app/customer_list.html', {})

def customer_detail(request, pk):
	customer = get_object_or_404(Customer, pk=pk)
	return render(request, 'app/customer_detail.html', {'customer': customer})

def customer_add(request):
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			customer = form.save(commit=False)
			customer.register()
			return redirect('customer_detail', pk=customer.pk)
	else:
		form = CustomerForm()
	return render(request, 'app/customer_edit.html', {'form': form})

def customer_edit(request, pk):
	customer = get_object_or_404(Customer, pk=pk)
	if request.method == "POST":
		form = CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			customer = form.save(commit=False)
			customer.register()
			return redirect('customer_detail', pk=customer.pk)
	else:
		form = CustomerForm(instance=customer)
	return render(request, 'app/customer_edit.html', {'form': form})

def customer_remove(request, pk):
	customer = get_object_or_404(Customer, pk=pk)
	customer.delete()
	customers = Customer.objects.all()
	return render(request, 'app/customer_list.html', {'customers': customers})

# Views for categories
def category_list(request):
	try:
		categories = Category.objects.all() 
		return render(request, 'app/category_list.html', {'categories': categories})
	except:
		return render(request, 'app/category_list.html', {})

def category_detail(request, pk):
	category = get_object_or_404(Category, pk=pk)
	return render(request, 'app/category_detail.html', {'category': category})