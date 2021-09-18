from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('fe_male', 'Female')], default='male', string='Gender')
    related_user = fields.Many2one('res.users', string='Related User')
