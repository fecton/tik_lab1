using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections;

namespace HammingCode
{
    public partial class Form_table_3 : Form
    {
        public Form_table_3()
        {
            InitializeComponent();
            SetDGV();
        }

        public void SetDGV()
        {

            Dictionary<char, double> newDict = ConvertText.GetDictionaryForTable3(3);

            HuffmanTree hf = new HuffmanTree();
            Dictionary<char, double> tmpDict = hf.BuildNodes(ConvertText.table_3_Prob);

            Dictionary<char, BitArray> codes = hf.BuildHuffmanTree();
            ConvertText.table_3_Code = codes;

            dgv.RowCount = codes.Keys.Count;
            for (int i = 0; i < codes.Keys.Count; i++)
            {
                BitArray bt = codes.Values.ToArray()[i];
                foreach (object o in bt)
                {
                    if ((bool)o == true)
                    {
                        dgv[3, i].Value += '1'.ToString();
                    }
                    else
                    {
                        dgv[3, i].Value += '0'.ToString();
                    }
                }
                dgv[1, i].Value = "x" + i.ToString();
                dgv[2, i].Value = hf.Frequencies[codes.Keys.ToArray()[i]];
                dgv[4, i].Value = dgv[3, i].Value.ToString().Length;
            }

            dgv[0, 0].Value = "x1*x1";
            dgv[0, 1].Value = "x1*x2";
            dgv[0, 2].Value = "x2*x1";
            dgv[0, 3].Value = "x2*x2";
        }


    }
}
