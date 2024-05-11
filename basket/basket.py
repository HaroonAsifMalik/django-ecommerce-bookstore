# This file contains functions to manage the basket:
# - Add item
# - Remove item
# - Get total price
# - Display items in the basket
from decimal import Decimal

from store.models import Product


class Basket():
    def __init__(self, request):
        """
        Initializes the Basket object with session data from the request.
        """
        self.session = request.session  # Extract session data from the request object
        basket = self.session.get('skey')  # Retrieve the basket data from the session
        if 'skey' not in request.session:  # If 'skey' is not present in the session, initialize it as an empty dictionary
            basket = self.session['skey'] = {}
        self.basket = basket  # Set the basket attribute of the Basket object

    def add(self, product, qty):
        """
        Adds a product to the basket.
        """
        print('Basket Add Function')
        product_id = str(product.id)  # Convert product ID to string
        if product_id in self.basket:  # If the product is already in the basket, update its quantity
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}  # If the product is not in the basket, add it with the specified quantity
        self.save()  # Save the basket

    def __iter__(self):
        product_ids = self.basket.keys() # Create list of keys (products ids). It have all basket productIds
        products = Product.products.filter(id__in=product_ids)  # Extract products form database
        basket = self.basket.copy()  # Create a copy of the basket

        for product in products:  # Associate each product with its corresponding item in the basket
            basket[str(product.id)]['product'] = product

        for item in basket.values():  # Convert item price to Decimal for precision
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item  # Yield the item for iteration

    def __len__(self):
        """
        Returns the total number of items in the basket.
        """
        return sum(item['qty'] for item in self.basket.values())  # Sum the quantities of all items in the basket

    def delete(self ,product):
        """
        Delete the product
        """
        product_id = str(product)
        print(product_id)
        if product_id in self.basket:
            del self.basket[product_id]
        self.save()


    def save(self):
        """
        Saves the basket data to the session.
        """
        self.session.modified = True  # Mark the session as modified to ensure it gets saved
