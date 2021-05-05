using System;

namespace ClassLibrary01
{
    public class Class04ObjectTypes
    {
        static void Main(string[] args)
        {
            // you can store literal values in variables defined by object types
            Byte b = 127;
            Int16 s = 32_767;
            Int32 i = 2_147_483_647;
            Int64 l = 9_223_372_036_854_775_807L;
            Single f = 3.4e38f;
            Double d = 1.7e308d;
            Char c = 'Z';
            Boolean o = true;
            String t = "Hello, world!";
            
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