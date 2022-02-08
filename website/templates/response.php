<?php
include("connection.php");
class Student {
    protected $conn;
    protected $data = array();
    function __construct()  {

        $db = new dbObj();
        $connString =  $db->getConnstring();
        $this->conn = $connString;

    }
    public function getStudents() {

        $sql = "SELECT * FROM student";
        $queryRecords = pg_query($this->conn, $sql) or die("error to fetch student data");
        $data = pg_fetch_all($queryRecords);
        return $data;
    }
}
