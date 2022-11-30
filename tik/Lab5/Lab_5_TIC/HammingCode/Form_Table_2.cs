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
    public partial class Form_Table_2 : Form
    {
        public Form_Table_2(string text)
        {
            InitializeComponent();
            SetDGV(text);
        }

        public void SetDGV(string text)
        {
            if (text.Length == 0) return;
            HuffmanTree hf = new HuffmanTree();
            Dictionary<char, double> tmpDict =  hf.BuildNodes(text);
            ConvertText.table_2_Prob = tmpDict;
            ConvertText.table_2_Prob = ConvertText.NormalizeIndex(ConvertText.table_2_Prob);
            Dictionary<char, BitArray> codes = hf.BuildHuffmanTree();
            

            dgv.RowCount = codes.Keys.Count;
            for(int i =0; i < codes.Keys.Count; i++)
            {
                dgv[0, i].Value = codes.Keys.ToArray()[i];
                BitArray bt = codes.Values.ToArray()[i];
                foreach(object o in bt)
                {
                    if((bool)o == true)
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
            
            Dictionary<char, BitArray> newDict = new Dictionary<char, BitArray>();
            newDict.Clear();
            for (int i = 0; i < codes.Count; i++)
            {
                newDict.Add(char.Parse(i.ToString()), codes.Values.ToArray()[i]);
            }
            ConvertText.table_2_Code = newDict;
        }
    }
}
