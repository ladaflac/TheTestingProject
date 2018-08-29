from datetime import datetime
import testrail


class TestRailParams:
    project_id = '1'
    base_url = 'https://ladaflac.testrail.io/'

    def testrail_status(status):
        if status == 'passed':
            return {'status_id': 1}
        elif status == 'failed':
            return {'status_id': 5}
        elif status == 'skipped':
            return {'status_id': 6}


class AddRun:
    def get_run_id(self):
        method = 'add_run/'
        run_name = datetime.now().strftime('%Y%m%d%H%M%S')
        client = testrail.APIClient(TestRailParams.base_url)
        post = client.send_post(method + TestRailParams.project_id, {'name': run_name})
        run_id = post['id']
        return run_id


class AddResultForCase:
    def send_result(self, context, status, case_id):
        method = 'add_result_for_case/'
        status_id = TestRailParams.testrail_status(status)
        client = testrail.APIClient(TestRailParams.base_url)
        client.send_post(method + str(context.run_id) + '/' + case_id, status_id)
