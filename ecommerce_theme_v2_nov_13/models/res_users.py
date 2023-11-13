```python
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    wishlist_ids = fields.One2many('product.template', 'wishlist_user_id', string='Wishlist')
    order_ids = fields.One2many('sale.order', 'user_id', string='Orders')
    reward_points = fields.Integer(string='Reward Points', default=0)
    badges_ids = fields.Many2many('gamification.badge', string='Badges')

    def add_to_wishlist(self, product_id):
        product = self.env['product.template'].browse(product_id)
        self.wishlist_ids = [(4, product.id)]

    def remove_from_wishlist(self, product_id):
        product = self.env['product.template'].browse(product_id)
        self.wishlist_ids = [(3, product.id)]

    def add_reward_points(self, points):
        self.reward_points += points

    def redeem_reward_points(self, points):
        if self.reward_points >= points:
            self.reward_points -= points
        else:
            raise ValueError('Not enough reward points')

    def add_badge(self, badge_id):
        badge = self.env['gamification.badge'].browse(badge_id)
        self.badges_ids = [(4, badge.id)]
```