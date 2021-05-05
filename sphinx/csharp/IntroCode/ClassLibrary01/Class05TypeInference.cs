using System;

namespace ClassLibrary01
{
    public class Class05TypeInference
    {
        static void Main(string[] args)
        {
            // you can omit the type and use "var" to declare a variable
            // type inference will take place
            var b = 127;
            var s = 32_767;
            var i = 2_147_483_647;
            var l = 9_223_372_036_854_775_807L;
            var f = 3.4e38f;
            var d = 1.7e308d;
            var c = 'Z';
            var o = true;
            var t = "Hello, world!";
            
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