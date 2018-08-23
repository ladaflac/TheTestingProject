import random
from airtable import Airtable


class AirtblAuth:
    """Access to Airtable API"""

    BASE_KEY = 'appSjN1YiEsy8uN6t'      # database name
    API_KEY = 'key1rAAlNih6BFL4r'       # not set as environment variable because of code sharing


class DbTables:
    """Airtable database tables"""

    ACC_TRSF_INPUT = 'ACC_TRSF_INPUT_DATA'
    ACC_TRSF_ORDERS = 'ACC_TRSF_ORDERS'


class GetDataFromDb:
    def get_input_data_random_record(self):
        all_records = Airtable(AirtblAuth.BASE_KEY, DbTables.ACC_TRSF_INPUT, AirtblAuth.API_KEY).get_all()
        random_record = random.choice(all_records)
        return random_record


class DataParser:
    def input_data_fields(self):
        record_dict = GetDataFromDb.get_input_data_random_record(self)
        fields_dict = record_dict['fields']
        return fields_dict

    def create_account_transfer(self, payment_data_to_save):
        # delete unnecessary data from source dict...
        del payment_data_to_save['ID']
        # ...and send the rest to the db
        payment_data_to_save_final = payment_data_to_save
        return payment_data_to_save_final


class SaveDataToDb:
    def create_new_payment(self, payment_data_to_save):
        payment_data_to_save_final = DataParser.create_account_transfer(self, payment_data_to_save)
        Airtable(AirtblAuth.BASE_KEY, DbTables.ACC_TRSF_ORDERS, AirtblAuth.API_KEY).insert(payment_data_to_save_final)
        # todo: handle the response from api
