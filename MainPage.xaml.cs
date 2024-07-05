using System.Windows;
using Microcharts;
using SkiaSharp;

namespace BudgetMate
{
    public partial class MainPage : ContentPage
    {
        ChartEntry[] entries = new[]
        {
            new ChartEntry(112)
            {
                Label = "Jan",
                ValueLabel="112",
                Color = SKColor.Parse("#2c3e50")
            },
            new ChartEntry(200)
            {
                Label = "Feb",
                ValueLabel="200",
                Color = SKColor.Parse("#2c3e50")
            },
            new ChartEntry(300)
            {
                Label = "Mar",
                ValueLabel="300",
                Color = SKColor.Parse("#2c3e50")
            },
            new ChartEntry(400)
            {
                Label = "Apr",
                ValueLabel="400",
                Color = SKColor.Parse("#2c3e50")
            }
        };
        public MainPage()
        {
            InitializeComponent();

            chartView.Chart = new LineChart
            {
                Entries = entries
            };

        }

        

    }

}
