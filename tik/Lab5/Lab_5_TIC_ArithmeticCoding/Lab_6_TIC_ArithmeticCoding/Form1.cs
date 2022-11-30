using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab_6_TIC_ArithmeticCoding
{
    public partial class Form1 : Form
    {
        const int COUNT_SUMBOLS_PER_SUBSTRING = 5;
        public Form1()
        {
            InitializeComponent();
        }

        private void BtnEncode_Click(object sender, EventArgs e)
        {
            ArifmCode arthCode = new ArifmCode();
            List<Node> resNodes;
            string[] sliceInTextPer_5_Symb;
            txtBoxStrPart.Clear();
            txtBoxFraction.Clear();
            txtBoxBinary.Clear();

            arthCode.Build(txtBoxInput.Text);
            arthCode.GetSymbolsRanges(txtBoxInput.Text);
            sliceInTextPer_5_Symb = splitStrOn_N_Symbols(txtBoxInput.Text, COUNT_SUMBOLS_PER_SUBSTRING);
            foreach (string str in sliceInTextPer_5_Symb)
            {
                txtBoxStrPart.Text += str + "\r\n";
                decimal res = arthCode.Encode(str, out resNodes);
                txtBoxFraction.Text += (res.ToString() + "\r\n");
                txtBoxBinary.Text +=  Convert.ToString(GetFractionPart(res), 2) + "\r\n";
            }
        }
        
        private string[] splitStrOn_N_Symbols(string inputString, int sizeSubstr)
        {
            string[] splitedStrings = new string[(int)Math.Ceiling((double)inputString.Length / sizeSubstr)];
            if(inputString.Length < sizeSubstr)
            {
                splitedStrings[0] = inputString;
                return splitedStrings;
            }
            int i, j;
            for (i = 0, j = 0; i < inputString.Length;i+=sizeSubstr, j++)
            {
                splitedStrings[j] = inputString.Substring(i, Math.Min(sizeSubstr, inputString.Length-i));
            }
            return splitedStrings;
        }

        private int GetFractionPart(decimal number)
        {
            string fractionPartStr = (number - Math.Floor(number)).ToString();
            fractionPartStr = fractionPartStr.Split(',')[1];
            return int.Parse(fractionPartStr);
        }
    }
}
