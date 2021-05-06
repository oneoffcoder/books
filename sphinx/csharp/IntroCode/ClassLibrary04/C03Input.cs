using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary04
{
    class C03Input
    {
        static void Main(string[] args)
        {
            // program to add, subtract, multiply and divide 2 numbers
            Console.WriteLine("num: ");
            var num1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("num: ");
            var num2 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine($"{num1} + {num2} = {num1 + num2}");
            Console.WriteLine($"{num1} - {num2} = {num1 - num2}");
            Console.WriteLine($"{num1} * {num2} = {num1 * num2}");
            Console.WriteLine($"{num1} / {num2} = {num1 / num2}");
        }
    }
}
