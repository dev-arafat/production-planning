from odoo import models, fields, api

class ProductionPlanning(models.Model):
    _name = 'production.planning'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Production Planning'

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default='New')
    create_by = fields.Char(string='CreateBy', required=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Product', required=True, tracking=True)
    quantity = fields.Float(string='Quantity', tracking=True)
    ref_id = fields.Many2one('res.partner',string="Reference")
    work_order = fields.Char(string="Work Order", tracking=True)
    department = fields.Char(string="Department", required=True, tracking=True)
    supervisor = fields.Char(string="Supervisor", tracking=True)
    planned_date = fields.Datetime(string='Planned Date', tracking=True)
    planned_closing_date = fields.Datetime(string='Planned Closing Date', tracking=True)
    total_day = fields.Integer(String="Total Day", compute='_compute_day', required=True, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approve', 'Approve'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string="Status", default="draft", required=True, tracking=True)


    @api.depends('planned_date', 'planned_closing_date')
    def _compute_day(self):
        for record in self:
            if record.planned_date and record.planned_closing_date:
                delta = record.planned_closing_date - record.planned_date
                record.total_day = delta.days
            else:
                record.total_day = 0

    def print_pdf(self):
        return self.env.ref('production_planning.action_report_production_planning').report_action(self)

    def action_approve(self):
        for rec in self:
            rec.state = 'approve'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('production.planning') or 'New'
        return super(ProductionPlanning, self).create(vals)



