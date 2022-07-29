# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request




class PaginaInicio(http.Controller):
     @http.route('/inicio', auth='public' , website=True)       
     def pagina_inicio(self, **kw):
        return http.request.render('modulo3.inicio')


class PaginaImpresoras(http.Controller):
     @http.route('/impresoras', auth='public' , website=True)       
     def pagina_impresoras(self, **kw):
        return http.request.render('modulo3.impresoras')



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
