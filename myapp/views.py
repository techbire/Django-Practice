from decimal import Decimal
from django.shortcuts import render
from django.http import Http404, HttpResponse

# menu items demo
MENU_ITEMS = {
	'burger': Decimal('5.99'),
	'pizza': Decimal('8.49'),
	'pasta': Decimal('7.99'),
	'salad': Decimal('4.99'),
}


def menu_item(request, item_name):
	item_name = item_name.lower()
	price = MENU_ITEMS.get(item_name)

	if price is None:
		raise Http404('Menu item not found.')

	display_name = item_name.title()
	return HttpResponse(f'{display_name}: ${price:.2f}')


def menu(request):
	items = '\n'.join(
		f'{item_name.title()}: ${price:.2f}'
		for item_name, price in MENU_ITEMS.items()
	)
	return HttpResponse(items, content_type='text/plain')



def home(request):
    return render(request,"home.html")

def filter_demo(request):
	context={
		"name":"ansh",
		"course":"btech",
		"city":"ballia",
		"students":["aa","bb","cc"]
	}
	return render(request,'filter.html',context)