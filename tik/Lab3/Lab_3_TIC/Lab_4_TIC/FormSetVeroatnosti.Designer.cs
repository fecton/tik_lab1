namespace Lab_4_TIC
{
    partial class FormSetVeroatnosti
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
            this.dgvSet = new System.Windows.Forms.DataGridView();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dgvSet)).BeginInit();
            this.SuspendLayout();
            // 
            // dgvSet
            // 
            this.dgvSet.AllowUserToAddRows = false;
            this.dgvSet.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgvSet.Location = new System.Drawing.Point(-1, 0);
            this.dgvSet.Name = "dgvSet";
            this.dgvSet.Size = new System.Drawing.Size(240, 265);
            this.dgvSet.TabIndex = 0;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(-1, 271);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(240, 36);
            this.button1.TabIndex = 1;
            this.button1.Text = "Подтвердить ";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.Button1_Click);
            // 
            // FormSetVeroatnosti
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(239, 306);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.dgvSet);
            this.Name = "FormSetVeroatnosti";
            this.Text = "FormSetVeroatnosti";
            ((System.ComponentModel.ISupportInitialize)(this.dgvSet)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView dgvSet;
        private System.Windows.Forms.Button button1;
    }
}