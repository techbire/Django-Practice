from django.urls import path

from myapp.views import filter_demo, home, menu, menu_item


urlpatterns = [
	path('menu/', menu, name='menu'),
	path('menu/<str:item_name>/', menu_item, name='menu-item'),
	path('home/', home, name='home'),
	path('filter/', filter_demo, name='filter-demo'),
]
