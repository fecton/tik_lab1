using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HammingCode
{
    public class HuffmanTree
    {
        public int indexAddName = 0;
        public List<Node> nodes = new List<Node>();
        public Node Root { get; set; }
        public Dictionary<char, double> Frequencies = new Dictionary<char, double>();

        public Dictionary<char, double> BuildNodes(string text)
        {
            if (text.Length == 0) return null;
            Frequencies.Clear();
            foreach (char c in text)
            {
                if (!Frequencies.Keys.Contains(c))
                {
                    Frequencies.Add(c, text.Count(el => el == c) / (double)text.Length);
                }
            }
         
            nodes.Clear();
            indexAddName = 0;
            
            Frequencies = Frequencies.OrderBy(k => k.Value).ToDictionary(k => k.Key, k => k.Value);
            string tmp = "Build Nodes\n";
            foreach (KeyValuePair<char, double> c in Frequencies)
            {
                tmp += c.Key.ToString() + c.Value.ToString();
                nodes.Add(new Node { Symbol = c.Key, Frequency = c.Value, AddName = "x"+indexAddName++.ToString() });
            }
            MessageBox.Show(tmp);
            return Frequencies;

        }

        public Dictionary<char, double> BuildNodes(Dictionary<char, double> inputProbabilities)
        {
            Frequencies = inputProbabilities;
            
            nodes.Clear();
            indexAddName = 0;

            foreach(KeyValuePair<char, double> c in Frequencies)
            {
                nodes.Add(new Node { Symbol = c.Key, Frequency = c.Value, AddName = "x"+indexAddName++.ToString()});
            }
            return Frequencies;
        }

        public Dictionary<char, BitArray> BuildHuffmanTree()
        {
            while (nodes.Count > 1)
            {
                List<Node> orderedNodes = nodes.OrderBy(node => node.Frequency).ThenByDescending(node => node.AddName).ToList<Node>();
                //string tmp = "";
                //for(int i =0; i< orderedNodes.Count;i++)
                //{
                //    tmp += $"char:{orderedNodes[i].Symbol}|value:{orderedNodes[i].Frequency}|addName:{orderedNodes[i].AddName}\n";
                //}
                //MessageBox.Show(tmp);
                if (orderedNodes.Count >= 2)
                {
                    // Take first two items
                    List<Node> taken = orderedNodes.Take(2).ToList<Node>();

                    // Create a parent node by combining the frequencies
                    Node parent = new Node()
                    {
                        Symbol = '!',
                        Frequency = taken[0].Frequency + taken[1].Frequency,
                        Left = taken[0],
                        Right = taken[1],
                        AddName = "x" + indexAddName++.ToString()
                    };

                    //string tmp1 = $"{taken[0].Symbol} = ${taken[0].Frequency}|||{taken[1].Symbol} = ${taken[1].Frequency}";
                    //MessageBox.Show(tmp1);
                    nodes.Remove(taken[0]);
                    nodes.Remove(taken[1]);
                    nodes.Add(parent);

                }
                this.Root = nodes.FirstOrDefault();
            }

            Dictionary<char, BitArray> huffmanCodesTable = new Dictionary<char, BitArray>();

            // Frequencies = Frequencies.OrderBy(i => i.Key).ToDictionary<KeyValuePair<char, double>>(k => k.Key); 
            string tmp = "Frequinces:\n";
            foreach(var a in Frequencies)
            {
                tmp += "key:" + a.Key.ToString() + "|value:" + a.Value.ToString() + "\n";
            }
            foreach (char c in Frequencies.Keys)
            {
                huffmanCodesTable.Add(c, new BitArray(this.Root.Traverse(c, new List<bool>()).ToArray()));
            }
            return huffmanCodesTable;
        }

        public BitArray Encode(string source)
        {
            List<bool> encodedSource = new List<bool>();

            for (int i = 0; i < source.Length; i++)
            {
                List<bool> encodedSymbol = this.Root.Traverse(source[i], new List<bool>());
                encodedSource.AddRange(encodedSymbol);
            }

            BitArray bits = new BitArray(encodedSource.ToArray());

            return bits;
        }

        public string Decode(BitArray bits)
        {
            Node current = this.Root;
            string decoded = "";

            foreach (bool bit in bits)
            {
                if (bit)
                {
                    if (current.Right != null)
                    {
                        current = current.Right;
                    }
                }
                else
                {
                    if (current.Left != null)
                    {
                        current = current.Left;
                    }
                }

                if (IsLeaf(current))
                {
                    decoded += current.Symbol;
                    current = this.Root;
                }
            }

            return decoded;
        }

        public bool IsLeaf(Node node)
        {
            return (node.Left == null && node.Right == null);
        }
    }

    public class Node
    {
        public char Symbol { get; set; }
        public double Frequency { get; set; }
        public Node Right { get; set; }
        public Node Left { get; set; }
        public string AddName { get; set; }
        public List<bool> Traverse(char symbol, List<bool> data)
        {
            // Leaf
            if (Right == null && Left == null)
            {
                if (symbol.Equals(this.Symbol))
                {
                    return data;
                }
                else
                {
                    return null;
                }
            }
            else
            {
                List<bool> left = null;
                List<bool> right = null;

                if (Left != null)
                {
                    List<bool> leftPath = new List<bool>();
                    leftPath.AddRange(data);
                    leftPath.Add(false);

                    left = Left.Traverse(symbol, leftPath);
                }

                if (Right != null)
                {
                    List<bool> rightPath = new List<bool>();
                    rightPath.AddRange(data);
                    rightPath.Add(true);
                    right = Right.Traverse(symbol, rightPath);
                }

                if (left != null)
                {
                    return left;
                }
                else
                {
                    return right;
                }
            }
        }
    }
}
