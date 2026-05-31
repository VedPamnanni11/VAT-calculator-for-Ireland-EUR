# VAT-calculator

This is a simple VAT calculator written in Python.  
You can use it to either **add VAT** to a price or **remove VAT** from a price.

## What it does

- Asks you for a price (as a decimal number).
- Asks you for the VAT rate you want to use (also as a decimal, e.g. `0.23` for 23%).
- Asks if you want to **add** VAT or **remove** VAT from the price.
- If you choose **add**:
  - It calculates the VAT amount.
  - It shows you the VAT and the total price (price + VAT).
- If you choose **remove**:
  - It calculates what the price was before VAT.
  - It shows you the VAT amount and the original price before VAT.

All money values are rounded to 2 decimal places.

## How to run

1. Make sure you have Python installed.
2. Save the file (for example) as `vat_calculator.py`.
3. Open a terminal in the folder where the file is saved.
4. Run:

   ```bash
   python vat_calculator.py
   ```

5. Follow the instructions:
   - Enter the price you want to add or remove VAT from (for example: `100`).
   - Enter the VAT rate in decimals (for example: `0.23` for 23%).
   - Type `add` to add VAT or `remove` to remove VAT.

## Example

- Price: `100`  
- VAT: `0.23`  
- Mode: `add`  

The program will show you the VAT amount and the total cost with VAT added.
