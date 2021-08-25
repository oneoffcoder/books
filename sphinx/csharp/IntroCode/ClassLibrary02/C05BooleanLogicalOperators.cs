using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary02
{
    class C05BooleanLogicalOperators
    {
        static void Main(string[] args)
        {
            var a = false;
            var b = false;

            var not_a = !a;
            var a_or_b = a || b;
            var a_and_b = a && b;
            var ternary = a ? true : false;

            Console.WriteLine(not_a);
            Console.WriteLine(a_or_b);
            Console.WriteLine(a_and_b);
            Console.WriteLine(ternary);
        }
    }
}
