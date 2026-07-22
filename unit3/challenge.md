The Challenge: “The South African Fuel Cost Calculator”
With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:

1. Ask the user how many kilometers they want to drive.

2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).

3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
   (Formula: liters_needed = kilometers / 10).

4. Calculate the total cost (liters_needed \* petrol_price).

5. Use type casting to ensure your numbers work, and use round() to format the
   final cost to 2 decimal places.
