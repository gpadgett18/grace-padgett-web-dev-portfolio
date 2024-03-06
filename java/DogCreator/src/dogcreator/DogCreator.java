/*
 * Grace Padgett
 * Dog Creator
 */

package dogcreator;

public class DogCreator 
{
    
    public static void main(String[] args) 
    {
        //create dogs
        Dog dog1 = new Dog("Textie", 25);
        Dog dog2 = new Dog("Juicy", 15);
        Dog dog3 = new Dog("Penny", 28);
        
        //print out dog names and weight
        System.out.println("Name: " + dog1.getName());
        System.out.println("Weight: " + dog1.getWeight() + "lbs.");
        System.out.println("Name: " + dog2.getName());
        System.out.println("Weight: " + dog2.getWeight() + "lbs.");
        System.out.println("Name: " + dog3.getName());
        System.out.println("Weight: " + dog3.getWeight() + "lbs.");
        System.out.println("\n");
        
        //comparisons
        System.out.println(dog1.compare(dog2));
        System.out.println(dog1.compare(dog3));
        System.out.println(dog2.compare(dog3));
        System.out.println("\n");
        
        //dog1 gains weight
        dog1.setWeight(28);
        System.out.println("Name: " + dog1.getName());
        System.out.println("Weight: " + dog1.getWeight() + "lbs.");
        System.out.println(dog1.compare(dog3));
        
    } //end main
} //end class
