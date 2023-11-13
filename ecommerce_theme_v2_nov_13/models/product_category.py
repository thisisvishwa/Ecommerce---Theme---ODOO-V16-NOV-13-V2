```python
from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.category'

    # Adding new fields for advanced filters
    price_range = fields.Selection([
        ('1', 'Under $500'),
        ('2', '$500 to $1000'),
        ('3', '$1000 to $2000'),
        ('4', 'Over $2000'),
    ], string='Price Range')

    brand = fields.Many2one('res.partner', string='Brand')

    specs = fields.Text(string='Specifications')

    # Adding a field for comparison feature
    can_be_compared = fields.Boolean(string='Can be compared', default=True)
```