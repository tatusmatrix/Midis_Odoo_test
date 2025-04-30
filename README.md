# Midis_Odoo_test
Test of Odoo framework

## Table of contents
[Installation of Odoo v17](#installation-of-odoo-v17)  
[Configuration of PostgreSQL](#configuration-of-postgresql)  
[Configuration of Python](#configuration-of-python)  
[Nuances, (possible) issues and bugs identified](#nuances-possible-issues-and-bugs-identified)

### Installation of Odoo v17
Download Odoo [here](https://www.odoo.com/page/download).  
Odoo [documentation - by Odoo](https://www.odoo.com/documentation/17.0/).  
Odoo [documentation - by ITPP Labs](https://odoo-development.readthedocs.io/en/latest/).  
Odoo [module structure - by SpeedySense](https://speedysense.com/odoo-module-structure/).  
Odoo Community version [first steps - module + model - by Muhammad Abdullah / Youtube](https://www.youtube.com/watch?v=6w5Zk6Rkv2s).  
Solutions of the Odoo tutorials [- reports](https://github.com/odoo/technical-training-solutions/tree/17.0-J_reports).  
Odoo Community version [- a lot of how to - by Cybrosys](https://www.cybrosys.com/blog/).  

#### Work flow
Installation of Odoo (+ Python, + PostgreSQL) &rarr; Module's codes (py, xml, html, css, js, csv, etc.) &rarr; Restart of Odoo server service &rarr; Activate / Upgrade of Module (&rarr; check odoo.log)

### Configuration of PostgreSQL
PostgreSQL [documentation](https://www.postgresql.org/docs/current/).  
PostgreSQL [first steps](https://wiki.postgresql.org/wiki/First_steps).  
[PostgreSQL GUI tool - pgAdmin](https://www.postgresql.org/).

### Configuration of Python
[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/).  
[Python Crontab](https://pypi.org/project/python-crontab/).

### Nuances, (possible) issues and bugs identified
- Vital role for prefixes (?)
    - **model_name_of_model** for **model_id**
    - **model_** for **name="model_id" ref="model_name_of_model"**
    - **model_** for **name="binding_model_id" ref="model_name_of_model"**
    - **ir_cron_** for id of **model="ir.cron"**
    - **action_** for id of **model="ir.actions. ..."**
    - **email_template_** for id of **model="mail.template"**
    - **tree_** or **form_** or **kanban_** etc. for id of **model="ir.ui. ..."**
    - etc.
- Sensitive tags
    - **subject** or **email_to** etc. - *Header values may not contain linefeed or carriage return characters*
- Consistency of short information of App in Kanban view at Apps while switching on/off developer modes.
- Change of type of model in attribute for previously already mentioned record id attribute value.
- (nuance) Duplicate action at New form creates two new records (like Save action, View action and then Duplicate action).
- Additional menu created while Uninstall process can't be deleted.
