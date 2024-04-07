import pytest
from example_validation import validation_logic

def test_validate_salary_records():
    data = {
        "folder": {
            "datejoinedcomp": "2022-12-01",
            "salary": [
            {"datestarted": "2022-12-01"},
            {"datestarted": "2023-04-01"}
            ]
        },
        "inputs": {
            "current_date": "2024-03-31"
        }
    }

    expected_result = {
        "outputs": {
            "all_present": "true",
            "missing_years": []
        }
    }

    result = validation_logic.validate_salary_records(data)
    assert result == expected_result

def test_validate_missing_fields():
    data = {
        "folder": {
            "datejoinedcomp": "2022-12-01",
            "salary": [
            {"wrongfield": "2022-12-01"},
            ]
        },
        "inputs": {
            "current_date": "2024-03-31"
        }
    }

    expected_result = {'required': {
                            'folder': {
                                'datejoinedcomp': None, 
                                    'salary': [
                                        {'datestarted': None}
                                    ]
                             }, 
                            'inputs': {
                                'current_date': None}
                            }, 
                        'missing_keys': [
                            {'key': 'datestarted', 
                             'reason': 'missing'}]
                    }

    with pytest.raises(ValueError) as excinfo:
        validation_logic.validate_salary_records(data)

    assert excinfo.value.args[0] == expected_result
