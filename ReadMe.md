# Spell Variation Automation

## Instructions

1. **Place the CSV File**: Put your `variations.csv` file in the root directory.

   **CSV Required Headers**:

   - `variation1`
   - `variation2`
   - `meaning1`
   - `meaning2`

2. **Run the Script**: Execute the `extract.py` script to process the variations.

   ```bash
   python extract.py
   ```

## Example

Here is an example of how your `variations.csv` file should look:

```csv
variation1,variation2,meaning1,meaning2
color,colour,American spelling,British spelling
organize,organise,American spelling,British spelling
```

## Output

The script will generate an output based on the variations provided in the CSV file.
