# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class LibraryPayments(models.Model):
    _name = "library.payments"
    _description = 'Payments'
    _order = "payment_date desc"

    customer_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain=[('customer','=',True), ],
        required=True,
    )
    payment_date =  fields.Date(string='Payment date', required=True, default=lambda self: fields.Date.today())
    amount = fields.Float('Amount')