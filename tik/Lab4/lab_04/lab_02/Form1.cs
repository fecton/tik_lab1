using System;
using System.Windows.Forms;

namespace lab_02
{
    public partial class Form1 : Form
    {
        private readonly int NUM = 11;
        private readonly Random r;
        readonly double[] Per = new double[11];
        public Form1()
        {
            InitializeComponent();
            r = new Random();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridView1.RowCount = dataGridView1.ColumnCount = NUM + 1;
            for (int i = 0; i < NUM; i++)
            {
                dataGridView1.Columns[i].HeaderText = (i + 1).ToString();
                dataGridView1.Rows[i].HeaderCell.Value = (i + 1).ToString();
                dataGridView1.Columns[i].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            }

            dataGridView1.Columns[NUM].HeaderText = "p(x)";

            for (int i = 0; i < NUM; i++)
            {
                Per[i] = Math.Round(r.NextDouble(), 3);
                for (int j = 0; j < NUM; j++)
                {
                    dataGridView1.Rows[i].Cells[j].Value = 
                        (Fact(NUM - 1) / (Fact(j) * Fact(NUM - 1 - j))) 
                        * Math.Pow(Per[i], j) * Math.Pow(1 - Per[i], NUM - 1 - j);
                }
                dataGridView1.Rows[i].Cells[NUM].Value = Per[i].ToString();
            }
        }

        private int Fact(int n)
        {
            if (n <= 1) return 1;
            return n * Fact(n - 1);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            double []pX = new double[NUM];
            double []pY = new double[NUM];
            double D = NUM - 1; // Потери в канале связи при алфавите размером 11
            double HX = 0; // H(A)
            double HY = 0; // H(B)
            for (int i = 0; i < NUM; i++)
            {
                double PBj = 0.0;
                for (int j = 0; j < NUM; j++)
                {
                    var data1 = dataGridView1.Rows[i].Cells[j].Value;
                    var data2 = dataGridView1.Rows[j].Cells[i].Value;
                    pX[i] += Convert.ToDouble(data1);
                    pY[i] += Convert.ToDouble(data2);
                    PBj += Per[j] * Convert.ToDouble(data2);
                }
                HY += PBj * Math.Log(PBj, 2);
                HX += Per[i] * Math.Log(Per[i], 2);
            }

            HX *= -1;
            HY *= -1;

            double[,] PAB = new double[NUM, NUM]; // P(A / B)
            double[,] PBA = new double[NUM, NUM]; // P(B / A)
            for (int i = 0; i < NUM; i++)
            {
                for (int j = 0; j < NUM; j++)
                {
                    var data = dataGridView1.Rows[i].Cells[j].Value;
                    PAB[i, j] = Convert.ToDouble(data) / pY[j];
                    PBA[i, j] = Convert.ToDouble(data) / pX[i];
                }
            }

            double HAB = 0, HBA = 0;
            double C = 0;
            for (int i = 0; i < NUM; i++)
            {
                double K = 0;
                double L = 0;
                for (int j = 0; j < NUM; j++)
                {
                    C += pX[i] * PBA[j, i] * Math.Log(PBA[j, i] / pY[j], 2);
                    var data1 = dataGridView1.Rows[i].Cells[j].Value;
                    var data2 = dataGridView1.Rows[j].Cells[i].Value;
                    L += Convert.ToDouble(data1) * Math.Log(Convert.ToDouble(data1), 2);
                    K += Convert.ToDouble(data2) * Math.Log(Convert.ToDouble(data2), 2);
                }
                HBA += L * Per[i];
                HAB += K * Per[i];
            }
            C *= -1;
            HBA *= -1;
            HAB *= -1;
            D *= HBA;

            double IXY = (NUM - 1) * HX - HBA;
            textBox1.AppendText("H( A ) = " + HX.ToString("G4") + " бит/символ" + "\r\n");
            textBox1.AppendText("H( B ) = " + HY.ToString("G4") + " бит/символ" + "\r\n");
            textBox1.AppendText("D      = " + D.ToString("G4") + " бит" + "\r\n");
            textBox1.AppendText("I(A,B) = " + IXY.ToString("G4")+ " бит" + "\r\n");
            textBox1.AppendText("H(A/B) = " + HAB.ToString("G4")+ " бит/символ" + "\r\n");
            textBox1.AppendText("H(B/A) = " + HBA.ToString("G4")+ " бит/символ" + "\r\n");
            textBox1.AppendText("C = " + C.ToString("G4")+ " бит/символ" + "\r\n");
        }
    }
}
