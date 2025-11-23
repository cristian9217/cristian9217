/**
 * File: CreateCourse.php
 * Course: COTI-4210-MR1
 * Date: May 15, 2020
 * Purpose: Handles the creation of courses in the system, including 
 * validation and insertion into the database using PHP and MySQL.
 */

<?php
	// Create a connection to the database
	$conn = new mysqli($server, $user, $password, $dbname);
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}

	/** Sanitize user input by trimming, stripping slashes, and managing HTML entities. */
	function setString($input, $length = null)
	{
		$input = substr($input, 0, $length);
		$input = stripslashes(trim($input));
		return htmlspecialchars($input);
	}
	
	/** Format number as float with two decimal places if numeric. */
	function setNumberFloat($input)
	{
		return is_numeric($input) ? number_format($input, 2, ".", ",") : $input;
	}

	// ======== VALIDATIONS ========

	// Initialize an array to store errors
	$errors = [];

	// Validate idCurso: should match 3 digits - 4 digits pattern
	$idCurso = setString($_POST['idCurso'], 8);
	if (!preg_match('/^\d{3}-\d{4}$/', $idCurso)) {
		$errors[] = "El formato del idCurso debe ser <b>999-9999</b>."; 
	}

	// Validate nombre: allow only alphanumeric and letters.
	$nombre = setString($_POST['nombre'], 30);
	if (!preg_match('/^[\p{L}0-9 \-\_\.\,\(\)\:]+$/u', $nombre)) {
		$errors[] = "El nombre solo puede contener letras y números.";
	}

	// Validate titulo: allow only alphanumeric and letters.
	$titulo = setString($_POST['titulo'], 100);
	if (!preg_match('/^[\p{L}0-9 \-\_\.\,\(\)\:]+$/u', $titulo)) {
		$errors[] = "El título solo puede contener letras y números.";
	}

	// Validate credito: check if the input is numeric.
	$MIN_CREDITO = 0.5;
	$MAX_CREDITO = 10.0;
	
	if (!is_numeric($_POST['credito'])) {
		$errors[] = "El crédito debe ser un número.";
	}
	
	$credito = setNumberFloat($_POST['credito']);
	if($credito < $MIN_CREDITO || $_POST['credito'] > $MAX_CREDITO) {
		$errors[] = sprintf("El crédito debe estar entre %.1f y %.1f.", 
			$MIN_CREDITO, $MAX_CREDITO);
	}

	// Validate prerrequisito: checks if it is not empty and validates its format.
	$prerrequisito = setString($_POST['prerequisito'], 8);
	if (!empty($prerrequisito)) 
	{
		if (!preg_match('/^\d{3}-\d{4}$/', $prerrequisito)) 
		{
			$errors[] = "El formato del prerrequisito debe ser 999-9999 o dejarse vacío.";
		} 
		else 
		{
			$stmtCheck = $conn->prepare("SELECT * FROM course WHERE id_course_pk = ?");
			$stmtCheck->bind_param("s", $prerrequisito);
			$stmtCheck->execute();
			$resultCheck = $stmtCheck->get_result();
			if ($resultCheck->num_rows === 0) 
				$errors[] = "El prerrequisito ingresado no existe en el sistema.";			
			$stmtCheck->close();
		}
	} 
	else 
	{
		$prerrequisito = null;
	}

	// Check if course with same idCurso already exists
	$stmtCheckCourse = $conn->prepare("SELECT * FROM course WHERE id_course_pk = ?");
	$stmtCheckCourse->bind_param("s", $idCurso);
	$stmtCheckCourse->execute();
	$resultCourse = $stmtCheckCourse->get_result();
	if ($resultCourse->num_rows > 0) {
		$errors[] = "El curso con el ID <b>$idCurso</b> ya existe.";
	}
	$stmtCheckCourse->close();

	// ======== INSERT INTO TABLE COURSE ========
	if (empty($errors)) 
	{
		$sqlInsertCourse = "INSERT INTO course (id_course_pk, nombre, titulo, 
			credito, prerrequisito) VALUES (?, ?, ?, ?, ?)";
		$stmtInsertCourse = $conn->prepare($sqlInsertCourse);
		$stmtInsertCourse->bind_param("sssds", $idCurso, $nombre, 
			$titulo, $credito, $prerrequisito);
		$stmtInsertCourse->execute();

		if($stmtInsertCourse->affected_rows > 0) 
		{
			echo "<div class='alertMessage alert-success'>";
				echo "<p class='title'>Success!</p>";
				echo "<p class='msg'>Record added successfully!</p>";
			echo "</div>";
		} 
		else 
		{
			echo "<div class='alertMessage alert-error'>";
				echo "<p class='title'>Error!</p>";
				echo "<p class='msg'>No record was inserted.</p>";
			echo "</div>";
		}

		$stmtInsertCourse->close();
	} 
	else 
	{
		// Show errors
		echo "<div class='alertMessage alert-error'>";
			echo "<p class='title'>Validation Errors:</p>";
			foreach ($errors as $error) {
				echo "<p class='msg'>$error</p>";
			}
		echo "</div>";
	}

	$conn->close();
?>
