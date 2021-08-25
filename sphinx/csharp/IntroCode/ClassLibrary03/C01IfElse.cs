using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary03
{
    class C01IfElse
    {
        static void Main(string[] args)
        {
            int a = 10;
            int b = 9;

            // simple if statement
            // has if and else clauses
            // no else if clauses
            if (a > b)
            {
                Console.WriteLine("a > b");
            } else
            {
                Console.WriteLine("a < b");
            }
        }
    }
}
