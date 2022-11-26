using System;
using System.Collections;
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
    public partial class Form_Table_5 : Form
    {
        public Form_Table_5()
        {
            InitializeComponent();
            SetDGV();
        }

        public void SetDGV()
        {
            Dictionary<char, double> newDict = ConvertText.GetDictionaryForTable3(5);

            HuffmanTree hf = new HuffmanTree();
            Dictionary<char, double> tmpDict = hf.BuildNodes(ConvertText.table_5_Prob);

            Dictionary<char, BitArray> codes = hf.BuildHuffmanTree();
            ConvertText.table_5_Code = codes;

            dgv.RowCount = codes.Keys.Count;
            List<Node> orderedNodes = hf.nodes.OrderBy(node => node.AddName).ToList<Node>();
            int i = 0;
            foreach (var o in hf.Frequencies)
            {
                dgv[1, i].Value = "x" + i.ToString();
                dgv[2, i].Value = o.Value.ToString();
                foreach (var q in codes[o.Key])
                {
                    if ((bool)q == true)
                    {
                        dgv[3, i].Value += '1'.ToString();
                    }
                    else
                    {
                        dgv[3, i].Value += '0'.ToString();
                    }
                }
                dgv[4, i].Value = dgv[3, i].Value.ToString().Length;
                i++;
            }

            dgv[0, 0].Value = "x1*x1*x1*x1";
            dgv[0, 1].Value = "x1*x1*x1*x2";
            dgv[0, 2].Value = "x1*x1*x2*x1";
            dgv[0, 3].Value = "x1*x1*x2*x2";
            dgv[0, 4].Value = "x1*x2*x1*x1";
            dgv[0, 5].Value = "x1*x2*x1*x2";
            dgv[0, 6].Value = "x1*x2*x2*x1";
            dgv[0, 7].Value = "x1*x2*x2*x2";
            dgv[0, 8].Value = "x2*x1*x1*x1";
            dgv[0, 9].Value = "x2*x1*x1*x2";
            dgv[0, 10].Value = "x2*x1*x2*x1";
            dgv[0, 11].Value = "x2*x1*x2*x2";
            dgv[0, 12].Value = "x2*x2*x1*x1";
            dgv[0, 13].Value = "x2*x2*x1*x2";
            dgv[0, 14].Value = "x2*x2*x2*x1";
            dgv[0, 15].Value = "x2*x2*x2*x2";
        }

    }
}
