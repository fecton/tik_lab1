using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab_4_TIC
{
    public partial class FormSetVeroatnosti : Form
    {
        Dictionary<char, double> forSetVeroatnosi;
        Form1 f1;
        public FormSetVeroatnosti(Form1 form1)
        {
            InitializeComponent();
            f1 = form1;
            dgvSet.ColumnCount = 2;
            dgvSet.RowCount = f1.SDI.Keys.Count();
            char[] arrOfKeys = f1.SDI.Keys.ToArray();
            for (int i = 0; i < dgvSet.RowCount; i++)
            {
                dgvSet[0, i].Value = arrOfKeys[i];
            }
            dgvSet.Columns[0].HeaderText = "Символ";
            dgvSet.Columns[1].HeaderText = "Вероятность";
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            forSetVeroatnosi = new Dictionary<char, double>(0);

            for(int i = 0; i< f1.SDI.Keys.Count; i++)
            {
                forSetVeroatnosi.Add(char.Parse( dgvSet[0, i].Value.ToString()), double.Parse(dgvSet[1, i].Value.ToString()));
            }
            f1.SDI = forSetVeroatnosi;
            this.Close();
        }
    }
}
