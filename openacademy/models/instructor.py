# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Instructor(models.Model):
    _inherit = 'res.partner'
    
    isinstructor = fields.Boolean(
        'Is instructor')
    session_ids = fields.One2many("openacademy.session", "attendee_ids", string="Sessions")
    