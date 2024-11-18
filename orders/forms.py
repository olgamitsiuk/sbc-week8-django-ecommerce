from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity', 'order_date']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity',
                'min': '1'
            }),
            'order_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
        help_texts = {
            'quantity': 'Enter a positive number',
            'order_date': 'Select the date of the order'
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 1:
            raise forms.ValidationError("Quantity must be greater than zero")
        return quantity