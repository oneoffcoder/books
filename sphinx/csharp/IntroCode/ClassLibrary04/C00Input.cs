using System;

namespace ClassLibrary04
{
    public class C00Input
    {
        static void Main(string[] args)
        {
            // getting input from the user
            Console.WriteLine("name: ");
            var name = Console.ReadLine();

            Console.WriteLine($"hello, {name}!");
        }
    }
}
