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