```python
from odoo import http
from odoo.http import request

class MainController(http.Controller):

    @http.route('/ecommerce_theme_v2_nov_13/home', type='http', auth='public', website=True)
    def home(self, **kwargs):
        return request.render('ecommerce_theme_v2_nov_13.homepage_template')

    @http.route('/ecommerce_theme_v2_nov_13/product/<model("product.template"):product>', type='http', auth='public', website=True)
    def product(self, product, **kwargs):
        return request.render('ecommerce_theme_v2_nov_13.product_detail_template', {'product': product})

    @http.route('/ecommerce_theme_v2_nov_13/category/<model("product.category"):category>', type='http', auth='public', website=True)
    def category(self, category, **kwargs):
        return request.render('ecommerce_theme_v2_nov_13.category_template', {'category': category})

    @http.route('/ecommerce_theme_v2_nov_13/user/<model("res.users"):user>', type='http', auth='user', website=True)
    def user(self, user, **kwargs):
        return request.render('ecommerce_theme_v2_nov_13.user_dashboard_template', {'user': user})

    @http.route('/ecommerce_theme_v2_nov_13/404', type='http', auth='public', website=True)
    def error_404(self, **kwargs):
        return request.render('ecommerce_theme_v2_nov_13.404_template')

    @http.route('/ecommerce_theme_v2_nov_13/500', type='http', auth='public', website=True)
    def error_500(self, **kwargs):
        return request.render('ecommerce_theme_v2_nov_13.500_template')
```