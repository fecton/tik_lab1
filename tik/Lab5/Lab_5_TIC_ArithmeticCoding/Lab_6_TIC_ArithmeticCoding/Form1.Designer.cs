namespace Lab_6_TIC_ArithmeticCoding
{
    partial class Form1
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
            this.txtBoxInput = new System.Windows.Forms.TextBox();
            this.txtBoxFraction = new System.Windows.Forms.TextBox();
            this.btnEncode = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.txtBoxBinary = new System.Windows.Forms.TextBox();
            this.txtBoxStrPart = new System.Windows.Forms.TextBox();
            this.label4 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // txtBoxInput
            // 
            this.txtBoxInput.Location = new System.Drawing.Point(12, 36);
            this.txtBoxInput.Multiline = true;
            this.txtBoxInput.Name = "txtBoxInput";
            this.txtBoxInput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtBoxInput.Size = new System.Drawing.Size(202, 257);
            this.txtBoxInput.TabIndex = 0;
            // 
            // txtBoxFraction
            // 
            this.txtBoxFraction.Location = new System.Drawing.Point(410, 36);
            this.txtBoxFraction.Multiline = true;
            this.txtBoxFraction.Name = "txtBoxFraction";
            this.txtBoxFraction.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtBoxFraction.Size = new System.Drawing.Size(155, 61);
            this.txtBoxFraction.TabIndex = 1;
            // 
            // btnEncode
            // 
            this.btnEncode.Font = new System.Drawing.Font("Rockwell", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEncode.Location = new System.Drawing.Point(259, 91);
            this.btnEncode.Name = "btnEncode";
            this.btnEncode.Size = new System.Drawing.Size(100, 43);
            this.btnEncode.TabIndex = 2;
            this.btnEncode.Text = "Encode";
            this.btnEncode.UseVisualStyleBackColor = true;
            this.btnEncode.Click += new System.EventHandler(this.BtnEncode_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Rockwell", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(27, 9);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(79, 19);
            this.label1.TabIndex = 3;
            this.label1.Text = "Input text";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Rockwell", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(409, 9);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(69, 19);
            this.label2.TabIndex = 4;
            this.label2.Text = "Fraction";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Rockwell", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(255, 210);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(96, 19);
            this.label3.TabIndex = 6;
            this.label3.Text = "Binary code";
            // 
            // txtBoxBinary
            // 
            this.txtBoxBinary.Location = new System.Drawing.Point(259, 234);
            this.txtBoxBinary.Multiline = true;
            this.txtBoxBinary.Name = "txtBoxBinary";
            this.txtBoxBinary.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtBoxBinary.Size = new System.Drawing.Size(306, 60);
            this.txtBoxBinary.TabIndex = 5;
            // 
            // txtBoxStrPart
            // 
            this.txtBoxStrPart.Location = new System.Drawing.Point(410, 142);
            this.txtBoxStrPart.Multiline = true;
            this.txtBoxStrPart.Name = "txtBoxStrPart";
            this.txtBoxStrPart.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtBoxStrPart.Size = new System.Drawing.Size(155, 61);
            this.txtBoxStrPart.TabIndex = 7;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Rockwell", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(409, 115);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(88, 19);
            this.label4.TabIndex = 8;
            this.label4.Text = "String part";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(613, 302);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.txtBoxStrPart);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.txtBoxBinary);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnEncode);
            this.Controls.Add(this.txtBoxFraction);
            this.Controls.Add(this.txtBoxInput);
            this.Name = "Form1";
            this.Text = "Arithmetic compression";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtBoxInput;
        private System.Windows.Forms.TextBox txtBoxFraction;
        private System.Windows.Forms.Button btnEncode;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox txtBoxBinary;
        private System.Windows.Forms.TextBox txtBoxStrPart;
        private System.Windows.Forms.Label label4;
    }
}

