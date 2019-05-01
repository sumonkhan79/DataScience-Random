import csv
timing_data=[]
with open('/Users/sumon/desktop/TestTimingData.csv') as csv_file:
    file_reading = csv.reader(csv_file)
    for x in file_reading:
        timing_data.append(x)
#print(timing_data)
column_chart_data=['test name', 'difference from average']
csv_data = ['test name', 'run time in second']
for x in timing_data[1:]:
    test_name = x[0]
    #print(test_name)
    if x[1]== '':
        latest_run_time = 0
    else:
        latest_run_time = int(x[1])
    #print(latest_run_time)
    if x[2] == '':
        average_run_time = 0
    else:
        average_run_time = int(x[2])
     #   print(average_run_time)
    #print(average_run_time)
    #
    difference = average_run_time - latest_run_time
    #print(difference)
    column_chart_data.append([test_name, difference])
    csv_data.append([test_name,latest_run_time])
#print(column_chart_data)
#print(csv_data)
from string import Template

html_string = Template("""<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);

  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")
#print(htmlString)

chart_data_str = ''
for row in column_chart_data[1:]:
    print(row)
    chart_data_str += '%s,\n'%row
completed_html = html_string.substitute(labels=column_chart_data[0],data=chart_data_str)
#print(completed_html)
with open('/Users/sumon/chart.html','w') as f:
    #print(f)
     f.write(completed_html)