using System;

namespace ClassLibrary02
{
    public class C03BitwiseOperators
    {
        static void Main(string[] args)
        {
            var a = 42;
            var b = 15;

            var q = ~42; // bitwise not
            var r = a | b; // bitwise or
            var s = a & b; // btiwise and
            var t = a ^ b; // bitwise XOR
            
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(q);
            Console.WriteLine(r);
            Console.WriteLine(s);
            Console.WriteLine(t);
        }
    }
}