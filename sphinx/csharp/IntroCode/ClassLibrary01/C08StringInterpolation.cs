using System;

namespace ClassLibrary01
{
    public class C08StringInterpolation
    {
        static void Main(string[] args)
        {
            var firstName = "Alan";
            var lastName = "Turing";
            
            // composite formatting
            Console.WriteLine("{0} {1}", firstName, lastName);
            
            // string interpolation
            var sentence = $"{firstName} {lastName}";
            Console.WriteLine(sentence);
        }
    }
}