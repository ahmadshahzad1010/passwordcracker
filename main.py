# Import the PyPDF2 library
import PyPDF2 

def unlock_pdf(pdf_path):
    # Generate all possible 4-digit PINs
    for pin in range(120000,129999):
        pin_str = str(pin).zfill(4)  # Assign a variable to store the PIN and Convert PIN to a 4-digit string

        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)  # Initialize PDF reader 

                # Check if the PDF is encrypted
                if reader.is_encrypted: 
                    # Try to decrypt with the current PIN
                    if reader.decrypt(pin_str):  
                        # Try reading the first page to ensure decryption worked
                        try:
                            reader.pages[0]  # Attempt to read the first page 
                            print("That is correct, the password was:", pin_str)
                               
                            return pin_str
                        except:
                           continue


                    else:
                        print("Incorrect pin:", pin_str)


                    

        except Exception as e:  
            # Print any errors that occur
            print(f"An error occurred: {e}")  

    # Print if all attempts fail and return None


    print("failed to unlock PDF with all possible PINs!")
    return None

if __name__ == "__main__":  # Fill in the blanks
    pdf_path = "Locked.pdf"  # Path to the locked PDF (Fill in the blank)
    unlock_pdf(pdf_path)  # Call the unlock function with the given path