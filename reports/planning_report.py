from odoo import models

class ProductionPlanningReport(models.AbstractModel):
    _name = 'report.production_planning.report_production_planning_template'
    _description = 'Production Planning Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['production.planning'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'production.planning',
            'docs': docs,
        }
