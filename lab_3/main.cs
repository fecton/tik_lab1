namespace Lab_4_TIC
{
    public partial class Form1 : Form
    {
        public Dictionary<char, double> SDI;
        Dictionary<char, string> codingTable;
        char[] arrSortedKeys;
        double[] arrDefaultVer;

        double entropyInput;
        double avarageCountBitsPerSymbol;
        double closeCoef;
        bool needModef;
        public Form1()
        {
            InitializeComponent();
        }

        private void ButtCode_Click(object sender, EventArgs e)
        {
            InitializeFieldAfterInputText();
            CalculateVeroutnostiPoavleniy();
            GlobalScript();
            CodingText();
            SetDGVSDI();

        }

        void SetDGVSDI()
        {
            dgvSDI.ColumnCount = 2;
            dgvSDI.RowCount = SDI.Keys.Count();
            char[] arrOfKeys = SDI.Keys.ToArray();
            double[] arrOfValues = SDI.Values.ToArray();
            dgvSDI.Columns[0].HeaderText = "Символ";
            dgvSDI.Columns[1].HeaderText = "Вероятность";
            dgvSDI.Columns[0].Width = 25;
            for (int i = 0; i < dgvSDI.RowCount; i++)
            {
                if (needModef)
                {
                    dgvSDI[0, i].Value = "X" + arrOfKeys[i];
                }
                else
                {
                    dgvSDI[0, i].Value = arrOfKeys[i];
                }
                dgvSDI[1, i].Value = arrOfValues[i];
            }
        }

        void CodingText()
        {
            string res = "";
            for(int i = 0; i < tbForCoding.Text.Length; i++)
            {
                res += codingTable[tbForCoding.Text[i]];
            }
            tbForSending.Text = res;
        }

        void InitializeFieldAfterInputText()
        {
            SDI = new Dictionary<char, double>(tbForCoding.Text.Length);
            codingTable = new Dictionary<char, string>(SDI.Keys.Count);
            
            
        }

        void GlobalScript()
        {
            SortSDIAndCalcEntropy();
            if(needModef == false)
                arrDefaultVer = SDI.Values.ToArray();
            //   MessageBox.Show(DivideForHalfs(0, SDI.Count).ToString());
            arrSortedKeys = SDI.Keys.ToArray();
            ShenonFanoMainFunc(0, SDI.Keys.Count);
            //MessageBox.Show("After shenon fano");
            CalcAvarageCountBitsPerSymb();
            AnalizGettedCountAndInputEntropy();
        }

        void ShenonFanoMainFunc(int L, int R)
        {
            int half = DivideForHalfs(L, R);
        //    MessageBox.Show("half:" + half.ToString());
            
            
            for(int j = L; j < half; j++)
            {
                codingTable[arrSortedKeys[j]] += "1";
        //        MessageBox.Show("for 1:" + arrSortedKeys[j] + "=" + codingTable[arrSortedKeys[j]]);
            }

            for (int j = half; j < R; j++)
            {
                codingTable[arrSortedKeys[j]] += "0";
           //     MessageBox.Show("for 1:" + arrSortedKeys[j] + "=" + codingTable[arrSortedKeys[j]]);
            }

         //   MessageBox.Show("R - L = " + (R-L).ToString());
            if (half - L > 1)
            {
                ShenonFanoMainFunc(L, half);
            }
            if (R - half > 1)
            {
                ShenonFanoMainFunc(half, R);
            }
        }

        void AnalizGettedCountAndInputEntropy()
        {
            closeCoef = (avarageCountBitsPerSymbol - entropyInput) / entropyInput;
            labelCloseCoef.Text = closeCoef.ToString("G4");
            if(closeCoef > 0.15)
            {
                needModef = true;
                ModificateSDI();
                ChangeCodingTable();
                SetDGVSDI();
                GlobalScript();

            }
        }

        void ChangeCodingTable()
        {
            Dictionary<char, string> tmpTable = new Dictionary<char, string>(0);
            
            for (int i=0; i < SDI.Keys.Count;i++)
            {
                tmpTable.Add(char.Parse(i.ToString()), ""); 
            }

            codingTable = tmpTable;
        }


        void ModificateSDI()
        {
            Dictionary<char, double> tmpDict = new Dictionary<char, double>(SDI.Count * 2);
            double[] modArrVer = CalcModifiedVer();
            MessageBox.Show("length:" + modArrVer.Length.ToString());
            for (int i = 0; i < SDI.Count * 2; i++)
            {
                tmpDict[char.Parse(i.ToString())] = modArrVer[i];
            }
            SDI = tmpDict;
        }

        double[] CalcModifiedVer()
        {
            double[] arrNewVer = new double[SDI.Count * 2];
            double[] arrOfValues = SDI.Values.ToArray();

            for(int i =0; i < SDI.Count*2;i++)
            {
                arrNewVer[i] = arrOfValues[i % SDI.Keys.Count];
            }
            for (int i = 0; i <= 1; i++)
            { // Math.Ceiling(Math.Log(SDI.Keys.Count, 2))

                for (int j = 0; j < SDI.Count; j++)
                {
                    MessageBox.Show("arrOfValues" + i.ToString() + "||" + arrDefaultVer[i]);
                    arrNewVer[j + i * SDI.Count] *= arrDefaultVer[i];
                    MessageBox.Show("arrNewVer " + (j + i * SDI.Count).ToString() + "|" + arrNewVer[j + i * SDI.Count].ToString() + "/n\n");
                }
            }

            return arrNewVer;
        }

        void CalcAvarageCountBitsPerSymb()
        {
            avarageCountBitsPerSymbol = 0;
            foreach(var ch in codingTable.Keys)
            {
                avarageCountBitsPerSymbol += SDI[ch] * codingTable[ch].Length;
            }
            labelAvarageCountBitsPerSymbol.Text = avarageCountBitsPerSymbol.ToString("G4");
        }


        void CalculateVeroutnostiPoavleniy()
        {
            // calculate veroutnosti
            foreach (char el in tbForCoding.Text)
            {
                if (!SDI.Keys.Contains(el))
                {
                    SDI.Add(el, tbForCoding.Text.Count(charI => charI == el) / (double)tbForCoding.Text.Length);
                }

                if(!codingTable.Keys.Contains(el))
                {
                    codingTable.Add(el, "");
                }

            }
        }

        void SortSDIAndCalcEntropy()
        {
            // calculate entropy 
            entropyInput = 0;
            SDI = SDI.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
            foreach (var veroytnost in SDI.Values)
            {
                entropyInput += veroytnost * Math.Log(veroytnost, 2);
            }
            entropyInput = 0 - entropyInput;
            labelInputEntropy.Text = entropyInput.ToString("G4");
        }

        int DivideForHalfs(int L, int R)
        {
            double[] arrSDIValues = SDI.Values.ToArray();
            double halfValue = 0;
            int i = L;
            int m = i;

            for(int j =L; j< R;j++)
            {
                halfValue += arrSDIValues[j];
            }
            halfValue /= (double)2;
          //  MessageBox.Show(halfValue.ToString("G4"));
            double counterValue = 0;
            while ((counterValue + arrSDIValues[i] < halfValue) && (i < R))
            {
                counterValue += arrSDIValues[i];
                i++;
            }
            double deltaFromTopSide = Math.Abs(halfValue - counterValue);
         //   MessageBox.Show("Top" + deltaFromTopSide.ToString("G4"));
            double deltaFromBottomSide = Math.Abs((counterValue + arrSDIValues[i]) - halfValue);
          //  MessageBox.Show("bottom"+deltaFromBottomSide.ToString("G4"));
            if ((deltaFromTopSide > deltaFromBottomSide) &&(i<R))
            {
           //     MessageBox.Show("return i++");
                return (++i);
            }
            else
            {
             //   MessageBox.Show("return i");
                return i;
            }
        }

        private void ButtSetVeroatnosti_Click(object sender, EventArgs e)
        {
            InitializeFieldAfterInputText();
            CalculateVeroutnostiPoavleniy();
            FormSetVeroatnosti f2 = new FormSetVeroatnosti(this);
            f2.ShowDialog();
            GlobalScript();
            SetDGVSDI();
        }

        private void ButtSend_Click(object sender, EventArgs e)
        {
            tbForReceivingCode.Text = tbForSending.Text;
        }

        private void ButtDecode_Click(object sender, EventArgs e)
        {
            string decodedStr = "";
            int pointerEl = 0, i = 0;
            while (pointerEl < tbForReceivingCode.Text.Length)
            {
                for(int j =1; j < tbForReceivingCode.Text.Length; j++)
                {
                    i = IsExistCode(tbForReceivingCode.Text.Substring(pointerEl, j));
                    //MessageBox.Show("substr:" + tbForReceivingCode.Text.Substring(pointerEl, j) + "| i =" + i.ToString());
                    if ( i >= 0 )
                    {
                        decodedStr += codingTable.Keys.ToArray()[i];
                    //    MessageBox.Show("keys:" + codingTable.Keys.ToArray() );
                        pointerEl += j;
                        break;
                    }
                }
                //MessageBox.Show("decoded str:" + decodedStr);
            }

            tbForDecoding.Text = decodedStr;
        }

        int IsExistCode(string code)
        {
            string[] arrCodes = codingTable.Values.ToArray();
            for(int i =0; i < codingTable.Values.Count; i++)
            {
                if(arrCodes[i] == code)
                {
                    return i;
                }
            }
            return -1;
        }

        private void groupBox5_Enter(object sender, EventArgs e)
        {

        }

        private void tbForCoding_TextChanged(object sender, EventArgs e)
        {

        }
    }

}