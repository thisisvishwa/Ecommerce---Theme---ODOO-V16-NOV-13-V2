```python
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_image = fields.Binary("Product Image", attachment=True)
    product_brand = fields.Char("Brand")
    product_specs = fields.Text("Specifications")
    product_price = fields.Float("Price")
    product_components = fields.One2many('product.component', 'product_id', string="Components")

class ProductComponent(models.Model):
    _name = 'product.component'

    name = fields.Char("Component Name")
    description = fields.Text("Description")
    price = fields.Float("Price")
    product_id = fields.Many2one('product.template', string="Product")
```