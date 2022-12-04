using System;

namespace ConsoleApp31
{
    class Program
    {
        static string Demo(int Count) // для двух
        {
            Console.WriteLine("Введите число от 1 до 50");
            int a = Int32.Parse(Console.ReadLine());
            int[] c = new int[10];
            Random d = new Random();
            string L = " ";
             Count = 0;
            Console.WriteLine(" ");

            for (int i = 0; i < c.Length; i++)
            {
                c[i] = d.Next(1,51);
                Console.WriteLine(c[i]);
                if (c[i] == a)
                    Count++;
            }
            if (Count == 1)
                L = " БОЛЬШАЯ ПОБЕДА. 50 коп.";
            else if (Count == 0)
                L = " Не повезло, 20 коп.";
            return L;
        }
        static string Demo2(int Count) // для трех
        {
            Console.WriteLine("Введите число от 1 до 20");
            int a = Int32.Parse(Console.ReadLine());
            int[] c = new int[10];
            Random d = new Random();
            string L = " ";
            Count = 0;
            Console.WriteLine(" ");

            for (int i = 0; i < c.Length; i++)
            {
                c[i] = d.Next(1, 21);
                Console.WriteLine(c[i]);
                if (c[i] == a)
                    Count++;
            }
            switch (Count)
            {
                case 0:
                    L = " Попробуйте еще раз ";
                    break;

                case 1:
                    L = " Неплохо. Повезло.1р.55коп.";
                    break;

                case 2:
                    L = "Очень хорошо!1р.60коп.";
                    break;

                case 3:
                    L = " Пора покупать лотарейные билеты) 2р. ";
                    break;

                case 4:
                    L = " Может сходишь в реальное казино? 5р. ";
                    break;

                case 5:
                    L = " Ультра победа 7.5р. ";
                    break;

                case 6:
                    L = "Я не знал, что такое возможно 10р.";
                    break;

                case 7:
                    L = "МУЖИК... 20р.";
                    break;

                case 8:
                    L = " БЛЯ, я в ахуе 60р.";
                    break;

                case 9:
                    L = " ВЫКЛЮЧИ КОМП 65р. ";
                    break;

                case 10:
                    L = "Блять, ты просто охуел, реально, не заходи сюда больше никогда, наглотайся таблеток и прыгни в окно. Хотя... С твоей удачей ты все равно выживешь 100р.";
                    break;
                    

            }
            return L;
        }
        static void Main(string[] args) 
        {
            Console.WriteLine("Ставка 5 коп.");
            Console.WriteLine("Введите число от 1 до 50");
            int a = Int32.Parse(Console.ReadLine());
            int[] c = new int[10];
            Random d = new Random();
            int Count = 0;
            Console.WriteLine(" ");

            for (int i = 0;i<c.Length;i++)
            {
                c[i] = d.Next(1,51);
                Console.WriteLine(c[i]);
                if (c[i] == a)
                    Count++;
            }
            if (Count == 1)
                Console.WriteLine("Победа,15коп. ");
            else if (Count == 0)
                Console.WriteLine("Попробуй еще раз ");
            if (Count == 2)
            {
                string f = Demo(Count);
                Console.WriteLine(f);
            }

            if (Count == 3)
            {
                string f = Demo2(Count);
                Console.WriteLine(f);
            }
            if (Count == 4)
            {
                Console.WriteLine("Введите число от 1 до 1000");
                int a1 = Int32.Parse(Console.ReadLine());
                int[] c1 = new int[150];
                Random d1 = new Random();
                 Count = 0;
                Console.WriteLine(" ");

                for (int i = 0; i < c.Length; i++)
                {
                    c[i] = d.Next(1, 1001);
                    Console.WriteLine(c[i]);
                    if (c[i] == a)
                        Count++;
                }
                if (Count == 1)
                    Console.WriteLine("Победа,15коп. ");
                else if (Count == 0)
                    Console.WriteLine("Попробуй еще раз ");
                if (Count == 2)
                {
                    string f = Demo(Count);
                    Console.WriteLine(f + " + бонус 5р ");
                }

                if (Count == 3)
                {
                    string f = Demo2(Count);
                    Console.WriteLine(f + " + бонус 15р ");
                    
                }




            }    
        }
    }
}
