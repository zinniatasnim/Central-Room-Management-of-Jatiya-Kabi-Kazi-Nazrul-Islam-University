Central Room Management System --- JKKNIU
A Python-based, console-driven application designed to support
conference room management at Jatiya Kabi Kazi Nazrul Islam University
(JKKNIU). The project brings room information, booking, payment
handling, booking records, and customer satisfaction ratings together in
a simple menu-based interface. Originally developed as an academic
project, it can also serve as a learning resource for Python functions,
conditional logic, loops, lists, and basic record handling.
Features
- Room information: View details and amenities for Standard Non-AC
  and Standard AC rooms.
- Room booking: Enter customer name, phone number, registration
  number, booking date, and booking time.
- Room selection and pricing: Choose a room type and view the
  listed daily charge.
- Payment handling: Process a cash payment and print a booking
  bill.
- Booking records: Display stored booking details, including
  customer information, date, time, room type, and price.
- Customer ratings: Collect a satisfaction rating using a
  five-level menu.
- Menu-based navigation: Move between the main menu and the
  available features through console prompts.
Tech Stack
- Language: Python
- Interface: Console / command-line interface (CLI)
- Data handling: Python lists and in-memory data
- Standard-library modules: random and datetime (the code
  imports both)
Storage note: The current code stores booking information in
in-memory lists. Records are not saved to a database or file, so they
are lost when the program exits.

Requirements
- Python 3 installed
- A terminal or command prompt
Run the Project
1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run the Python file. If the file is named project code.py, use:
   python "project code.py"
   If you rename the file to main.py, run:
   python main.py
Project Structure
Central-Room-Management-System/
├── project code.py
└── README.md
The Python filename may differ depending on how you organize the
repository.
Usage
1. Run the program to open the main menu.
2. Select Conference Room's Info to review room types and
   amenities.
3. Select Booking and enter the requested customer and booking
   details.
4. Choose a room type:
   - Standard Non-AC: Tk. 3,500 per day
   - Standard AC: Tk. 4,000 per day
5. Select Payment and enter the phone number associated with the
   booking to access the cash-payment flow.
6. Select Room Ratings to submit a satisfaction rating when
   prompted.
7. Select Record to view booking details held during the current
   run.
8. Choose Exit to close the application.
Limitations
- Console-based interface; no graphical or web interface.
- Booking data is stored in memory and does not persist after the
  program closes.
- The payment flow supports cash as shown in the menu.
- The application uses basic input prompts and has limited input
  validation.
- The current implementation is a simple academic project, not a
  production booking platform.
Possible Future Improvements
- Save bookings to a file or database so records persist between runs.
- Improve input validation for dates, times, phone numbers, and menu
  choices.
- Add stronger checks for duplicate bookings and customer records.
- Generate clearer booking confirmations and payment receipts.
- Add room availability checks and prevent conflicting reservations.
- Improve the rating flow and store submitted ratings.
- Refactor the program into separate modules and add automated tests.
- Add a GUI or web interface if needed.
About
This project was developed for Jatiya Kabi Kazi Nazrul Islam
University (JKKNIU) as a simple way to explore console-based room
management using Python. It demonstrates how a menu-driven program can
organize basic booking, payment, record-display, and feedback workflows.
