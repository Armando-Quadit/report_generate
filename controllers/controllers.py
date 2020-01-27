# -*- coding: utf-8 -*-
from odoo import http

# class ReportGenerate(http.Controller):
#     @http.route('/report_generate/report_generate/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_generate/report_generate/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_generate.listing', {
#             'root': '/report_generate/report_generate',
#             'objects': http.request.env['report_generate.report_generate'].search([]),
#         })

#     @http.route('/report_generate/report_generate/objects/<model("report_generate.report_generate"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_generate.object', {
#             'object': obj
#         })