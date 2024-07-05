using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BudgetMate.Model
{
    public class MainMenuSummaryCardModel
    {
        public int Savings { get; set; }
        public int Debt { get; set; }
        public int Expense { get; set; }
        public int ForeCast { get; set; }

        public MainMenuSummaryCardModel()
        {
            Savings = 0;
            Debt = 0;
            Expense = 0;
            ForeCast = 0;
        }
    }
}
