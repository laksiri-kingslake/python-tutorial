from ecommerce.shopping.sales import calc_tax, calc_shipping
import ecommerce.shopping.sales as sales
# from ecommerce.shopping import sales
import sys

calc_tax()
calc_shipping()
sales.calc_tax()

print(sales.__name__)