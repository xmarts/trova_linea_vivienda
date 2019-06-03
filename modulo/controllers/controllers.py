# -*- coding: utf-8 -*-
from odoo import http

# class TrovaVenta(http.Controller):
#     @http.route('/trova_venta/trova_venta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trova_venta/trova_venta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trova_venta.listing', {
#             'root': '/trova_venta/trova_venta',
#             'objects': http.request.env['trova_venta.trova_venta'].search([]),
#         })

#     @http.route('/trova_venta/trova_venta/objects/<model("trova_venta.trova_venta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trova_venta.object', {
#             'object': obj
#         })