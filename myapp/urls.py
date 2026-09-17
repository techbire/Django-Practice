from django.urls import path

from myapp.views import filter_demo, home, menu, menu_item, name_form, result


urlpatterns = [
	path('menu/', menu, name='menu'),
	path('menu/<str:item_name>/', menu_item, name='menu-item'),
	path('home/', home, name='home'),
	path('filter/', filter_demo, name='filter-demo'),
	path('result/', result, name='result'),
	path('name/', name_form, name='name-form'),
]
