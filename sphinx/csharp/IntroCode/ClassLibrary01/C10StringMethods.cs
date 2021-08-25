using System;
using Microsoft.VisualBasic;

namespace ClassLibrary01
{
    public class C10StringMethods
    {
        static void Main(string[] args)
        {
            var s1 = "hello, world";
            var s2 = "hello, world!";
            var s3 = "hello, world";
            
            // string comparison
            Console.WriteLine($"s1.equals(s2): {s1.Equals(s2)}");
            Console.WriteLine($"s1.equals(s3): {s1.Equals(s3)}");
            
            Console.WriteLine($"s1 == s2: {s1 == s2}");
            Console.WriteLine($"s1 == s3: {s1 == s3}");

            // string methods
            Console.WriteLine(s1.StartsWith("hello"));
            Console.WriteLine(s1.EndsWith("world"));
            Console.WriteLine(s1.Replace("world", "earth"));
            Console.WriteLine(s1.ToUpper());
            Console.WriteLine(s1.ToLower());
            Console.WriteLine(s1.Contains(','));
            Console.WriteLine(s1.IndexOf(','));
            Console.WriteLine(s1.Split(','));
            Console.WriteLine(s1.Substring(0, 5));
            Console.WriteLine(s1.Length);
        }
    }
}