# in test_script.py
def hello_script(name): 
    """This function takes as a string as an input and prints a 2 line greeting."""
    print("Hello from the command line " + name + "!")
    print("It is a good day to script.")

if __name__ == "__main__":
    print("Executing as main program")
    print(hello_script("class"))
    print("Done Executing Script. Have a Nice Day")