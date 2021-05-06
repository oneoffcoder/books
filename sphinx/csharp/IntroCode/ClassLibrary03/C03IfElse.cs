using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary03
{
    class C03IfElse
    {
        static void Main(string[] args)
        {
            int a = 9;

            // if must always come first
            // else must always come last
            // else if can be as many as required, always in middle
            if (a > 20)
            {
                Console.WriteLine("a > 20");
            }
            else if (a > 10)
            {
                Console.WriteLine("a > 10");
            }
            else if (a > 5)
            {
                Console.WriteLine("a > 5");
            }
            else
            {
                Console.WriteLine("a <= 5");
            }
        }
    }
}
