<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>


<?php
include("response.php");
    $newObj = new Student();
    $emps = $newObj->getStudents();
?>

<table id="student_grid" class="table" width="100%" cellspacing="0">
    <thead>
    <tr>
    <th>tnumber</th>
    <th>firstname</th>
    <th>middlename</th>
    <th>lastname</th>
    <th>term</th>
    <th>level</th>
    <th>pprogram</th>
    <th>ppname</th>
    <th>pcollege</th>
    <th>pdept</th>
    <th>pdeptdesc</th>
    <th>sprogram</th>
    <th>spname</th>
    <th>scollege</th>
    <th>sdept</th>
    <th>sdeptdesc</th>
    <th>decision</th>
    <th>admit</th>
    <th>saddress1</th>
    <th>saddress2</th>
    <th>city</th>
    <th>state</th>
    <th>zip</th>
    <th>phonearea</th>
    <th>phonenum</th>
    <th>phonenumex</th>
    <th>email</th>
    <th>ualremail</th>
    <th>ethnicity</th>
    <th>sex</th>
    <th>admission</th>
    <th>studenttype</th>
    </tr>
    </thead>
<tbody>
    <?php foreach($emps as $key => $emp) :?>
    <tr>
        <td><?php echo $emp['student_tnumber'] ?></td>
        <td><?php echo $emp['student_firstname'] ?></td>
        <td><?php echo $emp['student_middlename'] ?></td>
        <td><?php echo $emp['student_lastname'] ?></td>
        <td><?php echo $emp['student_term'] ?></td>
        <td><?php echo $emp['student_level'] ?></td>
        <td><?php echo $emp['student_pprogram'] ?></td>
        <td><?php echo $emp['student_ppname'] ?></td>
        <td><?php echo $emp['student_pcollege'] ?></td>
        <td><?php echo $emp['student_pdept'] ?></td>
        <td><?php echo $emp['student_pdeptdesc'] ?></td>
        <td><?php echo $emp['student_sprogram'] ?></td>
        <td><?php echo $emp['student_spname'] ?></td>
        <td><?php echo $emp['student_scollege'] ?></td>
        <td><?php echo $emp['student_sdept'] ?></td>
        <td><?php echo $emp['student_sdeptdesc'] ?></td>
        <td><?php echo $emp['student_decision'] ?></td>
        <td><?php echo $emp['student_admit'] ?></td>
        <td><?php echo $emp['student_saddress1'] ?></td>
        <td><?php echo $emp['student_saddress2'] ?></td>
        <td><?php echo $emp['student_city'] ?></td>
        <td><?php echo $emp['student_state'] ?></td>
        <td><?php echo $emp['student_zip'] ?></td>
        <td><?php echo $emp['student_phonearea'] ?></td>
        <td><?php echo $emp['student_phonenum'] ?></td>
        <td><?php echo $emp['student_phonenumex'] ?></td>
        <td><?php echo $emp['student_email'] ?></td>
        <td><?php echo $emp['student_ualremail'] ?></td>
        <td><?php echo $emp['student_ethnicity'] ?></td>
        <td><?php echo $emp['student_sex'] ?></td>
        <td><?php echo $emp['student_admission'] ?></td>
        <td><?php echo $emp['student_studenttype'] ?></td>
        <td><?php echo $emp['student_firstname'] ?></td>
        <td><div class="btn-group" data-toggle="buttons"><a href="#" target="_blank" class="btn btn-warning btn-xs" rel="noopener">Edit</a><a href="#" target="_blank" class="btn btn-danger btn-xs" rel="noopener">Delete</a><a href="#" target="_blank" class="btn btn-primary btn-xs" rel="noopener">View</a></div></td>
    </tr>
    <?php endforeach;?>
</tbody>
</table>