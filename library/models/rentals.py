# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.bookcopie', string='Book copie')
    rental_date =  fields.Date(string='Rental date', default=fields.Date.context_today)
    return_date = fields.Date(string='Return date')
