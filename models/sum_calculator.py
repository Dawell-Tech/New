from odoo import models, fields, api


class SumCalculator(models.Model):
    _name = 'sum.calculator'
    _description = 'Simple Sum Calculator'

    number1 = fields.Float(string='First Number', required=True)
    number2 = fields.Float(string='Second Number', required=True)
    result = fields.Float(string='Result', compute='_compute_sum', store=True)

    @api.depends('number1', 'number2')
    def _compute_sum(self):
        for record in self:
            record.result = record.number1 + record.number2
