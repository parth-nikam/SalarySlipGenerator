# Salary Slip Generator using Python, MySQL

This is a Python application that generates salary slips in PDF format using data from a CSV file and MySQL database. It is designed to handle the generation of multiple salary slips simultaneously and efficiently.

## Installation

1. Clone the repository using the command:

```
git clone https://github.com/parth-nikam/SalarySlipGenerator.git
```

2. Install the required packages using the command:

```
pip install -r requirements.txt
```
3. Set up the MySQL database with the required tables using the `salary_slip_db.sql` script provided in the repository.

4. Update the database configuration details in the `config.py` file.

## Usage

1. Place the CSV file containing the employee data in the `data` directory.

2. Run the following command to generate salary slips:

```
python generate_salary_slips.py
```

3. The generated salary slips will be saved in the `output` directory.

## Simulation Video

Check out this simulation video to see how the salary slip generator works:

[![Salary Slip Generator Simulation](https://user-images.githubusercontent.com/87958912/235339879-5979e407-4d29-4097-8cb8-6a12f9c03945.png)](https://user-images.githubusercontent.com/87958912/235339762-553aa88e-caa4-4aeb-aea6-b67a1c986000.mp4)

## Credits

This application was created by [Parth Nikam](https://github.com/parth-nikam). It uses the following technologies:

- [Python](https://www.python.org/)
- [MySQL](https://www.mysql.com/)
- [pandas](https://pandas.pydata.org/)
- [PyMySQL](https://github.com/PyMySQL/PyMySQL)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)
- [ReportLab](https://www.reportlab.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
