# Mobile Shop Management System

A simple command-line application written in Python for managing a mobile phone shop's inventory. It supports adding, viewing, searching, updating, and deleting mobile records through an interactive menu.

## Features

- Add a new mobile with ID, brand, model, price, and quantity
- Prevent duplicate entries by checking for an existing mobile ID
- Display all mobiles in a tabular format
- Search for a mobile by its ID
- Update the details of an existing mobile
- Delete a mobile with a confirmation prompt
- Menu-driven interface that runs until the user chooses to exit

## Requirements

- Python 3.6 or higher
- No external libraries required

## Getting Started

1. Save the code in a file named `mobile_shop.py`.
2. Open a terminal in the folder containing the file.
3. Run the program:

```bash
python mobile_shop.py
```

## Usage

When the program starts, the following menu is displayed:

```
--- Mobile Shop ---
1. Add Mobile
2. Display Mobiles
3. Search Mobile
4. Update Mobile
5. Delete Mobile
6. Exit
```

Enter the number of the option you want and follow the prompts.

| Option | Description |
|--------|-------------|
| 1 | Add a new mobile. Rejects the entry if the ID already exists. |
| 2 | List all mobiles currently in inventory. |
| 3 | Look up a mobile by ID and show its full details. |
| 4 | Replace the brand, model, price, and quantity of an existing mobile. |
| 5 | Remove a mobile after confirming with `y`. |
| 6 | Exit the program. |

## Example Session

```
Enter your choice: 1
Enter mobile ID: 101
Enter brand: Samsung
Enter model: Galaxy S23
Enter price: 74999
Enter quantity: 10
Mobile added successfully.

Enter your choice: 2

ID      Brand           Model           Price   Quantity
101     Samsung         Galaxy S23      74999.0 10
```

## Data Structure

Each mobile is stored as a list inside the global `mobiles` list, in this order:

```
[mobile_id, brand, model, price, quantity]
```

## Project Structure

```
mobile_shop.py    # Main program containing all functions and the menu loop
README.md         # Project documentation
```

## Functions

- `add_mobile()` - Reads mobile details and appends a new record.
- `display_mobiles()` - Prints all records in a table-like layout.
- `search_mobile()` - Finds and prints a record by ID.
- `update_mobile()` - Overwrites the fields of an existing record.
- `delete_mobile()` - Removes a record after user confirmation.
- `main()` - Runs the menu loop and dispatches to the functions above.

## Limitations

- Data is stored in memory only and is lost when the program exits.
- Input is not validated for non-numeric values, so entering text where a number is expected will raise an error.
- Table alignment may vary with long brand or model names.

## Possible Improvements

- Persist data using a file (CSV or JSON) or a database such as SQLite
- Add input validation with `try`/`except` blocks
- Use dictionaries or a `Mobile` class instead of nested lists
- Add sorting and filtering by brand or price
- Add unit tests for each operation

## License

This project is free to use and modify for learning and personal purposes.