using BudgetMate.Model;
using System;
using System.Collections.Generic;
using System.Diagnostics.Metrics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Collections.ObjectModel;

namespace BudgetMate.ViewModel
{
    internal class MainPageViewModel: Object
    {
        private ObservableCollection<MainMenuSummaryCardModel> _menuSummaries = new();
        private ObservableCollection<NetworthModel> _networthModels = new();
        private DataAccess.DataAccess dataAccess = new DataAccess.DataAccess();  


        private void getMenuSummaryData() 
        {
            dataAccess.GetMainMenuSummaryData("");
        }

        private void getNetWorthData()
        {
            dataAccess.GetMainMenuSummaryData("");
        }
    }
}
