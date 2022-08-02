# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request




class Paginas(http.Controller):
     @http.route('/inicio', auth='public' , website=True)       
     def pagina_inicio(self, **kw):
        return http.request.render('modulo3.pagina_inicio')

     @http.route('/inicio/impresoras', auth='public' , website=True)       
     def pagina_tipos_impresoras(self, **kw):
        tipoimpresora = request.env["modulo3.tipoimpresora"]
        tiposimpresoras = tipoimpresora.search([])
        return http.request.render('modulo3.pagina_tipos_impresoras', { 'tiposimpresoras':tiposimpresoras } )





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
