/*
 * Grace Padgett
 * Dog File in Dog Creator
 */
package dogcreator;

public class Dog 
{
    //define instance variables
    private String name = null;
    private double weight = 0;
    
    //dog constructor
    public Dog (String newName, double newWeight)
    {
        setName(newName);
        setWeight(newWeight);
    }
    
    //setter mehtod to set the animal name
    public final void setName(String newName)
    {
        this.name = newName;
    }
    
    //setter method to check validity of data and set dog weight
    public final void setWeight(double newWeight)
    {
        if (newWeight > 0)
        {
            this.weight = newWeight;  
        }
        else
        {
            System.out.println("Weight cannot be negative or 0.");
        }
    }
    
    //getter method to get the animal name
    public String getName()
    {
        return this.name;
    }
    
    //getter method ot get the dog weight
    public double getWeight()
    {
        return this.weight;
    }
    
    //method to compare weight of 2 dogs
    public String compare (Dog dogCompare)
    {
        String message = null;
        if (dogCompare.weight > this.weight)
        {
            message = dogCompare.name + " weighs more than " + this.name;
        }
        else if (dogCompare.weight < this.weight)
        {
            message = dogCompare.name + " weighs more than " + dogCompare.name;
        }
        else
        {
            message = this.name + " weighs equal to " + dogCompare.name;
        }
        return message;
    }
} //end class
