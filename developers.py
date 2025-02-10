# Define the Developer class to represnt a software developer and thrir traits
class Developer:
    def __init__(self,name):
        # Initialize the attributes for the developer's traits
        self.name = name
        self.trait1 = None
        self.trait2 = None
        self.trait3 = None
        
    # Define a string representation of the Developer object
    def __str__(self):
        return f" Developers Traits \n\n Developer Name : {self.name} \n Trait 1 - Problem Solving : {self.trait1}\n Trait 2 - Team Player:{self.trait2}\n Trait 3 - Adaptability: {self.trait3} "
    

# Define the DeveloperBuilder class to implement the Builder pattern
class DeveloperBuilder:
    def __init__(self,name):
        # Initialize an empty Developer object when the builder is created
        self.developer = Developer(name)

    #Define the method for trait 1
    def trait1(self,level):
        self.developer.trait1 = level # Set the trait1 
        return self # Return the builder object for method chaining
    
    #Define the method for trait 1
    def trait2(self,level):
        self.developer.trait2 = level # Set the trait2
        return self 
    
    #Define the method for trait 1
    def trait3(self,level):
        self.developer.trait3 = level # Set the trait3
        return self 
    
    def build(self):
        return self.developer
    
# Main function to demonstrate the Builder Pattern
def main():
    
    print("\n****Building a Software Developer Profile****\n")

    # Create a DeveloperBuilder instance to begin the process
    builder = DeveloperBuilder('Sadhana')

    #Use the builder to set the traits of the developer step-by-step
    developer = builder.trait1("Excellence").trait2("Good").trait3("High").build()
    
    # Print the Developer object with all its traits
    print(developer)

    # Print the important steps involved in this program
    print(f"\nImportant Steps in the Program: 3")
    print("\n1. Define the Developer class with attributes.\n")
    print("2. Create a Builder class for step-by-step construction.\n")
    print("3. Use the Builder to assemble the Developer object.")
    print("4. Called by main function")

# Execute the main function if this script is run
if __name__ == "__main__":
    main()  # Call the main function to run the program