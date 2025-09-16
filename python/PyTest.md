## 

## Class Based Test Cases

## Pytest fixtures

## Pytest mark

- pytest.mark.slow
- pytest.mark.xfail(reason="Reason why this will fail)
- pytest.mark.skip(reason="Reason this is skipped")

## Parametrized test cases
- Use the `@pytest.mark.parametrize()` decorator
```python
# file: tests/test_roku_api.py
import pytest
from roku.api import to_snake_case


TEST_SNAKE_CASE = [
    #(input_string, expected)
    ("test", "test"),
    ("testTest", "test_test"),
    ("testTEST", "test_test"),
    ("test2Test", "test2_test"),
    ("TestTest", "test_test"),
    ("test-test", "test_test"),
    ("Test-test", "test_test"),
    ("TestTest-test", "test_test_test"),
    ("test-test-test", "test_test_test"),
    ("test-test-test-test", "test_test_test_test")
    # Fails("Testtest-test", "test_test_test")
]


@pytest.mark.parametrize("input_string,expected", TEST_SNAKE_CASE)
def test_to_snake_case(input_string, expected):
    assert to_snake_case(input_string) == expected
``` 

## Mocking Requests
- https://github.com/getsentry/responses#basics

```python
# file: tests/test_response_record.py
import requests
from responses import _recorder

url = "http://192.168.1.117:8060"

def another():
    rsp = requests.get(url)
    rsp = requests.post(url + "/keypress/HOME")

@_recorder.record(file_path="out.yaml")
def test_recorder():
    another()

```

## Mock Patch

```python
import pytest
import source.service.get_user_from_db
import unittest.mock as mock

@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mocked Alice"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked Alice"
```

# Resources
- [FreeCodeCamp Pytest](https://www.youtube.com/watch?v=cHYq1MRoyI0)