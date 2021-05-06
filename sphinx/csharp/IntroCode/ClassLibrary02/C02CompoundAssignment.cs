using System;

namespace ClassLibrary02
{
    public class C02CompoundAssignment
    {
        static void Main(string[] args)
        {
            // compound assignment with addition
            int a = 10;
            a = a + 4;

            int b = 10;
            b += 4;

            // compound assignment with subtraction
            int c = 10;
            c = c - 4;

            int d = 10;
            d -= 4;

            // compound assignment with multiplication
            int e = 10;
            e = e * 2;

            int f = 10;
            f *= 2;

            // compound assignment with division
            int g = 10;
            g = g / 2;

            int h = 10;
            h /= 2;
            
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            Console.WriteLine(d);
            Console.WriteLine(e);
            Console.WriteLine(f);
            Console.WriteLine(g);
            Console.WriteLine(h);
        }
    }
}