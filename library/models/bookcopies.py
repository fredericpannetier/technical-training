# -*- coding: utf-8 -*-
from odoo import models, fields

class BookCopies(models.Model):
    _name = 'library.bookcopie'
    _description = 'Copy of a book'
    _inherits = {'library.book':'original_id'}
    _order = 'copyref'
    
    copyref=fields.Char('Copy reference', )
    original_id = fields.Many2one('library.book', string='Original', required=True, ondelete='cascade')
    
    _sql_constraints = [
        ('copyref_unique', 'UNIQUE (copyref)', 'Copy ref must be unique.'),
    ]
    
    