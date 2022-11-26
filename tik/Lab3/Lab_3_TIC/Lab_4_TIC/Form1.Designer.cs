namespace Lab_4_TIC
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
            this.buttCode = new System.Windows.Forms.Button();
            this.buttSend = new System.Windows.Forms.Button();
            this.buttDecode = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.label1 = new System.Windows.Forms.Label();
            this.tbForCoding = new System.Windows.Forms.TextBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.label2 = new System.Windows.Forms.Label();
            this.tbForDecoding = new System.Windows.Forms.TextBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.tbForSending = new System.Windows.Forms.TextBox();
            this.groupBox4 = new System.Windows.Forms.GroupBox();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.tbForReceivingCode = new System.Windows.Forms.TextBox();
            this.buttSetVeroatnosti = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.labelInputEntropy = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.labelAvarageCountBitsPerSymbol = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.labelCloseCoef = new System.Windows.Forms.Label();
            this.dgvSDI = new System.Windows.Forms.DataGridView();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.groupBox4.SuspendLayout();
            this.groupBox5.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvSDI)).BeginInit();
            this.SuspendLayout();
            // 
            // buttCode
            // 
            this.buttCode.Location = new System.Drawing.Point(159, 585);
            this.buttCode.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.buttCode.Name = "buttCode";
            this.buttCode.Size = new System.Drawing.Size(172, 52);
            this.buttCode.TabIndex = 7;
            this.buttCode.Text = "Закодировать";
            this.buttCode.UseVisualStyleBackColor = true;
            this.buttCode.Click += new System.EventHandler(this.ButtCode_Click);
            // 
            // buttSend
            // 
            this.buttSend.Location = new System.Drawing.Point(376, 585);
            this.buttSend.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.buttSend.Name = "buttSend";
            this.buttSend.Size = new System.Drawing.Size(188, 52);
            this.buttSend.TabIndex = 8;
            this.buttSend.Text = "Передать";
            this.buttSend.UseVisualStyleBackColor = true;
            this.buttSend.Click += new System.EventHandler(this.ButtSend_Click);
            // 
            // buttDecode
            // 
            this.buttDecode.Location = new System.Drawing.Point(607, 585);
            this.buttDecode.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.buttDecode.Name = "buttDecode";
            this.buttDecode.Size = new System.Drawing.Size(172, 52);
            this.buttDecode.TabIndex = 9;
            this.buttDecode.Text = "Декодировать";
            this.buttDecode.UseVisualStyleBackColor = true;
            this.buttDecode.Click += new System.EventHandler(this.ButtDecode_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.tbForCoding);
            this.groupBox1.Font = new System.Drawing.Font("Segoe UI Emoji", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox1.Location = new System.Drawing.Point(1, 27);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox1.Size = new System.Drawing.Size(371, 271);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Устройство 1";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Segoe UI Emoji", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(8, 50);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(242, 27);
            this.label1.TabIndex = 1;
            this.label1.Text = "Текст для кодированния";
            // 
            // tbForCoding
            // 
            this.tbForCoding.Location = new System.Drawing.Point(8, 85);
            this.tbForCoding.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.tbForCoding.Multiline = true;
            this.tbForCoding.Name = "tbForCoding";
            this.tbForCoding.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tbForCoding.Size = new System.Drawing.Size(353, 170);
            this.tbForCoding.TabIndex = 0;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Controls.Add(this.tbForDecoding);
            this.groupBox2.Font = new System.Drawing.Font("Segoe UI Emoji", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox2.Location = new System.Drawing.Point(399, 27);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox2.Size = new System.Drawing.Size(360, 271);
            this.groupBox2.TabIndex = 3;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Устройство 2";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Segoe UI Emoji", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(8, 50);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(233, 27);
            this.label2.TabIndex = 1;
            this.label2.Text = "Декодированный текст";
            // 
            // tbForDecoding
            // 
            this.tbForDecoding.Location = new System.Drawing.Point(8, 85);
            this.tbForDecoding.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.tbForDecoding.Multiline = true;
            this.tbForDecoding.Name = "tbForDecoding";
            this.tbForDecoding.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tbForDecoding.Size = new System.Drawing.Size(343, 170);
            this.tbForDecoding.TabIndex = 0;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.tbForSending);
            this.groupBox3.Font = new System.Drawing.Font("Segoe UI Emoji", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox3.Location = new System.Drawing.Point(1, 305);
            this.groupBox3.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox3.Size = new System.Drawing.Size(371, 254);
            this.groupBox3.TabIndex = 5;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Код для передачи";
            // 
            // tbForSending
            // 
            this.tbForSending.Location = new System.Drawing.Point(8, 42);
            this.tbForSending.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.tbForSending.Multiline = true;
            this.tbForSending.Name = "tbForSending";
            this.tbForSending.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tbForSending.Size = new System.Drawing.Size(337, 204);
            this.tbForSending.TabIndex = 4;
            // 
            // groupBox4
            // 
            this.groupBox4.Controls.Add(this.groupBox5);
            this.groupBox4.Controls.Add(this.groupBox3);
            this.groupBox4.Controls.Add(this.groupBox2);
            this.groupBox4.Controls.Add(this.groupBox1);
            this.groupBox4.Location = new System.Drawing.Point(9, 10);
            this.groupBox4.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox4.Name = "groupBox4";
            this.groupBox4.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox4.Size = new System.Drawing.Size(777, 567);
            this.groupBox4.TabIndex = 6;
            this.groupBox4.TabStop = false;
            this.groupBox4.Text = "Структура системы для передачи закодированных сообщений";
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.tbForReceivingCode);
            this.groupBox5.Font = new System.Drawing.Font("Segoe UI Emoji", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox5.Location = new System.Drawing.Point(399, 306);
            this.groupBox5.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Padding = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.groupBox5.Size = new System.Drawing.Size(371, 254);
            this.groupBox5.TabIndex = 6;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "Полученный код";
            // 
            // tbForReceivingCode
            // 
            this.tbForReceivingCode.Location = new System.Drawing.Point(8, 42);
            this.tbForReceivingCode.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.tbForReceivingCode.Multiline = true;
            this.tbForReceivingCode.Name = "tbForReceivingCode";
            this.tbForReceivingCode.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tbForReceivingCode.Size = new System.Drawing.Size(337, 204);
            this.tbForReceivingCode.TabIndex = 4;
            // 
            // buttSetVeroatnosti
            // 
            this.buttSetVeroatnosti.Location = new System.Drawing.Point(16, 585);
            this.buttSetVeroatnosti.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.buttSetVeroatnosti.Name = "buttSetVeroatnosti";
            this.buttSetVeroatnosti.Size = new System.Drawing.Size(111, 52);
            this.buttSetVeroatnosti.TabIndex = 10;
            this.buttSetVeroatnosti.Text = "Задать вероятности";
            this.buttSetVeroatnosti.UseVisualStyleBackColor = true;
            this.buttSetVeroatnosti.Click += new System.EventHandler(this.ButtSetVeroatnosti_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Segoe UI Emoji", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(795, 37);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(227, 22);
            this.label3.TabIndex = 11;
            this.label3.Text = "Энтропия исходного ИДИ";
            // 
            // labelInputEntropy
            // 
            this.labelInputEntropy.AutoSize = true;
            this.labelInputEntropy.Font = new System.Drawing.Font("Segoe UI Emoji", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelInputEntropy.Location = new System.Drawing.Point(801, 74);
            this.labelInputEntropy.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelInputEntropy.Name = "labelInputEntropy";
            this.labelInputEntropy.Size = new System.Drawing.Size(0, 22);
            this.labelInputEntropy.TabIndex = 12;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Segoe UI Emoji", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(801, 137);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(231, 44);
            this.label4.TabIndex = 13;
            this.label4.Text = "Среднее число двоичных \r\nразрядов на символ";
            // 
            // labelAvarageCountBitsPerSymbol
            // 
            this.labelAvarageCountBitsPerSymbol.AutoSize = true;
            this.labelAvarageCountBitsPerSymbol.Font = new System.Drawing.Font("Segoe UI Emoji", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelAvarageCountBitsPerSymbol.Location = new System.Drawing.Point(801, 196);
            this.labelAvarageCountBitsPerSymbol.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelAvarageCountBitsPerSymbol.Name = "labelAvarageCountBitsPerSymbol";
            this.labelAvarageCountBitsPerSymbol.Size = new System.Drawing.Size(0, 22);
            this.labelAvarageCountBitsPerSymbol.TabIndex = 14;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Segoe UI Emoji", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.Location = new System.Drawing.Point(801, 230);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(166, 44);
            this.label5.TabIndex = 15;
            this.label5.Text = "Степень близости \r\n(lср - H(X)) / H(X)";
            // 
            // labelCloseCoef
            // 
            this.labelCloseCoef.AutoSize = true;
            this.labelCloseCoef.Font = new System.Drawing.Font("Segoe UI Emoji", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelCloseCoef.Location = new System.Drawing.Point(801, 279);
            this.labelCloseCoef.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelCloseCoef.Name = "labelCloseCoef";
            this.labelCloseCoef.Size = new System.Drawing.Size(0, 22);
            this.labelCloseCoef.TabIndex = 16;
            // 
            // dgvSDI
            // 
            this.dgvSDI.AllowUserToResizeRows = false;
            this.dgvSDI.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvSDI.Location = new System.Drawing.Point(805, 316);
            this.dgvSDI.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.dgvSDI.Name = "dgvSDI";
            this.dgvSDI.RowHeadersWidth = 51;
            this.dgvSDI.Size = new System.Drawing.Size(325, 321);
            this.dgvSDI.TabIndex = 17;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1143, 650);
            this.Controls.Add(this.dgvSDI);
            this.Controls.Add(this.labelCloseCoef);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.labelAvarageCountBitsPerSymbol);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.labelInputEntropy);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.buttSetVeroatnosti);
            this.Controls.Add(this.buttDecode);
            this.Controls.Add(this.buttSend);
            this.Controls.Add(this.buttCode);
            this.Controls.Add(this.groupBox4);
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.Name = "Form1";
            this.Text = "LabWork3";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.groupBox4.ResumeLayout(false);
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dgvSDI)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        public System.Windows.Forms.Button buttCode;
        public System.Windows.Forms.Button buttSend;
        public System.Windows.Forms.Button buttDecode;
        public System.Windows.Forms.GroupBox groupBox1;
        public System.Windows.Forms.Label label1;
        public System.Windows.Forms.TextBox tbForCoding;
        public System.Windows.Forms.GroupBox groupBox2;
        public System.Windows.Forms.Label label2;
        public System.Windows.Forms.TextBox tbForDecoding;
        public System.Windows.Forms.GroupBox groupBox3;
        public System.Windows.Forms.TextBox tbForSending;
        public System.Windows.Forms.GroupBox groupBox4;
        public System.Windows.Forms.GroupBox groupBox5;
        public System.Windows.Forms.TextBox tbForReceivingCode;
        public System.Windows.Forms.Button buttSetVeroatnosti;
        public System.Windows.Forms.Label label3;
        public System.Windows.Forms.Label labelInputEntropy;
        public System.Windows.Forms.Label label4;
        public System.Windows.Forms.Label labelAvarageCountBitsPerSymbol;
        public System.Windows.Forms.Label label5;
        public System.Windows.Forms.Label labelCloseCoef;
        private System.Windows.Forms.DataGridView dgvSDI;
    }
}

