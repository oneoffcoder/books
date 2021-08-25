using System;

namespace ClassLibrary05
{
    public class C00Loop
    {
        static void Main(string[] args)
        {
            string[] names = { "jules", "james", "jackie" };
            
            foreach (string name in names)
            {
                Console.WriteLine(name);
            }
        }
    }
}
