# Generated by Django 3.0.3 on 2020-02-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident_creation_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incidentcreationinfo',
            name='first_name',
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='detail_obtain_tool_1',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Details Obtained from Tool 1'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='detail_obtain_tool_2',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Details Obtained from Tool 2'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='detail_obtain_tool_3',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Details Obtained from Tool 3'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='detail_obtain_tool_4',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Details Obtained from Tool 4'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='detail_obtain_tool_5',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Details Obtained from Tool 5'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='detail_obtain_tool_6',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Details Obtained from Tool 6'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='different_country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country(If Different)'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='different_email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email(If Different)'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='different_person_reporting_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Person Reporting Name(If Different)'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='different_sector',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sector(If Different):'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='different_state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State(If Different)'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='domain_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Domain Url'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='evidence_forensic_images',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Evidence  forensic images'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='evidence_malicious_email_attachments',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Malicious Email attachments'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='fax',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Fax:'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='hosting_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Hosting Type'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='impacted_system_critical',
            field=models.BooleanField(blank=True, null=True, verbose_name='Impacted System Critical'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='impacted_system_user',
            field=models.BooleanField(blank=True, null=True, verbose_name='Impacted System User'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='incident_category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Incident Category'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='incident_creation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Incident Create Date'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='incident_creation_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Incident Create Time'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='incident_details',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Observations/incident details'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='incident_observed_date',
            field=models.DateField(blank=True, null=True, verbose_name='Incident Observed Date'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='incident_observed_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Incident Observed Time'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='ip_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='IP Address/Host details'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='isp_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ISP Name'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='malicious_email_content',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Malicious Email Content'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='md5',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='MD5'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='mobile',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mobile'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='no_systems_impacted',
            field=models.IntegerField(blank=True, null=True, verbose_name='No of Systems impacted'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='no_user_impacted',
            field=models.IntegerField(blank=True, null=True, verbose_name='No Of User Impacted'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='operating_system',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='OS'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='oragnaization_impacted',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Oragnaization Impacted(if different)'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='person_reporting_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Person Reporting Name'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='phishing_email_content',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phishing Email Content: (Paste)'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='phishing_screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Evidence:active phishing screenshot'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='phishing_source_code_snippet',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Evidence:active phishing source code snippet'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone:'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='sector',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sector:'),
        ),
        migrations.AddField(
            model_name='incidentcreationinfo',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
    ]
