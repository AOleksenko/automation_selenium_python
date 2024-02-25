from support.api_setup import ApiSetUp
from support.db_executor import DatabaseExecutor


# Get access token
access_token = ApiSetUp.get_access_token()


class TestData(ApiSetUp, DatabaseExecutor):

    @staticmethod
    def create_test_element_via_db():
        DatabaseExecutor.execute_query(
            "Insert Into [test_table]"
            "(externalId, name, type)"
            "values ('test_id', 'test_name', 'test_type')"
        )

    @staticmethod
    def create_test_group_and_item_data():
        test_group = [
            {
                "groupType": "test_type",
                "name": "test_group_name",
                "externalId": "test_group_id",
            }
        ]

        test_item = [
            {
                "groupId": "test_group_id",
                "name": "test_item_name_1",
                "externalId": "test_item_id_1"
            },
            {
                "groupId": "test_group_id",
                "name": "test_item_name_2",
                "externalId": "test_item_id_2"
            }
        ]

        if access_token:
            # Send POST request with different payloads
            ApiSetUp.send_post_request("ConfiguredGroups", access_token, test_group)
            ApiSetUp.send_post_request("ConfiguredItems", access_token, test_item)

    @staticmethod
    def delete_test_group_data():
        if access_token:
            # Send DELETE request with different ids
            ApiSetUp.send_delete_request("ConfiguredGroups/test_group_id", access_token)