## Overview
This app was created as a result of an assessment test for _itemis_ company.
## Features
+ Parses string lines from command-line input
+ Calculates sales taxes and total price from parsed lines
+ Prints out a receipt details from input values
## Requirements
This app was implemented in [python3](https://www.python.org/), and it is run by command-line. Make sure [python3](https://www.python.org/) and [pip3](https://pypi.org/project/pip/) are installed 
on your system.
### Installation

    $ git clone https://github.com/eattar/Sales-Taxes.git
    $ cd Sales-Taxes/
    ~/Sales-Taxes$ pip3 install .

## Usage

    $ sales-taxes-cli
## Example


    $ sales-taxes-cli
    
    [q] SHOW RESULTS
    
    Add Item: 1 book at 12.49
    Added to basket!
    Add Item: 1 music CD at 14.99
    Added to basket!
    Add Item: 1 chocolate bar at 0.85
    Added to basket!
    Add Item: q

    1 book: 12.49
    1 music CD: 16.49
    1 chocolate bar: 0.85
    Sales Taxes: 1.50
    Total: 29.83
## Tests
This app runs tests using _[unittest](https://docs.python.org/3/library/unittest.html)_ framework. To run tests:

    $ cd Sales-Taxes/
    ~/Sales-Taxes$ python3 -m unittest
