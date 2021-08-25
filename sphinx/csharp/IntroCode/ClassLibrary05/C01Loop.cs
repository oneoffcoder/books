using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary05
{
    class C01Loop
    {
        static void Main(string[] args)
        {
            // 1. create a string array of the planets and loop through them to print them
            // 2. create a float array of the following values: 32.2, 16.8, 3.4, 5.5, loop through them to print them

            string[] planets = { "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune" };
            float[] radiuses = { 32.2f, 16.8f, 3.4f, 5.5f };

            foreach (string planet in planets)
            {
                Console.WriteLine(planet);
            }

            foreach (float radius in radiuses)
            {
                Console.WriteLine(radius);
            }
        }
    }
}
