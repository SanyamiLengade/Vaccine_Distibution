<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Statewise_Dustribution</title>
    <style>
      table{
        position: relative;
        left:120px;
        top:50px;
        border-collapse: collapse;
        width: 60%;
        font-size:20px;
        bottom:35px;
         

     }
th,td{
    text-align: left;
    padding: 8px;

}
tr:nth-child(even){
	background-color: #ddedff;
	
}
th{
	background-color: #3b77bb ;
    color: white;
	
}
</style>
</head>
<body>
<h2>State_Wise_Distribution</h2>

<table border="2" id="left">
  <tr>
      <th>State</th>
      <th>Confirmed</th>
      <th>Active</th>
      <th>No_of_vaccines</th>
  </tr>
  <?php
        $servername = "localhost";
        $username = "root";
        $password = "";
        $dbname = "vaccines";
        // Create connection
        $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
          die("Connection failed: " . $conn->connect_error);
        }

        //Displays all customers
        $sql = "SELECT * FROM state_final";
        $result = $conn->query($sql);

    
if ($result->num_rows > 0) {
          while ($row = $result->fetch_assoc()) {
            echo "<tr><td>" . $row["State"] . "</td><td>" . $row["Confirmed"] . "</td><td>" . $row["Active"] . "</td><td>"  . $row["NO_of_vaccines"] . "</td></tr>";
          }
        } else {
          echo "0 results";
        }
        $conn->close();
        ?>
</table>
</body>
</html>