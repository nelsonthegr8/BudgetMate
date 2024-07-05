using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Data.SqlClient;
using Dapper;

namespace BudgetMate.DataAccess
{
   
    public class DataAccess
    {
        public string UserName = "Nelsonthegr8";
        SqlConnection connection = new SqlConnection("Data Source=tcp:budgetmatesrv.database.windows.net,1433;Initial Catalog=BudgetMateDB;User ID=BMAdmin;Password=Judese197!");
        public void GetAccountData(string UserName, int TypeID) 
        {
            var result = connection.Query(
                "exec bmsp_getAccountData @Username, @TypeID",
                new { this.UserName, TypeID }
            ).AsList();

            Console.Write(result);
        }

        public void insertAccountData(string AccountName, int AccountAmount, int AccountTypeID, int RoadMapID, string UserName)
        {
            var result = connection.Query(
                "exec bmsp_addAccountData @AccountName, @AccountAmount, @AccountTypeID, @RoadMapID, @UserName",
                new { AccountName, AccountAmount, AccountTypeID, RoadMapID, this.UserName}
            ).AsList();

            Console.Write(result);
        }

        public void GetMainMenuSummaryData(string UserName)
        {
            var result = connection.Query(
                "exec bmsp_addAccountData @AccountName, @AccountAmount, @AccountTypeID, @RoadMapID, @UserName",
                new { this.UserName }
            ).AsList();

            Console.Write(result);
        }
    }
}
