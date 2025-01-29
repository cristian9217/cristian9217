/*
 * Name: script.js
 * Author: Cristian M. Pagan
 * Course: SICI-4997
 * Date: 01/29/2025
 * Purpose: This script creates a dynamic pie chart for displaying 
 * courses in different modalities for a specific semester using Chart.js. 
 * The chart shows how many courses are offered in Hybrid, Presencial, 
 * and Distance modality, and displays the percentage of each modality.
 */

async function filterData() 
{
	try 
	{
		// Base URL for the raw GitHub content
		var baseUrl = "https://raw.githubusercontent.com/cristian9217/";
		var path = "cristian9217/default/courses/SICI4997/csv/";
		var file = "uprb_database.csv";
		
		// Construct the full URL for the CSV file
		const csvUrl = baseUrl + path + file;
		
		// Sends a request to fetch the file
		const response = await fetch(csvUrl); 
		
		// Waits for the response and converts it to text
		const csvText = await response.text(); 
	
	    // Parse the CSV text into a JavaScript object using PapaParse
		const { data } = Papa.parse(csvText, { header: true, dynamicTyping: true });
		
		// Calculate the amount of data for each semester and its modality.	
		const hybridC12 = modalityTerm(data, "C12", "(H) - Hybrid").length;
		const hybridC11 = modalityTerm(data, "C11", "(H) - Hybrid").length;
		const hybridC03 = modalityTerm(data, "C03", "(H) - Hybrid").length;
		const hybridC02 = modalityTerm(data, "C02", "(H) - Hybrid").length;
		
		document.getElementById("hybridC12").innerText = hybridC12;
		document.getElementById("hybridC11").innerText = hybridC11;
		document.getElementById("hybridC03").innerText = hybridC03;
		document.getElementById("hybridC02").innerText = hybridC02;
		
		const presencialC12 = modalityTerm(data, "C12", "(P) - Presencial").length;
		const presencialC11 = modalityTerm(data, "C11", "(P) - Presencial").length;
		const presencialC03 = modalityTerm(data, "C03", "(P) - Presencial").length;
		const presencialC02 = modalityTerm(data, "C02", "(P) - Presencial").length;
		
		document.getElementById("presencialC12").innerText = presencialC12;
		document.getElementById("presencialC11").innerText = presencialC11;
		document.getElementById("presencialC03").innerText = presencialC03;
		document.getElementById("presencialC02").innerText = presencialC02;
		
		const distanceC12 = modalityTerm(data, "C12", "(D) - Distance").length;
		const distanceC11 = modalityTerm(data, "C11", "(D) - Distance").length;
		const distanceC03 = modalityTerm(data, "C03", "(D) - Distance").length;
		const distanceC02 = modalityTerm(data, "C02", "(D) - Distance").length;
		
		document.getElementById("distanceC12").innerText = distanceC12;
		document.getElementById("distanceC11").innerText = distanceC11;
		document.getElementById("distanceC03").innerText = distanceC03;
		document.getElementById("distanceC02").innerText = distanceC02;
		
		createPieChart('modalityC11', 'Courses in each modality for C11', 
			[hybridC11, presencialC11, distanceC11]);
		createPieChart('modalityC03', 'Courses in each modality for C11', 
			[hybridC03, presencialC03, distanceC03]);
		
		// Calculate the amount of data for each semester, modality, and course code.
        document.getElementById("COTIPresC11").innerText =
			modalityTermCourse(data, "C11", "(P) - Presencial", "COTI3101").length;

        // Calculate the amount of data created from course ID and semester.
        document.getElementById("COTI3101C11").innerText =
			modalityCourse(data, "C11", "COTI3101").length;

        // Calculate the amount of data offered on days in semester C11
        document.getElementById("twoDaysC11").innerText = 
			modalityTermDays(data, "C11", "TuTh").length;
        document.getElementById("oneDayC11").innerText = 
			modalityTermDays(data, "C11", "W").length;

        // Calculate the amount of courses created in each semester
        const totalC22 = showCourseTerm(data, "C22").length;
        const totalC12 = showCourseTerm(data, "C12").length;
        const totalC11 = showCourseTerm(data, "C11").length;
        const totalC03 = showCourseTerm(data, "C03").length;
        const totalC02 = showCourseTerm(data, "C02").length;
		
		document.getElementById("totalC22").innerText = totalC22;
		document.getElementById("totalC12").innerText = totalC12;
		document.getElementById("totalC11").innerText = totalC11;
		document.getElementById("totalC03").innerText = totalC03;
		document.getElementById("totalC02").innerText = totalC02;

		createChart([totalC22, totalC12, totalC11, totalC03, totalC02]);
				
		// Calculate the course offered in semester and difference.
		document.getElementById("totalC11_diff").innerText = totalC11;
		document.getElementById("totalC02_diff").innerText = totalC02;
		
		const countCourse = totalC11 - totalC02; 
		document.getElementById("countCourse").innerText = countCourse;
	}	 
	catch (error) 
	{
		console.error("Error fetching CSV:", error);
		document.getElementById("error").innerText = "Failed to load data.";
	}
}

// This function returns the amount of data for each semester and its modality.
function modalityTerm(data, term, modality) {
	return data.filter(row => row.Term === term && row.Modality === modality);
}

// Function to filter by Term, Modality, and Course Code
function modalityTermCourse(data, term, modality, courseCode) {
    return data.filter(row => row.Term === term && row.Modality === modality && 
		row.Course === courseCode);
}

// Function to filter by Term and Course Code
function modalityCourse(data, term, courseCode) {
    return data.filter(row => row.Term === term && row.Course === courseCode);
}

// Function to filter by Term and Days
function modalityTermDays(data, term, days) {
    return data.filter(row => row.Term === term && row.Days === days);
}

// Function to filter by Term
function showCourseTerm(data, term) {
    return data.filter(row => row.Term === term);
}

// Function to create the pie chart
function createPieChart(canvasId, title, modalityCounts) 
{
    const ctx = document.getElementById(canvasId).getContext('2d');
    
	// Calculate the total count of courses
    const totalCourses = modalityCounts.reduce((total, count) => total + count, 0);
	
    // Creating the Pie Chart with Chart.js
    new Chart(ctx, 
	{
        type: 'pie',
        data: {
            labels: ['Hybrid', 'Presencial', 'Distance'],
            datasets: [{
                label: title,
                data: modalityCounts, 
                backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)', 
					'rgba(255, 159, 64, 0.6)'], 
                borderColor: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 
					'rgba(255, 159, 64, 1)'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            const count = tooltipItem.raw;
							const percentage = ((count / totalCourses) * 100).toFixed(2);
                            return `${count} courses (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

// Function to create the bar chart
function createChart(coursesCount) 
{	
	const ctx = document.getElementById('courseChart').getContext('2d');
	
	// Creating the chart with Chart.js
	new Chart(ctx, 
	{
		type: 'bar',
		data: {
			labels: ['C22', 'C12', 'C11', 'C03', 'C02'], // Labels for the x-axis
			datasets: [{
				label: 'Amount of Courses', 
				data: coursesCount, 
				backgroundColor: 'rgba(75, 192, 192, 0.2)', 
				borderColor: 'rgba(75, 192, 192, 1)', 
				borderWidth: 1
			}]
		},
		options: {
			responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Term'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Amount of Courses'
                    }
                }
            }		
		}
	});
}

// Automatically call the method filterData() when the page loads.
document.addEventListener("DOMContentLoaded", filterData); 
