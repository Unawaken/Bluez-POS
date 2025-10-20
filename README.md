# Bluez-POS
# Bluez Coffee Shop POS Console Application

Bluez is a simple, terminal/console-based application designed to process customer orders and calculate totals for a small coffee shop business. Built using **Python**, this script provides essential Point-of-Sale (POS) functionality directly within the command line.

---

## Features

* **Menu Display:** Shows a complete list of available coffee items and their prices (in ₱).
* **Order Processing:** Guides the user through selecting items and specifying quantities.
* **Inventory Management:** Checks stock levels of ingredients required for the order and deducts usage upon sale.
* **Total Calculation:** Automatically calculates the total price of the order.
* **Virtual Payment:** Processes payment and correctly calculates change, allowing for multiple payment attempts if insufficient funds are initially provided.
* **Receipt Generation:** Generates a final, formatted sales receipt summary.

---

## How to Run

### Prerequisites

You need **Python 3.x** installed on your system.

### Steps

1.  **Clone the repository** (or download the `Bluez.py` file).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where the file is saved.
4.  Execute the script using the following command:

    ```bash
    python Bluez.py
    ```

---

## Usage Example

The application will guide you through the process:

1.  **Check Inventory** (Displayed automatically at startup).
2.  **Select Coffee** (Enter the menu index, e.g., `1` for Caramel Macchiato).
3.  **Specify Quantity** (Enter a number, e.g., `2`).
4.  **Confirm Order** (Type `Y` or `yes`).
5.  **Enter Payment** (The application will prompt for the exact remaining amount if the first payment is insufficient).
6.  A **Receipt** will be printed upon successful payment.


<img width="332" height="348" alt="image" src="https://github.com/user-attachments/assets/fbca798f-0dfd-4ffa-9372-fdc2aa83061f" />
<img width="366" height="547" alt="image" src="https://github.com/user-attachments/assets/b5a840a2-5d9b-4ce6-bcc7-d21d547c3d6c" />
<img width="426" height="461" alt="image" src="https://github.com/user-attachments/assets/27891ec0-d3c3-4af6-bfb8-fab35d03cb98" />



