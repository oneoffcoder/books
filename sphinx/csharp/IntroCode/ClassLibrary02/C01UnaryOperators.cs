using System;

namespace ClassLibrary02
{
    public class C01UnaryOperators
    {
        static void Main(string[] args)
        {
            // a = 10, b = 9, c = 9, d = 9, e = 9
            // why?
            // pre- and post-increment and pre- and post-decrement matters!
            // b is 9 because we pre-decrement 10 and then assign to b (decrement, then assign)
            // c is 9 because we post-decrement (assignment, then decrement)
            // d is 9 because we pre-increment (increment, then assign)
            // d is 9 because we post-increment (assign, then increment)
            int a = 10;
            int b = --a;
            int c = a--;
            int d = ++a;
            int e = a++;
            
            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            Console.WriteLine(d);
            Console.WriteLine(e);
        }
    }
}