# Central Room Management of Jatiya Kabi Kazi Nazrul Islam University

A console-based conference room management system written in Python. It started as a first-year academic project and has been refined to be modular, readable, and reliable. The system manages room booking, payment, billing, customer ratings, and booking records through a simple menu-driven console interface, making it a great resource for learning, practice, and everyday file-free data handling in Python.

## Features

- Conference room information (amenities of Standard Non-AC and Standard AC rooms)
- Room booking with name, phone number, registration number, booking date, and time
- Input validation: name, phone number, and registration number cannot be blank
- Two room types with fixed pricing (Standard Non-AC and Standard AC)
- Automatic random Customer ID generation (unique per booking)
- Payment processing with a formatted bill/receipt
- Duplicate-payment check (already paid bookings are flagged)
- Customer satisfaction rating (5-level scale)
- Booking record table showing all bookings
- Menu navigation with a back option on every screen

## Tech Stack

- Language: Python 3
- Libraries: `random`, `datetime` (standard library only)
- Platform: Any OS with a terminal (Windows, Linux, macOS)
- Storage: In-memory lists (data resets when the program exits)

## Installation

### Prerequisites

- Python 3.x installed

### Clone and run

```bash
git clone https://github.com/<your-username>/Central-Room-Management-System.git
cd Central-Room-Management-System
python "project code.py"
```

## Project Structure

```text
Central-Room-Management-System/
|-- project code.py   # Main program (all functions and driver code)
|-- README.md
```

## Usage

1. Run the program.
2. Choose an option from the main menu.
3. Use **Conference Room's Info** to view room amenities.
4. Use **Booking** to reserve a room and receive a Customer ID.
5. Use **Payment** with the booking phone number to pay and print the bill.
6. Use **Room ratings** to rate your experience with your Customer ID.
7. Use **Record** to view all bookings.

Room prices:

- Standard Non-AC: Tk. 3500 for 1 day
- Standard AC: Tk. 4000 for 1 day

## Demo

The examples below mirror the program's printed output. Exact values depend on the data you enter.

### Main Menu

```text
						 Welcome to JKKNIU CENTRAL ROOM

			 1 Conference Room's Info

			 2 Booking

			 3 Payment

			 4 Room ratings

			 5 Record

			 0 Exit

Enter your choice:
```

### Booking

```text
 BOOKING ROOMS

Name: Rahim
Phone No: 01700000000
Registration No: 12345
Booking Date: 20-10-2026
Booking Time: 10:00 AM
------SELECT ROOM TYPE------
 1. Standard Non-AC
 2. Standard AC
		Press 0 for Room Prices
Enter your choice: 2
Room Type- Standard AC
Price- 4000

			 **Room Booked Successfully**

Customer Id - 27
```

### Payment (Bill)

```text
Payment
-------------------------------
Mode of Payment
 1- Cash
Enter your choice->1

 Amount:  4000

      Pay for JKKNIU
(y/n)
->y

----------------------------
         JKKNIU
--------------------------------
            Bill
--------------------------------
Name: Rahim
 Phone No: 01700000000
 Registration no: 12345

Booking Date: 20-10-2026
 Booking Time: 10:00 AM

Room Type: Standard AC
 Room Charges: 4000
--------------------------------
 Total Amount:  4000
--------------------------------
             Thank You!!
             Visit Again!!!
------------------------------------
```

### Room Ratings

```text
Customer Id: 27

 Ratings
 1 Very satisfied
 2 Somewhat satisfied
 3 Neither satisfied nor unsatisfied
 4 Somewhat unsatisfied
 5 Very unsatisfied
 Press  0 to exit
Enter your choice-> 1
Thanks for your ratings!
```

### Booking Record

```text
     *Booking Record*

|Name   |Phone No     |Registration No |Booking Date |Booking Time |Room Type    |Price
-----------------------------------------------------------------------------------------
| Rahim | 01700000000 | 12345          | 20-10-2026  | 10:00 AM    | Standard AC | 4000
-----------------------------------------------------------------------------------------
```

## Limitations

- Data is stored in memory only and is lost when the program closes.
- Booking does not check for date/time conflicts between customers.
- The rating function does not save the submitted rating.

## Possible Future Improvements

- Save bookings to a file or database
- Add date/time conflict checking
- Store and summarize customer ratings
- Add admin login

## License

This project is for educational purposes.
