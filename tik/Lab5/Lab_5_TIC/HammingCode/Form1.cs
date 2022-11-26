using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HammingCode
{
    public partial class Form1 : Form
    {
        static ConvertText ct;
        public Form1()
        {
            InitializeComponent();
            ct = new ConvertText();
            
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            Form_Table_2 form2 = new Form_Table_2(textBox1.Text);
            form2.ShowDialog();
            
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            Form_table_3 form3 = new Form_table_3();
            form3.ShowDialog();
        }

        private void Button3_Click(object sender, EventArgs e)
        {
            Form_Table_4 form4 = new Form_Table_4();
            form4.ShowDialog();
        }

        private void Button4_Click(object sender, EventArgs e)
        {
            Form_Table_5 form5 = new Form_Table_5();
            form5.ShowDialog();
        }

        private void Button5_Click(object sender, EventArgs e)
        {
            Form_Table_6 form6 = new Form_Table_6();
            form6.ShowDialog();
        }
    }


}
