namespace HammingCode
{
    partial class Form_Table_6
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
            this.dgv = new System.Windows.Forms.DataGridView();
            this.Column9 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column8 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column7 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column6 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column5 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column4 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column3 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.Column2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            ((System.ComponentModel.ISupportInitialize)(this.dgv)).BeginInit();
            this.SuspendLayout();
            // 
            // dgv
            // 
            this.dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dgv.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.Column2,
            this.Column3,
            this.Column4,
            this.Column5,
            this.Column6,
            this.Column7,
            this.Column8,
            this.Column9});
            this.dgv.Location = new System.Drawing.Point(-1, -1);
            this.dgv.Name = "dgv";
            this.dgv.Size = new System.Drawing.Size(578, 189);
            this.dgv.TabIndex = 2;
            // 
            // Column9
            // 
            this.Column9.HeaderText = "Избыточность кода";
            this.Column9.Name = "Column9";
            this.Column9.Width = 85;
            // 
            // Column8
            // 
            this.Column8.HeaderText = "n_minc/n_c(средня длина на символ)";
            this.Column8.Name = "Column8";
            this.Column8.Width = 80;
            // 
            // Column7
            // 
            this.Column7.HeaderText = "Средняя длина на символ, n_c";
            this.Column7.Name = "Column7";
            this.Column7.Width = 55;
            // 
            // Column6
            // 
            this.Column6.HeaderText = "Средняя длина кодового слова, n";
            this.Column6.Name = "Column6";
            this.Column6.Width = 60;
            // 
            // Column5
            // 
            this.Column5.HeaderText = "Избыточность источника";
            this.Column5.Name = "Column5";
            this.Column5.Width = 85;
            // 
            // Column4
            // 
            this.Column4.HeaderText = "n_minc";
            this.Column4.Name = "Column4";
            this.Column4.Width = 50;
            // 
            // Column3
            // 
            this.Column3.HeaderText = "Удельная энтропия источника, H1(S)";
            this.Column3.Name = "Column3";
            this.Column3.Width = 60;
            // 
            // Column2
            // 
            this.Column2.HeaderText = "Энтропия источника, H(S)";
            this.Column2.Name = "Column2";
            this.Column2.Width = 60;
            // 
            // Form_Table_6
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(579, 188);
            this.Controls.Add(this.dgv);
            this.Name = "Form_Table_6";
            this.Text = "Form_Table_6";
            ((System.ComponentModel.ISupportInitialize)(this.dgv)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.DataGridView dgv;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column2;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column3;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column4;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column5;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column6;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column7;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column8;
        private System.Windows.Forms.DataGridViewTextBoxColumn Column9;
    }
}