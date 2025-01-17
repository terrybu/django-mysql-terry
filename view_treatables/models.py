# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Treatables(models.Model):
    # Define fields matching the columns in your view
    market = models.CharField(db_column='market',max_length=255)
    customer_id = models.IntegerField(db_column='customer_id', primary_key=True)
    first_name = models.CharField(db_column='first_name', max_length=255)  # Field name made lowercase.
    last_name = models.CharField(db_column='last_name', max_length=255)  # Field name made lowercase.
    account_number = models.CharField(db_column='account_number', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pending_reason = models.CharField(db_column='pending_reason', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    third_party_verification = models.CharField(db_column='third_party_verification', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fico = models.IntegerField(db_column='fico')
    lmi_status = models.CharField(db_column='lmi_status', max_length=255)
    account_verified = models.CharField(db_column='account_verified', max_length=255)
    class Meta:
        managed = False
        db_table = 'treatables'  # Replace with the actual name of your view

class Cep(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    cep_code = models.CharField(db_column='CEP_code', max_length=80)  # Field name made lowercase.
    partner_name = models.CharField(max_length=80)
    partner_incentive = models.IntegerField(blank=True, null=True)
    enrollee_incentive = models.IntegerField(blank=True, null=True)
    contact_person = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    offer_condition = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'CEP'


class CmpRate(models.Model):
    date_start = models.DateField(db_column='Date_Start', blank=True, null=True)  # Field name made lowercase.
    date_end = models.DateField(db_column='Date_End', blank=True, null=True)  # Field name made lowercase.
    rate_category = models.CharField(db_column='Rate_Category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    delivery_and_transmission = models.DecimalField(db_column='Delivery_and_transmission', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    standard_offer = models.DecimalField(db_column='Standard_Offer', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    full_rate = models.DecimalField(db_column='Full_rate', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    active = models.CharField(db_column='Active', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMP_rate'


class GcSentMstrsfnytest(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    cust_id = models.IntegerField(blank=True, null=True)
    date_processed = models.DateField(db_column='Date_Processed', blank=True, null=True)  # Field name made lowercase.
    date_submitted = models.DateField(db_column='Date_Submitted', blank=True, null=True)  # Field name made lowercase.
    date_shipped = models.DateField(db_column='Date_Shipped', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoice_number = models.CharField(db_column='Invoice_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gc_type = models.CharField(db_column='GC_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submission_id_for_change_of_info_form = models.CharField(db_column='Submission_ID_for_Change_of_Info_Form', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GC_sent_MSTRSFNYtest'


class GcSentMstrtest(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    cust_id = models.IntegerField(blank=True, null=True)
    date_processed = models.DateField(db_column='Date_Processed', blank=True, null=True)  # Field name made lowercase.
    date_submitted = models.DateField(db_column='Date_Submitted', blank=True, null=True)  # Field name made lowercase.
    date_shipped = models.DateField(db_column='Date_Shipped', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoice_number = models.CharField(db_column='Invoice_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gc_type = models.CharField(db_column='GC_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submission_id_for_change_of_info_form = models.CharField(db_column='Submission_ID_for_Change_of_Info_Form', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'GC_sent_MSTRtest'


class LmiStatustest(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    cust_id = models.IntegerField(blank=True, null=True)
    cust_account_number = models.CharField(max_length=255, blank=True, null=True)
    cust_enrollment_id = models.CharField(max_length=255, blank=True, null=True)
    number_4506_t_submitted = models.DateField(db_column='4506-T_submitted', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    transcript_received = models.DateField(blank=True, null=True)
    census_blkgrp_geoid = models.CharField(max_length=80, blank=True, null=True)
    pct_lmi_census_blkgrp = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    lmi_status = models.CharField(db_column='LMI_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lmi_category = models.CharField(db_column='LMI_category', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lmi_decision = models.CharField(db_column='LMI_decision', max_length=255, blank=True, null=True)  # Field name made lowercase.
    payment_assistance = models.CharField(max_length=255, blank=True, null=True)
    housing_assistance = models.CharField(max_length=255, blank=True, null=True)
    lmi_status_date = models.DateField(db_column='LMI_status_date', blank=True, null=True)  # Field name made lowercase.
    communication_language = models.CharField(max_length=255, blank=True, null=True)
    enroll_form = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'LMI_statustest'


class MstrCustlist(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    current_farm_id = models.IntegerField(blank=True, null=True)
    original_farm_id = models.IntegerField(blank=True, null=True)
    enroll_date = models.DateField(db_column='Enroll Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    member_id = models.IntegerField(blank=True, null=True)
    salesweekend = models.DateField(db_column='SalesWeekEnd', blank=True, null=True)  # Field name made lowercase.
    enrollment_documents = models.CharField(db_column='Enrollment Documents', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cancel_date = models.DateField(db_column='Cancel Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cancel_reason = models.CharField(max_length=255)
    cancel_type = models.CharField(max_length=255)
    cancel_source = models.CharField(max_length=20)
    fname = models.CharField(db_column='FNAME', max_length=255)  # Field name made lowercase.
    lname = models.CharField(db_column='LNAME', max_length=255)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    email_status = models.CharField(db_column='Email Status', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paperless_opt_in = models.CharField(max_length=10)
    language_pref = models.CharField(max_length=10)
    phone = models.CharField(db_column='Phone', max_length=255)  # Field name made lowercase.
    phone_type = models.CharField(db_column='Phone Type', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_2 = models.CharField(db_column='Phone 2', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_address = models.CharField(db_column='Service Address', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_address_2 = models.CharField(db_column='Service Address 2', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_city = models.CharField(db_column='Service City', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_state = models.CharField(db_column='Service State', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_zip = models.CharField(db_column='Service Zip', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_county = models.CharField(db_column='Service County', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_address = models.CharField(db_column='Bill Address', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_city = models.CharField(db_column='Bill City', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_state = models.CharField(db_column='Bill State', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_zip = models.CharField(db_column='Bill Zip', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_county = models.CharField(db_column='Bill County', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utility = models.CharField(db_column='Utility', max_length=255)  # Field name made lowercase.
    esco = models.IntegerField()
    zone = models.CharField(db_column='Zone', max_length=255)  # Field name made lowercase.
    number_of_accounts = models.CharField(db_column='Number of Accounts', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    budget_bill = models.CharField(db_column='Budget Bill', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    account_number = models.CharField(db_column='Account Number', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pod_id = models.CharField(db_column='POD ID', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utility_account_number = models.CharField(db_column='Utility_Account_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enrollment_id = models.CharField(db_column='Enrollment ID', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pe_status = models.CharField(db_column='PE_status', max_length=255)  # Field name made lowercase.
    promo_code = models.CharField(db_column='Promo Code', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral = models.CharField(db_column='Referral', max_length=255)  # Field name made lowercase.
    channel = models.CharField(db_column='Channel', max_length=255)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=255)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=255)  # Field name made lowercase.
    agent_id = models.CharField(db_column='Agent ID', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plan = models.CharField(db_column='Plan', max_length=255)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=255)  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=80, blank=True, null=True)  # Field name made lowercase.
    arr_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    cap_rate = models.FloatField(db_column='Cap Rate', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_type = models.CharField(db_column='Payment Type', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    internal_exceptions = models.CharField(db_column='Internal Exceptions', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_id = models.CharField(db_column='Payment ID', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paymentprofileid = models.CharField(db_column='PaymentProfileID', max_length=255)  # Field name made lowercase.
    customerprofileid = models.CharField(db_column='CustomerProfileID', max_length=255)  # Field name made lowercase.
    payment_profile_updated = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=10)
    cc_zip = models.CharField(max_length=10)
    tpv_id = models.CharField(db_column='TPV ID', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scored = models.CharField(db_column='Scored', max_length=255)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    fico = models.IntegerField(db_column='FICO', blank=True, null=True)  # Field name made lowercase.
    tec = models.IntegerField(db_column='TEC', blank=True, null=True)  # Field name made lowercase.
    bcs = models.IntegerField(db_column='BCS', blank=True, null=True)  # Field name made lowercase.
    payment_history = models.CharField(max_length=255)
    annual_volume = models.IntegerField(db_column='Annual Volume', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    read_type = models.CharField(db_column='Read Type', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profile = models.CharField(max_length=255)
    read_cycle = models.CharField(max_length=255)
    service_class = models.CharField(max_length=255)
    revenue_class = models.CharField(db_column='Revenue Class', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rate_category = models.CharField(db_column='Rate Category', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rate_category_original = models.CharField(max_length=255)
    rate_class = models.CharField(max_length=80, blank=True, null=True)
    mtc_eligible = models.CharField(db_column='MTC_Eligible', max_length=10)  # Field name made lowercase.
    bill_credit = models.FloatField(db_column='Bill Credit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    survey_credit = models.FloatField(blank=True, null=True)
    courtesy_credit = models.FloatField(blank=True, null=True)
    welcome_letter_sent = models.DateField(db_column='Welcome Letter Sent', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    promo_due = models.FloatField(db_column='Promo Due', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    welcome_letter_type = models.CharField(max_length=255)
    reward_type = models.CharField(max_length=255)
    override_due = models.FloatField(db_column='Override Due', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    override_paid = models.DateField(db_column='Override Paid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    override_agent = models.CharField(db_column='Override Agent', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sfny_agent = models.CharField(db_column='SFNY Agent', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    signature_required = models.CharField(max_length=255)
    organization = models.CharField(db_column='Organization', max_length=255)  # Field name made lowercase.
    organization_payment = models.FloatField(db_column='Organization Payment', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization_paid = models.DateField(db_column='Organization Paid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sbc_location = models.CharField(db_column='SBC Location', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ib_sr_location = models.CharField(db_column='IB SR Location', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tpv_location = models.CharField(db_column='TPV Location', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_report_location = models.CharField(db_column='Credit Report Location', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    audit_status = models.CharField(db_column='Audit Status', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    credits_start_date = models.DateField(blank=True, null=True)
    usage_updated_on = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=255)
    phone_2_type = models.CharField(max_length=255)
    billing_address_2 = models.CharField(max_length=255)
    allocation_score = models.CharField(max_length=5)
    allocation_status = models.CharField(max_length=20)
    autopay_hold_reason = models.CharField(max_length=255)
    autopay_log_action_id = models.IntegerField(blank=True, null=True)
    commission_volume = models.IntegerField(blank=True, null=True)
    commission_allo_date = models.DateField(blank=True, null=True)
    rooftop_solar = models.CharField(max_length=255)
    ssn = models.CharField(max_length=255)
    account_verified = models.CharField(max_length=255)
    sent_to_developer_client = models.DateField(blank=True, null=True)
    confirmed_sale_by_developer = models.DateField(blank=True, null=True)
    commission_paid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_added = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=255)
    energy_supplier = models.CharField(max_length=255)
    annual_usage_dc = models.IntegerField(blank=True, null=True)
    disclosure_form = models.CharField(max_length=255)
    agreement = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    dg_customer = models.CharField(max_length=3, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'MSTR CUSTLIST'


class AllFarms(models.Model):
    developer = models.CharField(max_length=17)
    project = models.CharField(max_length=255, db_collation='utf8_general_ci')
    msql_id = models.IntegerField()
    project_type = models.CharField(max_length=10, db_collation='utf8_general_ci')
    array = models.CharField(max_length=20, db_collation='utf8_general_ci')
    account_number = models.CharField(max_length=255, db_collation='utf8_general_ci')
    llc_name = models.CharField(max_length=255, db_collation='utf8_general_ci')
    address = models.CharField(max_length=255, db_collation='utf8_general_ci')
    city = models.CharField(max_length=255, db_collation='utf8_general_ci')
    state = models.CharField(max_length=255, db_collation='utf8_general_ci')
    zip = models.CharField(max_length=255, db_collation='utf8_general_ci')
    zone = models.CharField(max_length=10, db_collation='utf8_general_ci')
    utility = models.CharField(max_length=255, db_collation='utf8_general_ci')
    pto = models.DateField(blank=True, null=True)
    capacity_kwh = models.IntegerField(blank=True, null=True)
    capacity_dc = models.IntegerField(blank=True, null=True)
    yield_field = models.DecimalField(db_column='yield', max_digits=12, decimal_places=2, blank=True, null=True)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'all_farms'

class AwsSqlReports(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    report = models.CharField(max_length=255, blank=True, null=True)
    db = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aws_sql_reports'


class CallLog(models.Model):
    developer = models.CharField(max_length=80, blank=True, null=True)
    call_date = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    account_number = models.IntegerField(blank=True, null=True)
    number_contacts = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    msql_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'call_log'


class CreditTransactions(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    credit_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'credit_transactions'


class Credits(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=80)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'credits'


class DeveloperDb(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    developer = models.CharField(max_length=255, blank=True, null=True)
    db = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developer_db'


class Email2Developer(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    developer = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_2_developer'



class FarmHostCreditsBeforeautomation(models.Model):
    farm_prod_id = models.IntegerField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    year_month = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    serviced_by = models.CharField(max_length=10, blank=True, null=True)
    account = models.CharField(max_length=255, blank=True, null=True)
    premise_number = models.CharField(db_column='Premise_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    garden_id = models.CharField(db_column='Garden_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tariff_rate = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    bill_start = models.DateField(blank=True, null=True)
    bill_end = models.DateField(blank=True, null=True)
    cdg_kwh_applied = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdg_kwh = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdg_bill_credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdg_bill_credit_statement = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdg_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cdg_charge = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True, db_comment='C= Credit / R= Reversal\n\nFrom NYSEG - when a credit is created based on an estimated meter reading and subsequently the actual reading comes in significantly different, the credit might be reversed and re-posted.  We need to back out and adjust our billing based on this reversal and reposting of credits.')
    cr_count = models.IntegerField(db_column='CR_count')  # Field name made lowercase.
    monthly_bank_contribution = models.DecimalField(db_column='Monthly Bank Contribution', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'farm_host_credits_beforeautomation'


class Farms(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    project = models.CharField(max_length=255)
    tgc_project = models.CharField(max_length=255)
    project_fund = models.CharField(max_length=80)
    project_type = models.CharField(max_length=10)
    array = models.CharField(max_length=20)
    serviced_by = models.CharField(max_length=10)
    nyseg_template = models.CharField(max_length=80)
    account_number = models.CharField(max_length=255)
    account_number_nyseg_report = models.CharField(max_length=255)
    llc_name = models.CharField(db_column='LLC_Name', max_length=255)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    zone = models.CharField(max_length=10)
    utility = models.CharField(max_length=255)
    pto = models.DateField(blank=True, null=True)
    interconnection_number = models.IntegerField(blank=True, null=True)
    capacity_kwh = models.IntegerField(blank=True, null=True)
    capacity_dc = models.IntegerField(blank=True, null=True)
    yield_field = models.DecimalField(db_column='yield', max_digits=10, decimal_places=2, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    p50_7pct = models.IntegerField(db_column='P50-7pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capacity_rce = models.IntegerField(blank=True, null=True)
    allocation = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    status = models.CharField(max_length=255)
    date_energized = models.DateField(blank=True, null=True)
    group_project_name = models.CharField(max_length=255)
    group_project_name_abbrev = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    garden_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'farms'


class FarmsCopy1(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    project = models.CharField(max_length=255)
    tgc_project = models.CharField(max_length=255)
    project_fund = models.CharField(max_length=80)
    project_type = models.CharField(max_length=10)
    array = models.CharField(max_length=20)
    serviced_by = models.CharField(max_length=10)
    nyseg_template = models.CharField(max_length=80)
    account_number = models.CharField(max_length=255)
    account_number_nyseg_report = models.CharField(max_length=255)
    llc_name = models.CharField(db_column='LLC_Name', max_length=255)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    zone = models.CharField(max_length=10)
    utility = models.CharField(max_length=255)
    pto = models.DateField(blank=True, null=True)
    interconnection_number = models.IntegerField(blank=True, null=True)
    capacity_kwh = models.IntegerField(blank=True, null=True)
    capacity_dc = models.IntegerField(blank=True, null=True)
    yield_field = models.DecimalField(db_column='yield', max_digits=10, decimal_places=2, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    p50_7pct = models.IntegerField(db_column='P50-7pct', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capacity_rce = models.IntegerField(blank=True, null=True)
    allocation = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    status = models.CharField(max_length=255)
    date_energized = models.DateField(blank=True, null=True)
    group_project_name = models.CharField(max_length=255)
    group_project_name_abbrev = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    garden_id = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'farms_copy1'


class Fernando(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fernando'


class FormstackConfirmation(models.Model):
    msql_id = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    likely_to_recomment = models.CharField(max_length=10, blank=True, null=True)
    cancellation_reason = models.CharField(max_length=255, blank=True, null=True)
    other_reason = models.CharField(max_length=255, blank=True, null=True)
    was_agent_informative = models.CharField(max_length=255, blank=True, null=True)
    cancel_enrollment = models.CharField(max_length=10, blank=True, null=True)
    how_to_improve = models.CharField(max_length=255, blank=True, null=True)
    fname = models.CharField(max_length=80, blank=True, null=True)
    lname = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    city = models.CharField(max_length=80, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    unique_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formstack_confirmation'


class FtFields(models.Model):
    field_id = models.AutoField(primary_key=True)
    form = models.ForeignKey('FtForms', models.DO_NOTHING)
    ft_field_id = models.PositiveIntegerField()
    ft_field_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ft_fields'


class FtForms(models.Model):
    form_id = models.AutoField(primary_key=True)
    ft_form_id = models.PositiveIntegerField(unique=True)
    form_name = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    last_update_date = models.DateTimeField()
    active = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ft_forms'


class FtSubmissionData(models.Model):
    submission_data_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(FtForms, models.DO_NOTHING)
    ft_submission_id = models.IntegerField()
    ft_field_id = models.IntegerField()
    ft_field_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ft_submission_data'


class FtSubmissionHeaders(models.Model):
    submission_header_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(FtForms, models.DO_NOTHING)
    ft_submission_id = models.PositiveIntegerField(unique=True)
    ft_submission_latitude = models.CharField(max_length=255)
    ft_submission_longitude = models.CharField(max_length=255)
    ft_submission_remote_addr = models.CharField(max_length=15)
    ft_submission_timestamp = models.DateTimeField()
    ft_submission_user_agent = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ft_submission_headers'


class HsCountTemp(models.Model):
    developer = models.CharField(max_length=261, db_collation='utf8_general_ci')
    cust_id = models.CharField(max_length=273, db_collation='utf8_general_ci')
    fname = models.CharField(db_column='FNAME', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    lname = models.CharField(db_column='LNAME', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    service_address = models.CharField(db_column='Service Address', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_address_2 = models.CharField(db_column='Service Address 2', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_city = models.CharField(db_column='Service City', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_state = models.CharField(db_column='Service State', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_zip = models.CharField(db_column='Service Zip', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_address = models.CharField(db_column='Bill Address', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    billing_address_2 = models.CharField(max_length=255, db_collation='utf8_general_ci')
    bill_city = models.CharField(db_column='Bill City', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_state = models.CharField(db_column='Bill State', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bill_zip = models.CharField(db_column='Bill Zip', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.CharField(db_column='Email', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    phone_type = models.CharField(db_column='Phone Type', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    utility = models.CharField(db_column='Utility', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    account_number = models.CharField(db_column='Account Number', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    current_farm_id = models.IntegerField(blank=True, null=True)
    farm_name = models.CharField(db_column='Farm Name', max_length=255, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    allocation_status = models.CharField(max_length=20, db_collation='utf8_general_ci')
    cancel_date = models.DateField(db_column='Cancel Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    balance_due = models.DecimalField(max_digits=32, decimal_places=2, blank=True, null=True)
    balance_status = models.CharField(db_column='Balance Status', max_length=48, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stripe_id = models.CharField(db_column='Stripe ID', max_length=80, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    url_account = models.CharField(max_length=306, db_collation='utf8_general_ci', blank=True, null=True)
    created_at = models.DateTimeField(db_column='Created At', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    modified_at = models.CharField(db_column='Modified At', max_length=19, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    serviced_by = models.CharField(db_column='Serviced By', max_length=10, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cancel_type = models.CharField(db_column='Cancel Type', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_type = models.CharField(db_column='Payment Type', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    plan_discount = models.CharField(db_column='Plan Discount', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_status = models.CharField(db_column='Payment Status', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_failed_message = models.CharField(db_column='Payment Failed Message', max_length=80, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lmi_status = models.CharField(db_column='LMI Status', max_length=255, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enrollment_id = models.CharField(db_column='Enrollment ID', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    enrollment_date = models.DateField(db_column='Enrollment Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referral = models.CharField(db_column='Referral', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    last_amount_paid = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    last_payment_date = models.DateField(blank=True, null=True)
    payment_confirmation_number = models.CharField(max_length=22, blank=True, null=True)
    account_status = models.CharField(max_length=124, blank=True, null=True)
    bill_credit = models.FloatField(db_column='Bill Credit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    first_allocation_date = models.DateField(db_column='First Allocation Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cancel_reason = models.CharField(db_column='Cancel Reason', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cancel_source = models.CharField(db_column='Cancel Source', max_length=20, db_collation='utf8_general_ci')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    scored = models.CharField(db_column='Scored', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
    fico = models.IntegerField(db_column='FICO', blank=True, null=True)  # Field name made lowercase.
    dealname = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    subscription_type = models.CharField(max_length=255, db_collation='utf8_general_ci')
    enrollment_stage = models.CharField(max_length=16)
    kwh = models.IntegerField(blank=True, null=True)
    kw = models.DecimalField(db_column='KW', max_digits=14, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rate_class = models.CharField(max_length=80, db_collation='utf8_general_ci', blank=True, null=True)
    debtor_number = models.CharField(max_length=255, db_collation='utf8_general_ci')
    premise_number = models.CharField(max_length=255, db_collation='utf8_general_ci')
    dg_customer = models.CharField(db_column='DG Customer', max_length=3, db_collation='utf8_general_ci', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    member_id = models.IntegerField(db_column='Member ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company = models.CharField(db_column='Company', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hs_count_temp'


class HubspotEmailEvents(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    created = models.DateTimeField()
    emailid = models.IntegerField()
    eventid = models.CharField(max_length=255, blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    appname = models.CharField(db_column='appName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attempt = models.CharField(max_length=255, blank=True, null=True)
    response = models.CharField(max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='linkId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    dropmessage = models.CharField(db_column='dropMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dropreason = models.CharField(db_column='dropReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    subscriptions = models.CharField(max_length=255, blank=True, null=True)
    portalsubscriptionstatus = models.CharField(db_column='portalSubscriptionStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourceid = models.CharField(db_column='sourceId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    bcc = models.CharField(max_length=255, blank=True, null=True)
    replyto = models.CharField(db_column='replyTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    from_field = models.CharField(db_column='from', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    suppressedmessage = models.CharField(db_column='suppressedMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suppressedreason = models.CharField(db_column='suppressedReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='deviceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useragent = models.CharField(db_column='userAgent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    browser_name = models.CharField(db_column='browser.name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_family = models.CharField(db_column='browser.family', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_producer = models.CharField(db_column='browser.producer', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_producerurl = models.CharField(db_column='browser.producerUrl', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    browser_type = models.CharField(db_column='browser.type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_url = models.CharField(db_column='browser.url', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sentby_created = models.DateTimeField(db_column='sentBy.created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hubspot_email_events'
        unique_together = (('emailid', 'recipient', 'type'),)


class HubspotEmailEventsCopy1(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=255)
    recipient = models.CharField(max_length=255)
    created = models.DateTimeField()
    emailid = models.IntegerField()
    eventid = models.CharField(max_length=255, blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    appname = models.CharField(db_column='appName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    attempt = models.CharField(max_length=255, blank=True, null=True)
    response = models.CharField(max_length=255, blank=True, null=True)
    linkid = models.CharField(db_column='linkId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    dropmessage = models.CharField(db_column='dropMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dropreason = models.CharField(db_column='dropReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    subscriptions = models.CharField(max_length=255, blank=True, null=True)
    portalsubscriptionstatus = models.CharField(db_column='portalSubscriptionStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sourceid = models.CharField(db_column='sourceId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    subject = models.CharField(max_length=255, blank=True, null=True)
    cc = models.CharField(max_length=255, blank=True, null=True)
    bcc = models.CharField(max_length=255, blank=True, null=True)
    replyto = models.CharField(db_column='replyTo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    from_field = models.CharField(db_column='from', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    suppressedmessage = models.CharField(db_column='suppressedMessage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suppressedreason = models.CharField(db_column='suppressedReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    devicetype = models.CharField(db_column='deviceType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useragent = models.CharField(db_column='userAgent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    browser_name = models.CharField(db_column='browser.name', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_family = models.CharField(db_column='browser.family', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_producer = models.CharField(db_column='browser.producer', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_producerurl = models.CharField(db_column='browser.producerUrl', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    browser_type = models.CharField(db_column='browser.type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    browser_url = models.CharField(db_column='browser.url', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sentby_created = models.DateTimeField(db_column='sentBy.created', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hubspot_email_events_copy1'


class HubspotEmailId(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    invoice_name = models.CharField(db_column='Invoice_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoice_id = models.CharField(db_column='Invoice_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hubspot_email_id'


class HubspotEmailStatistics(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    fromname = models.CharField(db_column='FromName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    replyto = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hubspot_email_statistics'


class HubspotNotesEmails(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    engagement_createdat = models.DateTimeField(db_column='engagement.createdAt', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    engagement_lastupdated = models.DateTimeField(db_column='engagement.lastUpdated', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    engagement_modifiedby = models.CharField(db_column='engagement.modifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    engagement_id = models.CharField(db_column='engagement.id', unique=True, max_length=255)  # Field renamed to remove unsuitable characters.
    engagement_type = models.CharField(db_column='engagement.type', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    engagement_bodypreview = models.TextField(db_column='engagement.bodyPreview', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    associations_contactids = models.CharField(db_column='associations.contactIds', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)
    rep_email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hubspot_notes_emails'


class HubspotPropertiesMapping(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    hs_list_name = models.CharField(db_column='hs_List_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datafile_field = models.CharField(db_column='Datafile_field', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hs_properties_field = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hubspot_properties_mapping'


class Invoices(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    farm_type = models.CharField(max_length=10)
    inv_number = models.CharField(max_length=15, blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    inv_due_date = models.DateField(blank=True, null=True)
    year_month = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plan = models.CharField(max_length=255)
    cap_rate = models.IntegerField(blank=True, null=True)
    cdg_kwh_applied = models.IntegerField(blank=True, null=True)
    cdg_credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plan_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit_applied = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payments_applied = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
    write_off = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=80)
    payment_status = models.CharField(max_length=80)
    payment_status_date = models.DateField(blank=True, null=True)
    paid_in_full_date = models.DateField(blank=True, null=True)
    statement_pmt_thru_date = models.DateField(blank=True, null=True, db_comment='Calculate previous Balance and Payments applied through this date.\n\nShould be set to the day before the merge is actually run.\n')
    autopay_date = models.DateField(blank=True, null=True)
    autopay_hold = models.IntegerField()
    autopay_note = models.CharField(max_length=255)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invoices'


class InvoicesBeforeautomation(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    farm_type = models.CharField(max_length=10)
    inv_number = models.CharField(max_length=15, blank=True, null=True)
    inv_date = models.DateField(blank=True, null=True)
    inv_due_date = models.DateField(blank=True, null=True)
    year_month = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plan = models.CharField(max_length=255)
    cap_rate = models.IntegerField(blank=True, null=True)
    cdg_kwh_applied = models.IntegerField(blank=True, null=True)
    cdg_credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plan_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit_applied = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payments_applied = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
    write_off = models.DecimalField(max_digits=10, decimal_places=2)
    balance_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=80)
    payment_status = models.CharField(max_length=80)
    payment_status_date = models.DateField(blank=True, null=True)
    paid_in_full_date = models.DateField(blank=True, null=True)
    statement_pmt_thru_date = models.DateField(blank=True, null=True, db_comment='Calculate previous Balance and Payments applied through this date.\n\nShould be set to the day before the merge is actually run.\n')
    autopay_date = models.DateField(blank=True, null=True)
    autopay_hold = models.IntegerField()
    autopay_note = models.CharField(max_length=255)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invoices_beforeautomation'


class MemberApiA(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    utility_account = models.CharField(max_length=80)
    farm_id = models.IntegerField(blank=True, null=True)
    processor = models.CharField(max_length=80)
    name_on_account = models.CharField(max_length=80)
    account_type = models.CharField(max_length=80)
    business_personal = models.CharField(db_column='Business_Personal', max_length=10)  # Field name made lowercase.
    bank_name = models.CharField(max_length=80)
    routing_number = models.TextField(blank=True, null=True)
    routing_last4 = models.CharField(max_length=80)
    account_number = models.TextField(blank=True, null=True)
    account_last4 = models.CharField(max_length=80)
    payment_status = models.CharField(max_length=80)
    status_details = models.CharField(max_length=80)
    stripe_cust_id = models.CharField(max_length=80)
    stripe_pmt_id = models.CharField(max_length=80)
    stripe_account_status = models.CharField(max_length=80)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'member_api_a'


class MemberApiS(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    processor = models.CharField(max_length=80)
    stripe_cust_id = models.CharField(max_length=80)
    stripe_card_id = models.CharField(max_length=80)
    stripe_connected_cust_id = models.CharField(max_length=80)
    stripe_connected_card_id = models.CharField(max_length=80)
    card_funding = models.CharField(max_length=80)
    card_brand = models.CharField(max_length=80)
    card_last4 = models.CharField(max_length=10)
    card_exp_year = models.SmallIntegerField(blank=True, null=True)
    card_exp_month = models.SmallIntegerField(blank=True, null=True)
    card_exp_year_month = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=80)
    status_details = models.CharField(max_length=80)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'member_api_s'


class Members(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    company = models.CharField(max_length=80)
    address_1 = models.CharField(max_length=80)
    address_2 = models.CharField(max_length=80)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    email_status = models.CharField(max_length=20)
    phone_1 = models.CharField(max_length=20)
    phone_1_type = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20)
    phone_2_type = models.CharField(max_length=20)
    same_for_all_accounts = models.IntegerField()
    paperless = models.IntegerField()
    communication_pref = models.CharField(max_length=20)
    user_id = models.IntegerField(blank=True, null=True)
    dg_customer = models.CharField(max_length=3, blank=True, null=True)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    uuid = models.CharField(max_length=80)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'members'


class MonthYearTrans(models.Model):
    month_allocation = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_allocationplusone = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_allocationplustwo = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_allocationminusone = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'month_year_trans'


class PaymentTransactions(models.Model):
    payment_id = models.IntegerField(blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    reason = models.CharField(max_length=80)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    ach_tran_id = models.CharField(db_column='ACH_tran_id', max_length=255)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_transactions'


class Payments(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=20)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    batch = models.CharField(max_length=80)
    payment_json = models.JSONField(blank=True, null=True)
    api = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=80)
    brand = models.CharField(max_length=20)
    last4 = models.CharField(max_length=10)
    check_number = models.CharField(max_length=10)
    reason = models.CharField(max_length=80)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments'


class Paymentstest(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)
    farm_id = models.IntegerField(blank=True, null=True)
    payment_method = models.CharField(max_length=20)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    batch = models.CharField(max_length=80)
    payment_json = models.JSONField(blank=True, null=True)
    api = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=80)
    brand = models.CharField(max_length=20)
    last4 = models.CharField(max_length=10)
    check_number = models.CharField(max_length=10)
    reason = models.CharField(max_length=80)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'paymentstest'


class ProspectIdMstr(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    prosp_id = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(db_column='Developer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    purchase_number = models.CharField(db_column='Purchase Number', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'prospect_id_MSTR'


class StatusTest(models.Model):
    accountnumber = models.IntegerField(blank=True, null=True)
    newlmi_status = models.CharField(db_column='newLMI_status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datechanged = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status_test'


class SuppressionList(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=80)
    reason = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    entered_by = models.CharField(max_length=80)
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'suppression_list'


class SyncarphaAccountContract(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    contact_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'syncarpha_account_contract'


class SyncarphaContactAccount(models.Model):
    msql_id = models.AutoField(db_column='MSQL_ID', primary_key=True)  # Field name made lowercase.
    contact_id = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    contract_id = models.IntegerField(blank=True, null=True)
    member_id = models.IntegerField(blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'syncarpha_contact_account'


class UsZips(models.Model):
    zip = models.CharField(primary_key=True, max_length=5)
    city_name = models.CharField(max_length=80, blank=True, null=True)
    state_code = models.CharField(max_length=2, blank=True, null=True)
    state_name = models.CharField(max_length=80, blank=True, null=True)
    county_name = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'us_zips'
