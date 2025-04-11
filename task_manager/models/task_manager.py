# -*- coding: utf-8 -*-
# created on basis of addons -> calendar -> calendar_event.py -> Meetinng
# created on basis of addons -> project -> project_task.py -> Task

from odoo import fields, models

class Task(models.Model):
    _name = "task.manager"
    _description = "Task Manager"
    
    # description
    name = fields.Char('Name of the task', required=True)
    description = fields.Text('A brief description of the task')
    assigned_to = fields.Many2one('res.users')
    due_date = fields.Datetime('Due date for the task')
    priority = fields.Selection([('1','Low'), ('2','Medium'), ('3','High')])
    status = fields.Selection([('1','New'), ('2','In Progress'), ('3','Completed')])
