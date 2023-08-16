# Email Formatter

A quick Python script to take the submissions from the Giao Ly registration form and format
them in a way to create new Microsoft 365 accounts.

## Running the Project

### Setting Up Environment
First clone the repository or download the files for this project. You will then need to install 
the necessary Python packages: `pip install -r requirements.txt`

### Getting Started
1. Download the submissions from the Giao Ly registration form as a CSV file. If you're creating your 
own CSV file from scratch, then you will need these headers for this script:

```csv
First Name,Middle Name (N/A if you don't have one),Last Name
```

2. Rename the file as `{DATE}-emails.csv` and place the file in the `input` folder.

3. Inside the Python script, change the `DATE` constant to match the date you set on the CSV file. 

4. If you are creating emails for students, change `IS_STUDENT` to `True` which will give emails in 
the format of `username@student.vmpwa.org`; otherwise, leaving `IS_STUDENT` as `False` will give 
emails in the format of `username@school.vmpwa.org`.

5. Optionally, change `DEPARTMENT` to match whatever department you're creating emails for, e.g. 
`Viet Ngu` or `Giao Ly` (these are what's currently set in our Microsoft 365 admin center). Although
not necessary for creating emails, this helps organize the emails in our organization.

6. Run the Python script and you should see the formatted CSV file in the `output` folder.

7. Upload the outputted CSV file to [Microsoft 365](https://admin.microsoft.com/#/homepage) -> 
**Users | Active Users | Add multiple Users | I'd like to upload a CSV with user information**.