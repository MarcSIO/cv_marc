# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InfosMarcJobs(models.Model):
    _name = "infosmarc.infosmarcjobs"
    _description = "Expériences professionnelles"

    society = fields.Char(string='Société', required=True)
    poste = fields.Char(string='Poste', required=True)
    year = fields.Char(string='Année')
    contract = fields.Selection([
        ('cdi', 'CDI'),
        ('cdd', 'CDD'),
        ('alternance', 'Alternance'),
    ], required=True, default='cdi', string='Contrat')
    note = fields.Text(string='Description')