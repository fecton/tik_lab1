using System;
using System.Collections.Generic;
using System.Linq;

namespace Lab_6_TIC_ArithmeticCoding
{
    public class Node
    {
        public char Symbol { get; set; }
        public decimal Low { get; set; }
        public decimal High { get; set; }
        public decimal Range { get; set; }
        public int Frequency { get; set; }
    }

    public class ArifmCode
    {
        private List<Node> nodes = new List<Node>();
        public Dictionary<char, int> Frequencies = new Dictionary<char, int>();

        public void Build(string source)
        {
            for (int i = 0; i < source.Length; i++)
            {
                if (!Frequencies.ContainsKey(source[i]))
                {
                    Frequencies.Add(source[i], 0);
                }

                Frequencies[source[i]]++;
            }

            foreach (KeyValuePair<char, int> symbol in Frequencies)
            {
                nodes.Add(new Node() { Symbol = symbol.Key, Frequency = symbol.Value });
            }
            nodes = nodes.OrderBy(node => node.Frequency).ToList<Node>();
        }

        public List<Node> GetSymbolsRanges(string source)
        {
            decimal low = 0.0m;
            foreach (Node node in nodes)
            {
                node.Range = ((decimal)(node.Frequency) / (source.Length));
                node.Low = low;
                node.High = low + node.Range;
                low += node.Range;
            }
            return nodes;
        }

        public decimal Encode(string source, out List<Node> resNodes)
        {
            nodes.Reverse();
            List<Node> allNodes = new List<Node>();

            for (int i = 0; i < source.Length; i++)
            {
                for (int j = 0; j < nodes.Count; j++)
                {
                    if (source[i] == nodes[j].Symbol)
                    {
                        allNodes.Add(new Node() { Symbol = nodes[j].Symbol, Low = nodes[j].Low, High = nodes[j].High });
                    }
                }
            }

            for (int i = 1; i < allNodes.Count; i++)
            {
                for (int j = 0; j < nodes.Count; j++)
                {
                    if (allNodes[i].Symbol == nodes[j].Symbol)
                    {
                        allNodes[i].High = allNodes[i - 1].Low + (allNodes[i - 1].High - allNodes[i - 1].Low) * nodes[j].High;
                        allNodes[i].Low = allNodes[i - 1].Low + (allNodes[i - 1].High - allNodes[i - 1].Low) * nodes[j].Low;
                    }
                }
            }
            resNodes = allNodes;
            return Math.Round((allNodes[allNodes.Count - 1].Low + ((allNodes[allNodes.Count - 1].High - allNodes[allNodes.Count - 1].Low)/2)), 8);
        }

        public string Decode(List<Node> allNodes, int count, decimal inCode)
        {
            string decode = "";
            decimal code = inCode;
            int symbolsCount = 0;

            while (true)
            {
                for (int i = 0; i < nodes.Count; i++)
                {
                    if (code >= nodes[i].Low && code < nodes[i].High)
                    {
                        decode += nodes[i].Symbol;
                        code = Math.Round(((code - nodes[i].Low) / (nodes[i].High - nodes[i].Low)), 8);
                        symbolsCount++;
                        if (symbolsCount == count)
                            return decode;
                    }
                }
            }
        }
    }
}
