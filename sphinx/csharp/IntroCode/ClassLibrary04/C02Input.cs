using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary04
{
    class C02Input
    {
        class C01Input
        {
            static void Main(string[] args)
            {
                // a simple rectangle calculator
                Console.WriteLine("width: ");
                var width = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("height: ");
                var height = Convert.ToInt32(Console.ReadLine());

                var area = width * height;
                var perimeter = 2 * (width + height);

                Console.WriteLine($"area={area}, perimeter={perimeter}");
            }
        }
    }
}
