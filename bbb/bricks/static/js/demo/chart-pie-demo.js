// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
<<<<<<< HEAD
  type: 'Pie',
=======
  type: 'pie',
>>>>>>> 53d927fa2c5fff5a2ea438c3a829b8d1a3f235e3
  data: {
    labels: ["deposit","acquired", "unacquired"],
    datasets: [{
      data: [10, 55, 45],
      backgroundColor: ['#ffffff','#ff8080', '#ffb3b3'],
      hoverBackgroundColor: ['#ffffff','#ff9999', '#ffe6e6'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
<<<<<<< HEAD
    cutoutPercentage: 0,
=======
    cutoutPercentage: 10,
>>>>>>> 53d927fa2c5fff5a2ea438c3a829b8d1a3f235e3
  },
});
