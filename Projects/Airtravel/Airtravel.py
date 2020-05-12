'''
 __init__(): 
 1. Instance mehtod for initializing new objects
 2. It is an initializer not a constructor    
 3. self is similar to this in java,C# or  C++
 4. In python actual constructor is provided by python runtime system and checks if the instance initializer  is present or not

Class invariants
1. Truth about an object that endure for its lifetime

'''

class Flight:
    """A flight with a paticular passanger aircraft """

    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code in '{number}'")
        self._number = number
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError(f"Invalid rout number '{number}'")
        
        self._number =number
        self._aircraft = aircraft 
        rows,seats = self._aircraft.seating_plan()
        self._seating =[None]+ [{letter: None for letter in seats} for _ in rows]
    
    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]

    def allocate_seat(self,seat,passanger):
        
        row,letter = self._parse_seat(seat)


        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat{seat} already occupied")

        self._seating[row][letter]= passanger

    def _parse_seat(self,seat):
        rows,seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row{row_text}")

        if row not in rows:
            raise ValueError(f"Invalid seat row{row}")
        
        return row, letter 

    def relocate_passanger(self,from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"no pasanger to relocate in seat{from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat{to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] =None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
            for row in self._seating
            if row is not None)
    
    def make_boarding_cards(self,card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat,self.number(),self.aircraft_model())
    
    def _passenger_seats(self):
        row_numbers,seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter] 
                if passenger is not None:
                    yield (passenger,f"{row}{letter}")

# Applying polymorphism

class Aircraft:
     # Applying inheritance
    def __init__(self,registration):
            self._registration = registration
    
    def registration(self):
        return self._registration
    
    def num_seats(self):
        rows,rows_seats = self.seating_plan()
        return len(rows) * len(rows_seats)


# Similar to extends keyword in java here we use inheritance
class AirbusA319(Aircraft):
   
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23),"ABCDEF"
    
   

class Boeing777(Aircraft):

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return range(1,56),"ABCDEGHK"

    
        


def console_card_printer(passenger,seat,flight_number,aircraft):
    output =f"| Name: {passenger}" \
            f" Flight: {flight_number}"\
            f" Seat:{seat}"            \
            f" Aircraft: {aircraft} " \
            " |"
    banner = "+" + "-"*(len(output) -2)+"+"
    border = "+" + "-"*(len(output) -2)+"|"
    lines =[banner,border,output,border,banner]
    card ="\n".join(lines)
    print(card)
    print()


def make_flights():
    f = Flight("BA2432", AirbusA319("G-OIOE"))
    f.allocate_seat("20C", "Guido van rossum")
    f.allocate_seat("21C", "Franky rossum")
    f.allocate_seat("12D", "Brad  pitt") 
    f.allocate_seat("13D", "Jenifer  Aniston") 
    f.allocate_seat("21B", "Bjarne stroustrup")


    g= Flight("FE8784", Boeing777("D-ASFF" ))
    g.allocate_seat("33D", "Luffy")
    g.allocate_seat("12G", "Zoro")
    g.allocate_seat("14H", "Sanji") 
    g.allocate_seat("16K", "Ussop") 
    g.allocate_seat("21B", "Chopper")

    return f,g
    


# Print statements
'''
f = Flight()
print("f.number():",f.number())
print("Flight.number(f):",Flight.number(f))
from Airtravel import *


 a = Aircraft("G-EUPT","Airbus A319", num_rows =22, num_seats_per_row =6)

 f = Flight("BA2432", Aircraft("G-OIOE","Airbus B3434",num_rows=23, num_seats_per_row=7))


----
Final commands after modificaion to verify module in the REPL:

from Airtravel import *
f = make_flight()
f.num_available_seats()
6 * 22 - 5 

-------------------------------------------------
After addding boarding card in console

from Airtravel import *
f,g = make_flights()

f.aircraft_model()
g.aircraft_model()

f.num_available_seats()
g.num_available_seats()

For printing boarding cards: 
f.make_boarding_cards(console_card_printer)
g.make_boarding_cards(console_card_printer)

For getting seats
a = AirbusA319("G-OIOE")
b = Boeing777("D-ASFF")
a.num_seats()
b.num_seats()


'''
 