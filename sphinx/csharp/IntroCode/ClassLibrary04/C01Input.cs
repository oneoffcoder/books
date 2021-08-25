using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary04
{
    class C01Input
    {
        static void Main(string[] args)
        {
            // converting input to the appropriate type
            Console.WriteLine("age: ");
            var age = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine($"{age}");
        }
    }
}
