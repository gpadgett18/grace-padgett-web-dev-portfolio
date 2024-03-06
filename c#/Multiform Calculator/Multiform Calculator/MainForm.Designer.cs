namespace Multiform_Calculator
{
    partial class MainForm
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
            this.addSubtractButton = new System.Windows.Forms.Button();
            this.multiplyDivideButton = new System.Windows.Forms.Button();
            this.exitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // addSubtractButton
            // 
            this.addSubtractButton.Location = new System.Drawing.Point(39, 23);
            this.addSubtractButton.Name = "addSubtractButton";
            this.addSubtractButton.Size = new System.Drawing.Size(126, 32);
            this.addSubtractButton.TabIndex = 0;
            this.addSubtractButton.Text = "Add/Subtract";
            this.addSubtractButton.UseVisualStyleBackColor = true;
            this.addSubtractButton.Click += new System.EventHandler(this.addSubtractButton_Click);
            // 
            // multiplyDivideButton
            // 
            this.multiplyDivideButton.Location = new System.Drawing.Point(39, 74);
            this.multiplyDivideButton.Name = "multiplyDivideButton";
            this.multiplyDivideButton.Size = new System.Drawing.Size(126, 32);
            this.multiplyDivideButton.TabIndex = 1;
            this.multiplyDivideButton.Text = "Multiply/Divide";
            this.multiplyDivideButton.UseVisualStyleBackColor = true;
            this.multiplyDivideButton.Click += new System.EventHandler(this.multiplyDivideButton_Click);
            // 
            // exitButton
            // 
            this.exitButton.Location = new System.Drawing.Point(73, 126);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(62, 28);
            this.exitButton.TabIndex = 2;
            this.exitButton.Text = "Exit";
            this.exitButton.UseVisualStyleBackColor = true;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(204, 178);
            this.Controls.Add(this.exitButton);
            this.Controls.Add(this.multiplyDivideButton);
            this.Controls.Add(this.addSubtractButton);
            this.Name = "Form1";
            this.Text = "Calculator";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button addSubtractButton;
        private System.Windows.Forms.Button multiplyDivideButton;
        private System.Windows.Forms.Button exitButton;
    }
}

