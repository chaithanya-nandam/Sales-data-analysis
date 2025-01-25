# Sales-data-analysis
This project performs a comprehensive analysis of sales data using Python. The analysis includes visualizing monthly sales trends and identifying the top-selling products. The data is stored in a CSV file, which is read and processed using the Pandas library. Visualizations are created using Matplotlib and Seaborn.

## Technologies Used

- **Python**: The programming language used for data analysis.
- **Pandas**: A powerful data manipulation and analysis library for Python.
- **Matplotlib**: A plotting library for creating static, animated, and interactive visualizations.
- **Seaborn**: A statistical data visualization library based on Matplotlib.
- **CSV**: The data format used to store sales data.
### Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)

Install the required libraries using pip:

pip install pandas matplotlib seaborn
Data
The sales data is stored in a CSV file named sales_data.csv. The file contains the following columns:

Order Date: The date of the sale (format: YYYY-MM-DD).

Product Name: The name of the product sold.

Sales: The total sales amount for the product.

Running the Analysis
To run the analysis, execute the following command in your terminal or command prompt:
python sales_analysis.py
Output
The script will generate the following visualizations:

Monthly Sales Trend: A line plot showing the total sales for each month.
Top 10 Selling Products: A bar chart displaying the top-selling products based on total sales.
Example Data
Here is an example of the data format used in sales_data.csv:
Order Date,Product Name,Sales
2024-01-15,tshirt,200
2024-01-20,shirts,150
2024-02-10,kurtas,300
2024-02-15,ethnic kurtas,400
2024-03-05,men jeans,250
2024-03-10,women jeans,500
2024-04-01,women trousers,600
2024-04-15,kids tshirt,700
2024-05-20,Smartwatch,800
2024-05-25,home decore,900
