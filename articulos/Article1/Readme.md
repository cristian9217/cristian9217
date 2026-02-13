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

Indique el ancho del techo: 30
Indique el largo del techo: 40

Costo #1: $10,666.67
Costo #2: $21,333.33
Costo #3: $32,000.00
