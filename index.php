<?php
    $server="127.0.0.1";
    $username="localhost@root";
    $password="";

    $con= mysqli_connect($server,$username,$password);

    if(!=$con){
        die("connection failed due to" .mysqli_connect_error());
    }
    echo"success";
?>