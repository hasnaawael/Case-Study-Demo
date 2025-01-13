# Case-Study-Demo

## Here’s the transformation that was applied to the data, summarized in points:

- Timestamp Format Change:

The timestamp field was transformed from the format YYYY-MM-DDTHH:MM:SS to YYYY-MM-DD HH:MM:SS by removing the "T" between the date and time.
- Customer ID to User ID:

The customer_id field was replaced with user_id in some records, ensuring consistency in the field naming convention.
- Addition of Missing user_id:

Where the customer_id was present but no user_id was available, a user_id was added to maintain uniformity across all records.
- Data Type Conversion:

The amount field, which was originally a string, is now represented as a numeric value (float) for better data processing.
These transformations ensure that the data is cleaned, consistent, and in a proper format for further analysis.
