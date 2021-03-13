import os

import pytest

from nuvox_algorithm.utils.io_funcs import read_json_file


def example_payload(payload_number: int) -> dict:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    payload_path = os.path.join(current_dir, f'payloads/payload_{payload_number}.json')
    payload = read_json_file(payload_path)
    return payload


@pytest.mark.parametrize(
    'payload, expected_top_word, expected_action',
    [
        (
            example_payload(1),
            'Hello',
            'type'
        ),
        (
            example_payload(2),
            ' name',
            'type'
        ),
    ]
)
def test_predict_endpoint(app, client, payload, expected_top_word, expected_action):
    response = client.post('/api/predict/', json=payload)

    assert response.status_code == 200
    response_body = response.json()
    assert response_body['action'] == expected_action
    assert response_body['predicted_words'][0] == expected_top_word
