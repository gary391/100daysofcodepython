################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Does Python have a Block Scope ? Like JAVA
# There is no Block scope in python - There is no block like structure in python like if, for, while

game_level = 3
# enemies = ["Alien", "Zombie", "Vampaire"]
# if game_level < 5:
#   new_enemy = enemies[0]
# print(new_enemy)

# Note the new_enemy is a variable that is created within the if block,
# I can access it outside the if block and is a valid code.

# In case I move this piece of code inside a function
# I can access the variable name_enemy from outside the function
def create_enemy():
  enemies = ["Alien", "Zombie", "Vampaire"]
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy)

print("outside:" +  new_enemy) # can't be accessed from outside the function

"""
Certainly! In Java, variables can have block-level scope. Here's an example in Java demonstrating block scope:

public class BlockScopeExample {
    public static void main(String[] args) {
        int x = 10;  // This variable has method-level scope
        
        if (x > 5) {
            int y = 20;  // This variable has block-level scope within the if statement
            System.out.println("Inside the if block:");
            System.out.println("x = " + x);  // Accessible here
            System.out.println("y = " + y);  // Accessible here
        }
        
        // Variable 'x' is still accessible here
        System.out.println("Outside the if block:");
        System.out.println("x = " + x);

        // Variable 'y' is not accessible here; it's out of scope
        // Uncommenting the line below would result in a compilation error:
        // System.out.println("y = " + y);
    }
}

In the Java example above:

Variable x is defined with method-level scope, so it's accessible throughout the main method.
Variable y is defined within the if block, and it has block-level scope. 
This means it's only accessible within the curly braces of the if statement. 
Outside of those braces, it's out of scope, and attempting to access it would result in a compilation error.
This demonstrates the concept of block scope in Java, where variables defined within a block (e.g., inside an if statement) are only accessible within that block and its nested blocks.






"""
