using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary02
{
    class C04RelationalOperators
    {
        static void Main(string[] args)
        {
            var num1 = 4;
            var num2 = 2;

            // expressions of comparisons
            // always evaluate to true or false
            var a = num1 == num2;
            var b = num1 != num2;
            var c = num1 > num2;
            var d = num1 < num2;
            var e = num1 >= num2;
            var f = num1 <= num2;

            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            Console.WriteLine(d);
            Console.WriteLine(e);
            Console.WriteLine(f);
        }
    }
}
