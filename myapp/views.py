from decimal import Decimal

from django.http import Http404, HttpResponse


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
