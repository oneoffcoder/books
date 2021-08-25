using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary03
{
    class C05Switch
    {
        static void Main(string[] args)
        {
            var ethnicity = 1;
            var gender = "female";

            switch (ethnicity)
            {
                case 0:
                    switch (gender)
                    {
                        case "male":
                            Console.WriteLine("white male");
                            break;
                        default:
                            Console.WriteLine("white female");
                            break;
                    }
                    break;
                case 1:
                    switch (gender)
                    {
                        case "male":
                            Console.WriteLine("minority male");
                            break;
                        default:
                            Console.WriteLine("minority female");
                            break;
                    }
                    break;
            }
        }
    }
}
