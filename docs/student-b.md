# Student B contribution

Contributor: Daniel Haselock (`DanielHaselock`).
Development branch: `student-b/dictionary-operations`.

## Implemented examples

In `src/data_types/test_dictionaries.py`:

- `test_dictionary_update` demonstrates replacing an existing value and adding a
  new key with `update()`, while retaining an unrelated entry.
- `test_dictionary_get` demonstrates retrieving an existing value, the implicit
  `None` result for a missing key, and an explicit default. It verifies that
  retrieval does not insert the missing key or change existing entries.
- `test_dictionary_pop` demonstrates removing and returning an existing value,
  then using a default when attempting to remove the same key again.

## Local validation

Executed with Python 3.12.15 and pytest 8.4.2:

```text
python -m pytest src/data_types/test_dictionaries.py -v
4 passed

python -m flake8 src/data_types/test_dictionaries.py
No lint findings (flake8 7.3.0).

git diff --check
No whitespace errors.
```

The supplied requirements pin older tools intended for Python 3.6. Validation
used temporary local tools without changing the project's requirements.