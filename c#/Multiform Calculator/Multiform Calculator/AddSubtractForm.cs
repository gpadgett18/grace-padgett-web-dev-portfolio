using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Multiform_Calculator
{
    public partial class AddSubtractForm : Form
    {
        public AddSubtractForm()
        {
            InitializeComponent();
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            String first = firstNumberTextBox.Text;
            double firstNumber = double.Parse(first);

            String second = secondNumberTextBox.Text;
            double secondNumber = double.Parse(second);

            double result = firstNumber + secondNumber;

            resultLabel.Text = result.ToString();
        }
        private void subtractButton_Click(object sender, EventArgs e)
        {
            String first = firstNumberTextBox.Text;
            double firstNumber = double.Parse(first);

            String second = secondNumberTextBox.Text;
            double secondNumber = double.Parse(second);

            double result = firstNumber - secondNumber;

            resultLabel.Text = result.ToString();
        }

        private void closeButton_Click(object sender, EventArgs e)
        {
            //Close the form
            this.Close();
        }
    }
}
