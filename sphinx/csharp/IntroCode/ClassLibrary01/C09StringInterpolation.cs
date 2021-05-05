using System;

namespace ClassLibrary01
{
    public class C09StringInterpolation
    {
        static void Main(string[] args)
        {
            // you can specify formatting of dates, floats and integers
            var name = "Alan Turing";
            var date = DateTime.Now;
            var cash = 3_000;
            
            Console.WriteLine($"{name}");
            Console.WriteLine($"{date:MM/dd/yyyy}");
            Console.WriteLine($"{date:MM/dd/yyyy HH:m:s}");
            Console.WriteLine($"{date:MM/dd/yyyy HH:m:s tt}");
            Console.WriteLine($"{Math.PI:0.##}");
            Console.WriteLine($"{Math.PI:F2}");
            Console.WriteLine($"{cash:N0}");
            Console.WriteLine($"{cash:N3}");
        }
    }
}