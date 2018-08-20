from airtable import Airtable


class AirtblAuth:
    """Access to Airtable API"""

    BASE_KEY = 'appSjN1YiEsy8uN6t'      # database name
    API_KEY = 'key1rAAlNih6BFL4r'       # not set as environment variable because of code sharing


class DbTables:
    """Airtable database tables"""

    ACC_TRSF_INPUT = 'ACC_TRSF_INPUT_DATA'


class GetDataFromDb:
    def get_input_data_one_record(self):
        record = Airtable(AirtblAuth.BASE_KEY, DbTables.ACC_TRSF_INPUT, AirtblAuth.API_KEY).get_all(max_records=1)
        return record


class DataParser:
    def input_data_fields(self):
        record_list = GetDataFromDb.get_input_data_one_record(self)
        record_dict = record_list[0]
        fields_dict = record_dict['fields']
        return fields_dict
