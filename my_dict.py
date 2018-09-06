#!/usr/bin/env python3

def main():
    """ This program displays the usage of dictionary.
    """
    my_dict = { 'Gaurav' : 123456,
                 'Rohit' : 345789,
                 'Sunny' : 657908,
                 'Tony'  : 789098,
                 'Sony'  : 876987 }
    print( f" { my_dict [ 'Tony' ] } " )
    print( f" { hash('Rohit') } " )

if __name__ == "__main__":
    main()
