# Driver Search Algorithms

A small Python project that compares ways to find drivers in a JSON dataset. It demonstrates linear search, binary search, and hash map lookup, including searches that match both a driver's name and ID.

## Project files

- `driver.py` — loads the driver data, prepares available drivers, performs the searches, and prints the elapsed time for repeated lookups.
- `drivers.json` — sample driver records. Each record has an `id`, `name`, `vehicle`, and `available` field.

## Requirements

- Python 3
- No third-party packages are required.

## Run

From the project directory, run:

```bash
python driver.py
```

The script reads `drivers.json` from the current working directory and prints timing results for each search method. To use a different driver, update the target ID and name/ID values near the bottom of `driver.py`.

## Search methods

| Method | Preparation | Lookup complexity |
| --- | --- | --- |
| Linear search | None | O(n) |
| Binary search | Sort drivers by ID or name | O(log n) to locate a key; duplicate names may require checking adjacent matches |
| Hash map | Build a dictionary | O(1) average lookup; name matches are then checked for the requested ID |

The script filters to available drivers before building the sorted list and hash maps. Timing results depend on the machine and dataset size; the script is an educational comparison rather than a benchmark suite.
