using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        private static readonly Random Random = new Random();
        public static double GetRandomNumber(double minimum, double maximum)
        {
            return Random.NextDouble() * (maximum - minimum) + minimum;
        }
        static int Binomial(int n, double p)
        {
            int s = 0;
            for (int i = 0; i < n; i++)
            {
                double a = GetRandomNumber(0, 1);
                Console.WriteLine(a);
                if (a < p)
                {
                    s++;
                }

            }
            return s;
        }
        static void Main(string[] args)
        {
            int[] zeichneBinom = new int[100];
            int count = 0;
            while (count < 5)
            {
                zeichneBinom[count] = Binomial(3, 0.427);
                Console.WriteLine(zeichneBinom[count]);
                count++;
            }
           /* System.IO.StreamWriter textFile = new System.IO.StreamWriter(@"D:binom.txt");
            foreach (int t in zeichneBinom)
            {
                textFile.WriteLine(zeichneBinom[t]);
            }*/
            Console.ReadKey();
        }
    }
}
