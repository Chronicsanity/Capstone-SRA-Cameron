<?php
Class dbObj{
        var $servername, $username, $password, $dbname, $port, $conn;

	__construct()
	{
	  $this->servername = "ec2-52-70-107-254.compute-1.amazonaws.com";
	  $this->username = "rpojgsgfhigprq";
	  $this->password = "3e74d2ed51b8ad75dadd84b7404ac6761f19396439f75c48c4921cf97e4b2b88";
	  $this->dbname = "d1aldo6rvck7l1";
	  $this->port = "5432";
	}
	function getConnstring() {
		$con = pg_connect("host=".$this->servername." port=".$this->port." dbname=".$this->dbname." user=".$this->username." password=".$this->password."") or die("Connection failed: ".pg_last_error());

		if (pg_last_error()) {
			printf("Connect failed: %s\n", pg_last_error());
			exit();
		} else {
			$this->conn = $con;
		}
		return $this->conn;
	}
}
?>