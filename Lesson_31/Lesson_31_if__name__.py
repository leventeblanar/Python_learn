# if __name__ == __main__: (this script can be imported OR run standalone)
#                          Functions and classes in this module can be reused 
#                          without the main block of code executing
# Good practice (code is modular, helps readability, leaves no global variables, avoid unintended execution)

# ex. library = Import library for functionality
#               When running library directly, display a help page


# to translate this to a simpler understanding
# sometimes we want to borrow sections of code from another python file but to eliminate the ones we don't want to, we can include them in the def main() so those do not get carried through into the other file

def main():
    # Your program goes here

    if __name__ == '__main__':
        main()
    else:
        pass