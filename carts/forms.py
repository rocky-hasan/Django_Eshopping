from django import forms
from carts.models import Order, OrderProduct


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address_line_1', 'address_line_2', 'country', 'state',
                  'city', 'order_note']
