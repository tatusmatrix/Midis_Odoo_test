# -*- coding: utf-8 -*-
# created on basis of addons -> calendar -> calendar_event.py -> Meetinng
# created on basis of addons -> project -> project_task.py -> Task

from odoo import api, fields, models
import logging
import datetime

_logger = logging.getLogger(__name__)


class Task(models.Model):
    _name = "task.manager"
    _description = "Task Manager"

    days_left = 3

    # description
    name = fields.Char('Name of the task', required=True)
    description = fields.Text('A brief description of the task')
    assigned_to = fields.Many2one('res.users')
    due_date = fields.Datetime('Due date for the task')
    priority = fields.Selection([('1', 'Low'), ('2', 'Medium'), ('3', 'High')])
    status = fields.Selection(
        [('1', 'New'), ('2', 'In Progress'), ('3', 'Completed')])

    @api.model
    def action_send_email_task_is_about_to_expire(self):
        _logger.info('Task Manager: Email task is about to expire')

        self.env.cr.execute(f'''SELECT rp.name as email_to_name, rp.email as email_to,
                            tm.name as name, tm.due_date as due_date FROM "{self._table}" tm
                            LEFT JOIN res_users ru ON tm.assigned_to=ru.id
                            LEFT JOIN res_partner rp ON ru.partner_id=rp.id''')
        tasks = self.env.cr.dictfetchall()

        for task in tasks:
            date_today = datetime.datetime.now()
            task_days_left = (task['due_date'] - date_today).days

            if task_days_left <= self.days_left:

                email_values = {
                    'task_email_to': task['email_to'],
                    'task_email_to_name': task['email_to_name'],
                    'task_name': task['name'],
                    'task_due_date': task['due_date'],
                    'task_days_left': task_days_left
                }
                template = self.env.ref(
                    'task_manager.email_template_task_is_about_to_expire')
                template.with_context(email_values).send_mail(
                    self.id, email_values=None, force_send=True)
