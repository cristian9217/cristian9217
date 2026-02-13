# RoofCost

## Overview

`RoofCost` is a Java program that calculates the area of a roof and estimates its cost based on three different 
pricing rates. It provides an easy way to quickly determine roofing expenses for given dimensions.

## Features 
- Calculates roof area in square meters.
- Estimates costs using three predefined rates.
- Simple command-line interface for input and output.

## Usage 
1. Run the program.
2. Follow the prompts:
   - Enter the width of the roof.
   - Enter the length of the roof.
3. The program will display estimated costs for three rates.

## Methods 
- `getArea(double ancho, double largo):` Returns the area of the roof divided by 9.
- `getPrecio(int index, double area)`: Returns the cost using one of three rates (8, 16, 24)
   multiplied by the area.

## Example

```java
Indique el ancho del techo: 25.5
Indique el largo del techo: 40.5

Costo #1: $918.00
Costo #2: $1,836.00
Costo #3: $2,754.00
```

---

# CreateCourse.php

## Overview
`CreateCourse.php` is a PHP script that handles the creation of courses in a system 
using MySQL. It validates user input and inserts new course records into the database.

## Features
- Validates course ID, name, title, credits, and prerequisites.
- Checks for duplicate courses before insertion.
- Sanitizes input to prevent SQL injection and XSS.
- Displays success or error messages for feedback.

## Requirements
- PHP 7.x or higher.
- MySQL database connection.
- Docker installed and configured on your system.

## Usage
1. Configure database connection variables (`$server`, `$user`, `$password`, `$dbname`) at the top of the script.
2. Submit course data via POST request with these fields:
   - `idCurso` (format `999-9999`)  
   - `nombre` (alphanumeric, max 30 chars)  
   - `titulo` (alphanumeric, max 100 chars)  
   - `credito` (numeric, between 0.5 and 10.0)  
   - `prerequisito` (optional, format `999-9999`)  
3. The script validates inputs, checks prerequisites, and inserts the record if valid.
4. Displays success or error messages.

## Example POST Input
```text
idCurso=101-0001
nombre=Matematicas
titulo=Calculo I
credito=3.0
prerequisito=
