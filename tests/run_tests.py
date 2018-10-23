import os
import pytest
try:
    from spt_keys import KEYS
except:
    from spt_keys_template import KEYS


def export_keys():
    for k, v in KEYS.items():
        if v:
            os.environ[k] = v
            print("export " + k + "=" + v)


def run():
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    access_token = os.getenv('SPOTIFY_ACCESS_TOKEN')
    redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')
    test_integration_sync = os.getenv('PYFY_TEST_INTEGRATION_SYNC')
    test_integration_async = os.getenv('PYFY_TEST_INTEGRATION_ASYNC')

    if client_id and client_secret and access_token and redirect_uri and test_integration_sync == 'true' and test_integration_async =='true':  # Run unit tests then integration tests
        print('Running unit tests followed by integration tests')
        pytest.main(['-v', '-s', '--cov', 'pyfy/', 'tests/test_units/', 'tests/test_integration/test_sync/', 'tests/test_integration/test_async/'])
    elif client_id and client_secret and access_token and redirect_uri and test_integration_sync == 'true' and test_integration_async !='true':  # Run unit tests then integration tests
        print('Running unit tests followed by synchronous integration tests')
        pytest.main(['-v', '-s', '--cov', 'pyfy/', 'tests/test_units/', 'tests/test_integration/test_sync/'])
    elif client_id and client_secret and access_token and redirect_uri and test_integration_sync != 'true' and test_integration_async =='true':  # Run unit tests then integration tests
        print('Running unit tests followed by asynchronous integration tests')
        pytest.main(['-v', '-s', '--cov', 'pyfy/', 'tests/test_units/', 'tests/test_integration/test_async/'])
    else:
        print('Running unit tests')
        pytest.main(['-v', '-s', '--cov', 'pyfy/', 'tests/test_units/'])


if __name__ == '__main__':
    export_keys()
    run()
