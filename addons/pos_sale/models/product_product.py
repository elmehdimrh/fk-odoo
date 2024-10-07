from odoo import models


class ProductProduct(models.Model):
    _inherit = ['product.product']

    def get_product_info_pos(self, price, quantity, pos_config_id):
        res = super().get_product_info_pos(price, quantity, pos_config_id)

        # Optional products
        res['optional_products'] = [
            {'name': p.name, 'price': min(p.product_variant_ids.mapped('lst_price'))}
            for p in self.optional_product_ids.filtered_domain(self._optional_product_pos_domain())
        ]

        return res

    def _optional_product_pos_domain(self):
        return [
            *self.env['product.product']._check_company_domain(self.env.company),
            ['sale_ok', '=', True],
            ['available_in_pos', '=', True],
        ]
