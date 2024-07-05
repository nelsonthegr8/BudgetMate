using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BudgetMate.Model
{
    public class NetworthModel
    {
        public string Month { get; set; }
        public string Year { get; set; }
        public int Amount { get; set; }

        public NetworthModel()
        {
            Month = "Jan";
            Year = DateTime.Now.Year.ToString();
            Amount = 0;
        }

    }
}
