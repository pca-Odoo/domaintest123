# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CrossoveredBudgetLines(models.Model):
    _inherit = 'crossovered.budget.lines'

    practical_amount = fields.Monetary(
        compute='_compute_practical_amount', string='Practical Amount', help="Amount really earned/spent.", store=True)
    progress = fields.Float('Progress', compute='_compute_progress', store=True)
    pcatestchange = fields.Float('Test new change', store=True)

    @api.depends('practical_amount', 'planned_amount')
    def _compute_progress(self):
        for line in self:
            line.progress = (line.practical_amount / line.planned_amount) * 100

    @api.depends('general_budget_id', 'date_to', 'date_from', 'analytic_account_id')
    def _compute_practical_amount(self):
        super()._compute_practical_amount()
