using System;

namespace ClassLibrary01
{
    public class Class03PrimitiveTypes
    {
        static void Main(string[] args)
        {
            // you can store literal values in variables defined by "primitive" types
            byte b = 127;
            short s = 32_767;
            int i = 2_147_483_647;
            long l = 9_223_372_036_854_775_807L;
            float f = 3.4e38f;
            double d = 1.7e308d;
            char c = 'Z';
            bool o = true;
            string t = "Hello, world!";
            
            Console.WriteLine(b);
            Console.WriteLine(s);
            Console.WriteLine(i);
            Console.WriteLine(l);
            Console.WriteLine(f);
            Console.WriteLine(d);
            Console.WriteLine(c);
            Console.WriteLine(o);
            Console.WriteLine(t);
        }
    }
}