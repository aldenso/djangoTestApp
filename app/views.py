from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Category, Product
from .forms import CustomerForm, CategoryForm, ProductForm

# Create your views here.

def index(request):
	return render(request, 'app/index.html', {})

# Views for customers
def customer_list(request):
	customers = Customer.objects.all() 
	return render(request, 'app/customer_list.html', {'customers': customers})

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
	categories = Category.objects.all()
	return render(request, 'app/category_list.html', {'categories': categories})

def category_detail(request, pk):
	category = get_object_or_404(Category, pk=pk)
	return render(request, 'app/category_detail.html', {'category': category})

def category_add(request):
	if request.method == "POST":
		form = CategoryForm(request.POST, request.FILES)
		if form.is_valid():
			category = form.save(commit=False)
			category.register()
			return redirect('category_detail', pk=category.pk)
	else:
		form = CategoryForm()
	return render(request, 'app/category_edit.html', {'form': form})

def category_edit(request, pk):
	category = get_object_or_404(Category, pk=pk)
	if request.method == "POST":
		form = CategoryForm(request.POST, request.FILES, instance=category)
		if form.is_valid():
			category = form.save(commit=False)
			category.modify()
			return redirect('category_detail', pk=category.pk)
	else:
		form = CategoryForm(instance=category)
	return render(request, 'app/category_edit.html', {'form': form})

def category_remove(request, pk):
	category = get_object_or_404(Category, pk=pk)
	category.delete()
	categories = Category.objects.all()
	return render(request, 'app/category_list.html', {'categories': categories})

# Views for Products
def product_list(request):
	products = Product.objects.all()
	return render(request, 'app/product_list.html', {'products': products})

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'app/product_detail.html', {'product': product})

def product_add(request):
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.register()
			return redirect('product_detail', pk=product.pk)
	else:
		form = ProductForm()
	return render(request, 'app/product_edit.html', {'form': form})

def product_edit(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			product = form.save()
			product.modify()
			return redirect('product_detail', pk=product.pk)
	else:
		form = ProductForm(instance=product)
	return render(request, 'app/product_edit.html', {'form': form})

def product_remove(request, pk):
	product = get_object_or_404(Product, pk=pk)
	product.delete()
	products = Product.objects.all()
	return render(request, 'app/product_list.html', {'products': products})