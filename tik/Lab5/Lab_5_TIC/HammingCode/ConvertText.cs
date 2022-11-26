using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HammingCode
{
    class ConvertText
    {
        public static Dictionary<char, double> table_2_Prob = new Dictionary<char, double>(2);
        public static Dictionary<char, double> table_3_Prob = new Dictionary<char, double>(4);
        public static Dictionary<char, double> table_4_Prob = new Dictionary<char, double>(8);
        public static Dictionary<char, double> table_5_Prob = new Dictionary<char, double>(16);

        public static Dictionary<char, BitArray> table_2_Code = new Dictionary<char, BitArray>(2);
        public static Dictionary<char, BitArray> table_3_Code = new Dictionary<char, BitArray>(4);
        public static Dictionary<char, BitArray> table_4_Code = new Dictionary<char, BitArray>(8);
        public static Dictionary<char, BitArray> table_5_Code = new Dictionary<char, BitArray>(16);
        public Dictionary<char, double> GetProbabiltys(string text)
        {
            if (text.Length == 0) return null;
            Dictionary<char, double> charsProbab = new Dictionary<char, double>();
            foreach(char c in text)
            {
                if(!charsProbab.Keys.Contains(c))
                {
                    charsProbab[c] = text.Count(el => el == c) / text.Length;
                }
            }
            return charsProbab;
        }

        public static Dictionary<char, double> GetDictionaryForTable3(int numberOfForm)
        {
            int COUNT_VARS = 0;
            object numberTable = null;
            int middleTable = 0;
            switch (numberOfForm)
            {
                case 3:
                    {
                        numberTable = table_2_Prob;
                        COUNT_VARS = 4;
                        middleTable = 2;
                    }
                    break;
                case 4:
                    {
                        numberTable = table_3_Prob;
                        COUNT_VARS = 8;
                        middleTable = 4;
                    } break;
                case 5:
                    {
                        numberTable = table_4_Prob;
                        COUNT_VARS = 16;
                        middleTable = 8;
                    } break;

            }

            Dictionary<char, double> newDict = new Dictionary<char, double>(COUNT_VARS);
            newDict.Clear();
            for (int i = 0; i < COUNT_VARS; i++)
            {
                if (i < COUNT_VARS / 2)
                {
                    newDict[char.Parse(Convert.ToString(i, 16))] = ((Dictionary<char, double>)numberTable)[char.Parse((i % middleTable).ToString())] * table_2_Prob['0'];
                }
                else
                {
                    newDict[char.Parse(Convert.ToString(i, 16))] = ((Dictionary<char, double>)numberTable)[char.Parse((i % middleTable).ToString())] * table_2_Prob['1'];
                }
            }
            
            switch (numberOfForm)
            {
                case 3: table_3_Prob = newDict; break;
                case 4: table_4_Prob = newDict; break;
                case 5: table_5_Prob = newDict; break;
            }
            return newDict;
        }

        public static Dictionary<char, double> NormalizeIndex(Dictionary<char, double> oldDict)
        {
            Dictionary<char, double> newDict = new Dictionary<char, double>();
            newDict.Clear();
            for(int i=0; i< oldDict.Count; i++)
            {
                newDict.Add(char.Parse(i.ToString()), oldDict.Values.ToArray()[i]);
            }
            string tm = "NormalizeIndex";
            for (int i =0;  i < oldDict.Count; i++)
            {
                tm += "Key:" + oldDict.Keys.ToArray()[i].ToString() + "|Value:" + oldDict.Values.ToArray()[i].ToString()+"\n";
            }
            MessageBox.Show(tm);
            return newDict;
        }
   }
}
