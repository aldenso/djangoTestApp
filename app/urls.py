from django.conf.urls import url
from . import views

urlpatterns = [
	# Customer patterns
	url(r'^$', views.index, name='index'),
	url(r'^customer/$', views.customer_list, name='customer_list'),
	url(r'^customer/(?P<pk>[0-9]+)/detail/$', views.customer_detail, name='customer_detail'),
	url(r'^customer/new/$', views.customer_add, name='customer_add'),
	url(r'^customer/(?P<pk>[0-9]+)/edit/$', views.customer_edit, name='customer_edit'),
	url(r'^customer/(?P<pk>[0-9]+)/remove/$', views.customer_remove, name='customer_remove'),
	# Category patterns
	url(r'^category/$', views.category_list, name='category_list'),
	url(r'^category/(?P<pk>[0-9]+)/detail/$', views.category_detail, name='category_detail'),
]