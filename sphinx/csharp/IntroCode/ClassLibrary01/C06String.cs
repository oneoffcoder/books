using System;

namespace ClassLibrary01
{
    public class C06String
    {
        static void Main(string[] args)
        {
            // creating strings
            var s1 = "hello, world";
            var s2 = new string("hello, world");

            Console.WriteLine(s1);
            Console.WriteLine(s2);
        }
    }
}