/**
 * Grace Padgett
 * Quotient
 */
import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class Quotient 
{
    public static void main(String[] args) 
    {
        String message = "This program prompts for dividend and then for "
                + "divisor and returns the quotient.  \nInput can be whole "
                + "number or floating point. Quotient will have this format: "
                + "\nDividend / Divisor = Quotient. Example: 12 / 4 = 3.  "
                + "Press OK to continue. ";
        
        JOptionPane.showMessageDialog(null, message, "Quotient Program", 1);
        
        try
        {
            String response = JOptionPane.showInputDialog(null, 
                    "Enter dividend:  ");
            double number1 = Double.parseDouble(response);
            response = JOptionPane.showInputDialog(null, "Enter divisor:  ");
            double number2 = Double.parseDouble(response);
            
            if (number2 != 0)
            {
                double quotient = number1 / number2;
        
                DecimalFormat df = new DecimalFormat("###.##");
        
                String output = df.format(number1) + " / " 
                        + df.format(number2) + " = " + df.format(quotient);
        
                JOptionPane.showMessageDialog(null, output, 
                        "Quotient Program", 1);
            }
            else
            {
                JOptionPane.showMessageDialog(null, 
                        "You cannot divide by 0. Try again.");
            }
        }
        catch (NumberFormatException nfe)
        {
            JOptionPane.showMessageDialog(null, "You must enter numbers. "
                    + "Try again. ");
        }
        catch (Exception e)
        {
            JOptionPane.showMessageDialog(null, "An error has occurred. "
                    + "Try again. ");
        }
    } //end main method
} //end class
