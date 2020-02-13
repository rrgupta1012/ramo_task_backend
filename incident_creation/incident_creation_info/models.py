from django.db import models


class IncidentCreationInfo(models.Model):

    # Common fileds for all Category
    incident_category = models.CharField('Incident Category',max_length=100, null=True, blank=True)
    incident_creation_date = models.DateField('Incident Create Date', null=True, blank=True)
    incident_creation_time = models.TimeField('Incident Create Time', null=True, blank=True)

    person_reporting_name = models.CharField('Person Reporting Name',max_length=100, null=True, blank=True)
    email = models.CharField('Email',max_length=100, null=True, blank=True)
    sector = models.CharField('Sector:',max_length=100, null=True, blank=True)
    country = models.CharField('Country',max_length=100, null=True, blank=True)
    state = models.CharField('State',max_length=100, null=True, blank=True)
    mobile = models.CharField('Mobile',max_length=100, null=True, blank=True)
    detail_obtain_tool_1 = models.TextField('Details Obtained from Tool 1',max_length=100, null=True, blank=True)
    detail_obtain_tool_2 = models.TextField('Details Obtained from Tool 2',max_length=100, null=True, blank=True)
    detail_obtain_tool_3 = models.TextField('Details Obtained from Tool 3',max_length=100, null=True, blank=True)
    detail_obtain_tool_4 = models.TextField('Details Obtained from Tool 4',max_length=100, null=True, blank=True)
    detail_obtain_tool_5 = models.TextField('Details Obtained from Tool 5',max_length=100, null=True, blank=True)
    detail_obtain_tool_6 = models.TextField('Details Obtained from Tool 6',max_length=100, null=True, blank=True)
    incident_observed_date = models.DateField('Incident Observed Date', null=True, blank=True)
    incident_observed_time = models.TimeField('Incident Observed Time', null=True, blank=True)
    impacted_system_critical = models.BooleanField('Impacted System Critical', null=True, blank=True)
    phone = models.CharField('Phone:',max_length=100, null=True, blank=True)
    fax = models.CharField('Fax:',max_length=100, null=True, blank=True)
    incident_details = models.CharField('Observations/incident details',max_length=100, null=True, blank=True)
    domain_url = models.CharField('Domain Url',max_length=100, null=True, blank=True)
    ip_address = models.CharField('IP Address/Host details',max_length=100, null=True, blank=True)

    different_person_reporting_name = models.CharField('Person Reporting Name(If Different)',max_length=100, null=True, blank=True)
    different_email = models.CharField('Email(If Different)',max_length=100, null=True, blank=True)
    different_country = models.CharField('Country(If Different)',max_length=100, null=True, blank=True)
    different_state = models.CharField('State(If Different)',max_length=100, null=True, blank=True)
    different_sector = models.CharField('Sector(If Different):',max_length=100, null=True, blank=True)
    oragnaization_impacted = models.CharField('Oragnaization Impacted(if different)',max_length=100, null=True, blank=True)

    # fields only use for phishing
    impacted_system_user = models.BooleanField('Impacted System User', null=True, blank=True)
    no_user_impacted = models.IntegerField('No Of User Impacted', null=True, blank=True)
    phishing_screenshot = models.ImageField('Evidence:active phishing screenshot', null=True, blank=True)
    phishing_source_code_snippet = models.TextField('Evidence:active phishing source code snippet',max_length=100, null=True, blank=True)
    hosting_type = models.CharField('Hosting Type',max_length=100, null=True, blank=True)
    phishing_email_content = models.CharField('Phishing Email Content: (Paste)',max_length=100, null=True, blank=True)
    no_systems_impacted = models.IntegerField('No of Systems impacted', null=True, blank=True)
    operating_system = models.CharField('OS',max_length=100, null=True, blank=True)

    # fields for malware
    md5 = models.CharField('MD5',max_length=100, null=True, blank=True)
    # evidence_log_file = models.CharField('Evidence Log Files', null=True, blank=True)
    # evidence_malware_sample_files = models.CharField('Evidence Malware sample Files', null=True, blank=True)
    # evidence_md5_files = models.CharField('Evidence Malware sample Files', null=True, blank=True)
    evidence_forensic_images = models.ImageField('Evidence  forensic images', null=True, blank=True)
    malicious_email_content = models.CharField('Malicious Email Content',max_length=100, null=True, blank=True)
    evidence_malicious_email_attachments = models.CharField('Malicious Email attachments',max_length=100, null=True, blank=True)

    # fields for scanning or spamming
    isp_name = models.CharField('ISP Name',max_length=100, null=True, blank=True)
    # evidence_log_files = models.CharField('Evidence Log Files', null=True, blank=True)
    # evidence_spam_message = models.CharField('Evidence- Spam Message', null=True, blank=True)

    def __str__(self):
        return self.incident_category






