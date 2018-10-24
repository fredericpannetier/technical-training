# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    _order = "rental_date desc,return_date desc"

    customer_id = fields.Many2one(
        'res.partner',
        'Customer',
        domain=[('customer','=',True), ],
        required=True,
    )
    book_id = fields.Many2one(
        'product.product',
        'Book',
        domain=[('book','=',True)],
        required=True,
    )
    rental_date = fields.Date(string='Rental date', required=True, default=lambda self: fields.Date.today())
    return_date = fields.Date(string='Return date')
    duration = fields.Integer(string='Number of days')
    payment_id = fields.Many2one(
        'library.payments', 'Payment'
    )
    
    
    @api.multi
    def action_return(self):
        self.ensure_one()
        self.return_date = fields.Date.today()
        self.duration = (self.return_date - self.rental_date).days + 1
        vals = {
            "customer_id": self.customer_id.id,
            "payment_date": self.return_date,
            "amount": self.duration * 1.0,
        }
        payment = self.env['library.payments'].create(vals)
        self.payment_id = payment.id
        
        #pour ouvrir le formulaire sur le payment
        return {
            'type': 'ir.actions.act_window',
            'name': _('Payment for rental'),
            'view_mode': 'form',
            'res_model': 'library.payments',
            'res_id': payment.id,
            'target': 'new', #pour ouvrir dans une fenêtre à part
        }
        
        
        
    @api.multi
    def action_lost(self):
        self.ensure_one()
        vals = {
            "customer_id": self.customer_id.id,
            "payment_date": fields.Date.today(),
            "amount": 50,
        }
        payment = self.env['library.payments'].create(vals)
        self.payment_id = payment.id
        
        #pour ouvrir le formulaire sur le payment
        return {
            'type': 'ir.actions.act_window',
            'name': _('Payment for rental'),
            'view_mode': 'form',
            'res_model': 'library.payments',
            'res_id': payment.id,
            'target': 'new',
        }
        
        
        
