using System;

namespace ClassLibrary01
{
    public class Class02PrintMath
    {
        static void Main(string[] args)
        {
            // basic math operations
            Console.WriteLine(3 + 2);
            Console.WriteLine(3 - 2);
            Console.WriteLine(3 * 2);
            Console.WriteLine(3 / 2);
            
            // if you want a real number, make sure denominator is a decimal number
            Console.WriteLine(3 / 2.0);
            
            // PEMDAS
            Console.WriteLine(5 + 2 * 3); // 11
            Console.WriteLine((5 + 2) * 3); // 21
            
            // division operator gives quotient
            // modulus operator gives remainder
            Console.WriteLine(3 / 2);
            Console.WriteLine(3 % 2);
        }
    }
}