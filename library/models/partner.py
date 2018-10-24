# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Partner(models.Model):
    _inherit = 'res.partner'

    author =  fields.Boolean('is an Author', default=False)
    publisher =  fields.Boolean('is a Publisher', default=False)
    rental_ids = fields.One2many(
        'library.rental',
        'customer_id',
        string='Rentals')
    book_ids = fields.Many2many(
        comodel_name="product.product",
        string="Books",
        domain=[('book','=',True), ],
    )
    nationality_id = fields.Many2one(
        'res.country',
        'Nationality',
    )
    birthdate =  fields.Date('Birthdate',)
    payment_ids = fields.One2many('library.payments', 'customer_id', string="Payments")
    payment_count = fields.Integer("Number of payments", compute="_get_payment_count", store=False)
    
    @api.depends('session_ids')
    def _get_payment_count(self):
        for partner in self:
            partner.payment_count = len(partner.payment_ids)
