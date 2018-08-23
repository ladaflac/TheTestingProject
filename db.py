import random

from airtable import Airtable


class AirtblAuth:
    """Access to Airtable API"""

    BASE_KEY = 'appSjN1YiEsy8uN6t'      # database name
    API_KEY = 'key1rAAlNih6BFL4r'       # not set as environment variable because of code sharing


class DbTables:
    """Airtable database tables"""

    ACC_TRSF_INPUT = 'ACC_TRSF_INPUT_DATA'


class GetDataFromDb:
    def get_input_data_random_record(self):
        random_record = Airtable(AirtblAuth.BASE_KEY, DbTables.ACC_TRSF_INPUT, AirtblAuth.API_KEY).get_all()
        print(random_record)
        return random.choice(random_record)


class DataParser:
    def input_data_fields(self):
        record_dict = GetDataFromDb.get_input_data_random_record(self)
        fields_dict = record_dict['fields']
        return fields_dict
