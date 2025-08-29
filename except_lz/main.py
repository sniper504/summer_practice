from Dprocessing import Data_Proc 

def main():
    filename = "var1.csv"  
    processor = Data_Proc(filename)  
    processor.validate_file()  

if __name__ == "__main__":
    main() 
