using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary03
{
    class C04Switch
    {
        static void Main(string[] args)
        {
            char grade = 'B';

            switch (grade)
            {
                case 'A':
                    Console.WriteLine("great job!");
                    break;
                case 'B':
                    Console.WriteLine("good job!");
                    break;
                case 'C':
                    Console.WriteLine("let's do better!");
                    break;
                case 'D':
                    Console.WriteLine("need serious improvement!");
                    break;
                default:
                    Console.WriteLine("ouch!");
                    break;
            }
        }
    }
}
