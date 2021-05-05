using System;
using System.Linq;

namespace ClassLibrary01
{
    public class C07StringConcatenation
    {
        static void Main(string[] args)
        {
            // string concatenation is "adding" strings
            // here's a couple of ways to add strings together
            var s1 = "hello, i am" + " very excited to code";
            var s2 = string.Concat("hello", " world");
            var s3 = string.Join(",", "C#", "F#", "VB.NET");
            
            Console.WriteLine(s1);
            Console.WriteLine(s2);
            Console.WriteLine(s3);
        }
    }
}