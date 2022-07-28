# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class action1(http.Controller):
     @http.route('/tienda', auth='public' , website=True)       
     def principal(self, **kw):
        impresora = request.env["modulo3.impresora"]
        impresoras = impresora.search([])

        
        return http.request.render('modulo3.idtienda', { 'impresoras':impresoras} )

# class Modulo3(http.Controller):
#     @http.route('/modulo3/modulo3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo3/modulo3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo3.listing', {
#             'root': '/modulo3/modulo3',
#             'objects': http.request.env['modulo3.modulo3'].search([]),
#         })

#     @http.route('/modulo3/modulo3/objects/<model("modulo3.modulo3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo3.object', {
#             'object': obj
#         })
