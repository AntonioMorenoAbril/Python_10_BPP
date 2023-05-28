# Define function to read file
def read_file(file_name):
    try:
        file = open(file_name, "r")
        content = file.read()
        print("Content of the file:", content)
    
    except FileNotFoundError:
        print("Error: file not found")
    
    except IOError:
        print("Error: Some problem trying to read the file")
     
    except Exception as e:
        print(f"Error: Unexpected Error {e}")
    
    finally:
        # Check if the file has a value different to None
        if file:
            file.close()

file_name = "file.txt"
read_file(file_name)