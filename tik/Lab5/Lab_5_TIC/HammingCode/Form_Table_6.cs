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
    public partial class Form_Table_6 : Form
    {
        const int COUNT_GROUPS = 4;
        public Form_Table_6()
        {
            InitializeComponent();
            SetDGV();
        }

        public void SetDGV()
        {
            dgv.RowCount = COUNT_GROUPS;
            SetGenerallyParams();
            SetParamsRow_1();
            SetParamsRow_2();
            SetParamsRow_3();
            SetParamsRow_4();
        }

        void SetGenerallyParams()
        {
            List<double[]> listProbab = new List<double[]> { ConvertText.table_2_Prob.Values.ToArray(),
            ConvertText.table_3_Prob.Values.ToArray(),
            ConvertText.table_4_Prob.Values.ToArray(),
            ConvertText.table_5_Prob.Values.ToArray() };
            dgv[0, 0].Value = (Math.Log(2, 2)).ToString();
            dgv[0, 1].Value = (Math.Log(4, 2)).ToString();
            dgv[0, 2].Value = (Math.Log(8, 2)).ToString();
            dgv[0, 3].Value = (Math.Log(16, 2)).ToString();
            for (int i = 0; i< COUNT_GROUPS; i++)
            {
                dgv[1, i].Value = (CalcEntropy(listProbab[i])).ToString();

            }
        }

        void SetParamsRow_1()
        {
            dgv[5, 0].Value = CalcAvarageLengthPerSymb(ConvertText.table_2_Prob, ConvertText.table_2_Code);
            dgv[4, 0].Value = CalcAvarageLenght(ConvertText.table_2_Code);
            dgv[3, 0].Value = 1 - (double.Parse(dgv[1, 0].Value.ToString()) / Math.Log(2, 2));
            double tmp = double.Parse(dgv[5, 0].Value.ToString());
            dgv[7, 0].Value = (tmp - double.Parse(dgv[1, 0].Value.ToString())) /tmp;
            dgv[2, 0].Value = ConvertText.table_2_Code.Values.ToArray().Min(k => k.Count);
            dgv[6, 0].Value = double.Parse(dgv[2, 0].Value.ToString()) / double.Parse(dgv[5, 0].Value.ToString());
        }
        void SetParamsRow_2()
        {
            dgv[5, 1].Value = CalcAvarageLengthPerSymb(ConvertText.table_3_Prob, ConvertText.table_3_Code);
            dgv[4, 1].Value = CalcAvarageLenght(ConvertText.table_3_Code);
            dgv[3, 1].Value = 1 - (double.Parse(dgv[1, 1].Value.ToString()) / Math.Log(4, 2));
            double tmp = double.Parse(dgv[5, 1].Value.ToString());
            dgv[7, 1].Value = (tmp - double.Parse(dgv[1, 1].Value.ToString())) / tmp;
            dgv[2, 1].Value = ConvertText.table_3_Code.Values.ToArray().Min(k => k.Count);
            dgv[6, 1].Value = double.Parse(dgv[2, 1].Value.ToString()) / double.Parse(dgv[5, 1].Value.ToString());
        }
        void SetParamsRow_3()
        {
            dgv[5, 2].Value = CalcAvarageLengthPerSymb(ConvertText.table_4_Prob, ConvertText.table_4_Code);
            dgv[4, 2].Value = CalcAvarageLenght(ConvertText.table_4_Code);
            dgv[3, 2].Value = 1 - (double.Parse(dgv[1, 2].Value.ToString()) / Math.Log(8, 2));
            double tmp = double.Parse(dgv[5, 2].Value.ToString());
            dgv[7, 2].Value = (tmp - double.Parse(dgv[1, 2].Value.ToString())) / tmp;
            dgv[2, 2].Value = ConvertText.table_4_Code.Values.ToArray().Min(k => k.Count);
            dgv[6, 2].Value = double.Parse(dgv[2, 2].Value.ToString()) / double.Parse(dgv[5, 2].Value.ToString());
        }
        void SetParamsRow_4()
        {
            dgv[5, 3].Value = CalcAvarageLengthPerSymb(ConvertText.table_5_Prob, ConvertText.table_5_Code);
            dgv[4, 3].Value = CalcAvarageLenght(ConvertText.table_5_Code);
            dgv[3, 3].Value = 1 - (double.Parse(dgv[1, 3].Value.ToString()) / Math.Log(16, 2));
            double tmp = double.Parse(dgv[5, 3].Value.ToString());
            dgv[7, 3].Value = (tmp - double.Parse(dgv[1, 3].Value.ToString())) / tmp;
            dgv[2, 3].Value = ConvertText.table_5_Code.Values.ToArray().Min(k => k.Count);
            dgv[6, 3].Value = double.Parse(dgv[2, 3].Value.ToString()) / double.Parse(dgv[5, 3].Value.ToString());
        }

        double CalcEntropy(double[] probabilities)
        {
            double entropy = 0;
            foreach(var a in probabilities)
            {
                entropy += a * Math.Log(a, 2);
            }
            return (0 - entropy);
        }

        double CalcAvarageLengthPerSymb (Dictionary<char, double> probab, Dictionary<char, BitArray> codes)
        {
            //string tmp = "CODES dictionary\n";
            //foreach(var o in codes)
            //{
            //    tmp += "key:" + o.Key + "|value:" + o.Value + "\n";
            //}
            //MessageBox.Show(tmp);
            double n_c = 0;
            foreach(var pair in probab)
            {
                //MessageBox.Show("pair.Value:" + pair.Value.ToString() + "|key:" + pair.Key + "\n");
                n_c += pair.Value * codes[pair.Key].Count;
            }
            return n_c;
        }

        double CalcAvarageLenght (Dictionary<char, BitArray> codes)
        {
            double n = 0;
            foreach(var pair in codes)
            {
                n += pair.Value.Count;
            }
            n /= (double)codes.Count;
            return n;
        }

    }
}
