# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InfosMarcSchool(models.Model):
    _name = "infosmarc.infosmarcschool"
    _description = "Diplômes"

    school = fields.Char(string='Ecole', required=True)
    name = fields.Char(string='Intitulé', required=True)
    year = fields.Char(string='Année')
    state = fields.Selection([
        ('obtenu', 'Obtenu'),
        ('en cours', 'En cours'),
    ], required=True, default='obtenu')
    note = fields.Text(string='Description')