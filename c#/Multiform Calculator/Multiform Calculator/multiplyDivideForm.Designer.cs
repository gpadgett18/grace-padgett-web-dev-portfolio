namespace Multiform_Calculator
{
    partial class multiplyDivideForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.firstNumberDescriptionLabel = new System.Windows.Forms.Label();
            this.firstNumberTextBox = new System.Windows.Forms.TextBox();
            this.secondNumberDescriptionLabel = new System.Windows.Forms.Label();
            this.secondNumberTextBox = new System.Windows.Forms.TextBox();
            this.multipleButton = new System.Windows.Forms.Button();
            this.divideButton = new System.Windows.Forms.Button();
            this.resultDescriptionLabel = new System.Windows.Forms.Label();
            this.resultLabel = new System.Windows.Forms.Label();
            this.resultDescriptiomLabel2 = new System.Windows.Forms.Label();
            this.closeButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // firstNumberDescriptionLabel
            // 
            this.firstNumberDescriptionLabel.AutoSize = true;
            this.firstNumberDescriptionLabel.Location = new System.Drawing.Point(75, 54);
            this.firstNumberDescriptionLabel.Name = "firstNumberDescriptionLabel";
            this.firstNumberDescriptionLabel.Size = new System.Drawing.Size(69, 13);
            this.firstNumberDescriptionLabel.TabIndex = 0;
            this.firstNumberDescriptionLabel.Text = "First Number:";
            // 
            // firstNumberTextBox
            // 
            this.firstNumberTextBox.Location = new System.Drawing.Point(62, 70);
            this.firstNumberTextBox.Name = "firstNumberTextBox";
            this.firstNumberTextBox.Size = new System.Drawing.Size(100, 20);
            this.firstNumberTextBox.TabIndex = 1;
            // 
            // secondNumberDescriptionLabel
            // 
            this.secondNumberDescriptionLabel.AutoSize = true;
            this.secondNumberDescriptionLabel.Location = new System.Drawing.Point(297, 54);
            this.secondNumberDescriptionLabel.Name = "secondNumberDescriptionLabel";
            this.secondNumberDescriptionLabel.Size = new System.Drawing.Size(87, 13);
            this.secondNumberDescriptionLabel.TabIndex = 2;
            this.secondNumberDescriptionLabel.Text = "Second Number:";
            // 
            // secondNumberTextBox
            // 
            this.secondNumberTextBox.Location = new System.Drawing.Point(288, 70);
            this.secondNumberTextBox.Name = "secondNumberTextBox";
            this.secondNumberTextBox.Size = new System.Drawing.Size(108, 20);
            this.secondNumberTextBox.TabIndex = 3;
            // 
            // multipleButton
            // 
            this.multipleButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F);
            this.multipleButton.Location = new System.Drawing.Point(197, 23);
            this.multipleButton.Name = "multipleButton";
            this.multipleButton.Size = new System.Drawing.Size(53, 45);
            this.multipleButton.TabIndex = 4;
            this.multipleButton.Text = "x";
            this.multipleButton.UseVisualStyleBackColor = true;
            this.multipleButton.Click += new System.EventHandler(this.multipleButton_Click);
            // 
            // divideButton
            // 
            this.divideButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F);
            this.divideButton.Location = new System.Drawing.Point(197, 82);
            this.divideButton.Name = "divideButton";
            this.divideButton.Size = new System.Drawing.Size(53, 49);
            this.divideButton.TabIndex = 5;
            this.divideButton.Text = "/";
            this.divideButton.UseVisualStyleBackColor = true;
            this.divideButton.Click += new System.EventHandler(this.divideButton_Click);
            // 
            // resultDescriptionLabel
            // 
            this.resultDescriptionLabel.AutoSize = true;
            this.resultDescriptionLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F);
            this.resultDescriptionLabel.Location = new System.Drawing.Point(419, 65);
            this.resultDescriptionLabel.Name = "resultDescriptionLabel";
            this.resultDescriptionLabel.Size = new System.Drawing.Size(24, 25);
            this.resultDescriptionLabel.TabIndex = 6;
            this.resultDescriptionLabel.Text = "=";
            // 
            // resultLabel
            // 
            this.resultLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.resultLabel.Location = new System.Drawing.Point(476, 70);
            this.resultLabel.Name = "resultLabel";
            this.resultLabel.Size = new System.Drawing.Size(100, 20);
            this.resultLabel.TabIndex = 7;
            // 
            // resultDescriptiomLabel2
            // 
            this.resultDescriptiomLabel2.AutoSize = true;
            this.resultDescriptiomLabel2.Location = new System.Drawing.Point(505, 54);
            this.resultDescriptiomLabel2.Name = "resultDescriptiomLabel2";
            this.resultDescriptiomLabel2.Size = new System.Drawing.Size(40, 13);
            this.resultDescriptiomLabel2.TabIndex = 8;
            this.resultDescriptiomLabel2.Text = "Result:";
            // 
            // closeButton
            // 
            this.closeButton.Location = new System.Drawing.Point(541, 125);
            this.closeButton.Name = "closeButton";
            this.closeButton.Size = new System.Drawing.Size(55, 23);
            this.closeButton.TabIndex = 9;
            this.closeButton.Text = "Close";
            this.closeButton.UseVisualStyleBackColor = true;
            this.closeButton.Click += new System.EventHandler(this.closeButton_Click);
            // 
            // multiplyDivideForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(608, 160);
            this.Controls.Add(this.closeButton);
            this.Controls.Add(this.resultDescriptiomLabel2);
            this.Controls.Add(this.resultLabel);
            this.Controls.Add(this.resultDescriptionLabel);
            this.Controls.Add(this.divideButton);
            this.Controls.Add(this.multipleButton);
            this.Controls.Add(this.secondNumberTextBox);
            this.Controls.Add(this.secondNumberDescriptionLabel);
            this.Controls.Add(this.firstNumberTextBox);
            this.Controls.Add(this.firstNumberDescriptionLabel);
            this.Name = "multiplyDivideForm";
            this.Text = "multiplyDivideForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label firstNumberDescriptionLabel;
        private System.Windows.Forms.TextBox firstNumberTextBox;
        private System.Windows.Forms.Label secondNumberDescriptionLabel;
        private System.Windows.Forms.TextBox secondNumberTextBox;
        private System.Windows.Forms.Button multipleButton;
        private System.Windows.Forms.Button divideButton;
        private System.Windows.Forms.Label resultDescriptionLabel;
        private System.Windows.Forms.Label resultLabel;
        private System.Windows.Forms.Label resultDescriptiomLabel2;
        private System.Windows.Forms.Button closeButton;
    }
}