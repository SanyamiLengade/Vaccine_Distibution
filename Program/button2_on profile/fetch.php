<?php
    $con = mysqli_connect("localhost","root","","district");
    $sql = "Select Distinct State from district_sample";
    $res = mysqli_query($con , $sql);
?>
 
<!DOCTYPE html>
<html>
    <head>
        <title>District</title>
        <!-- <script type="text/javascript" src="js/function.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script> -->
        <style>
            table{
                position:relative;
                top:50px;
            }
        </style>
    </head>
    <body>
        Select State:
    

         <table>
            <thead>
                <th style="width:30%">State</th>
                <th style="width:30%">District</th>
                <th style="width:10%">Confirmed</th>
                <th style="width:10%">Active</th>
                <th style="width:10%">No of vaccines</th>
            </thead>
            <tbody id="ans">

            </tbody> 
     
        <form action="" method="post">
    <select name="Fruit">
        <option value="" disabled selected>Choose option</option>
        <option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
        <option value="Andhra Pradesh">Andhra Pradesh</option>
        <option value="Arunachal Pradesh">Arunachal Pradesh</option>
        <option value="Assam">Assam</option>
        <option value="Bihar">Bihar</option>
        <option value="Chandigarh">Chandigarh</option>
        <option value="Chhattisgarh">Chhattisgarh</option>
        <option value="Dadra and Nagar Haveli and Daman and Diu">Dadra and Nagar Haveli and Daman and Diu</option>
        <option value="Delhi">Delhi</option>
        <option value="goa">Goa</option>
        <option value="Gujarat">Gujarat</option>
        <option value="Haryana">Haryana</option>
        <option value="Himachal Pradesh">Himachal Pradesh</option>
        <option value="Jammu and Kashmir">Jammu and Kashmir</option>
        <option value="Jharkhan">Jharkhan</option>
        <option value="Karnataka">Karnataka</option>
        <option value="Kerala">Kerala</option>
        <option value="Ladakh">Ladakh</option>
        <option value="Lakshadweep">Lakshadweep</option>
        <option value="Madhya Pradesh">Madhya Pradesh</option>
        <option value="Maharashtra">Maharashtra</option>
        <option value="Manipur">Manipur</option>
        <option value="Meghalaya">Meghalaya</option>
        <option value="Mizoram">Mizoram</option>
        <option value="Nagaland">Nagaland</option>
        <option value="Odisha">Odisha</option>
        <option value="Puducherry">Puducherry</option>
        <option value="Punjab">Punjab</option>
        <option value="Rajasthan">Rajasthan</option>
        <option value="Sikkim">Sikkim</option>
        <option value="Tamil Nadu">Tamil Nadu</option>
        <option value="Telangana">Telangana</option>
        <option value="Tripura">Tripura</option>
        <option value="Uttar Pradesh">Uttar Pradesh</option>
        <option value="Uttarakhand">Uttarakhand</option>
        <option value="West Bengal">West Bengal</option>
        
    
    </select>

    <input type="submit" name="submit" vlaue="Choose options">
</form>
<?php
    if(isset($_POST['submit'])){
    if(!empty($_POST['Fruit'])) {
        $selected = $_POST['Fruit'];
        $sql = ("Select * from district_sample where State = '{$selected}'");
        $res = mysqli_query($con, $sql );
        if ($res->num_rows > 0) {
        while($rows = mysqli_fetch_array($res)){
            echo "<tr><td>" . $rows["State"] . "</td><td>" . $rows["District"] . "</td><td>" . $rows["Confirmed"] . "</td><td>" . $rows["Active"] . "</td><td>"  . $rows["No_of_vaccines"] . "</td></tr>";
    
         }
          } else {
            echo "0 results";
          }
          $con->close();
    } else {
        echo 'Please select the value.';
    }
    }
?>
   </table> 
    </body>
</html>