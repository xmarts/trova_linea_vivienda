# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    producto_vivienda = fields.Boolean(string="Producto de vivienda", default=False)

class TrovaVenta(models.Model):
    _inherit = "sale.order"

    @api.onchange('vivienda')
    def _get_price(self):
        producto_vivienda_search = self.env['product.template'].search([('producto_vivienda', '=', True)], limit=1)
        if producto_vivienda_search:
            if self.vivienda:
                line_ids = []
                res = {'value':{'order_line':[],}}
                line = {
                    'product_id': producto_vivienda_search.id,
                    'name': producto_vivienda_search.name,
                    'product_uom_qty': 1,
                    'price_unit': self.vivienda.precioventa,
                }
                line_ids += [line]
                res['value'].update({'order_line': line_ids,})
                return res
        else:
            raise ValidationError('No existe ningun producto de tipo vivienda, por favor asegurese de registrar un producto de este tipo')

    