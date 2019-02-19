from odoo import models, fields, api


class FirstModel(models.Model):
    _name = 'test_app.first_model'

    name = fields.Char(required=True)
    description = fields.Text()
    