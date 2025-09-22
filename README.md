# Discipline Management CRUD 📝

## Overview
This project is a **console-based CRUD application** for managing academic disciplines using **Python** and **MySQL**. Users can create, read, update, and delete records for disciplines, including their code, name, and workload hours. The project also displays records in a formatted table using the **PrettyTable** library.

---

## Features
- **Create (Insert)**: Add new disciplines with code, name, and workload.  
- **Read (Select)**: View all disciplines in a formatted table.  
- **Update (Edit)**: Modify existing discipline details.  
- **Delete (Remove)**: Remove disciplines from the database.  
- **Console Interface**: Interactive menu-driven interface for easy navigation.  

---

## Database Schema
```sql
CREATE TABLE tb_dis (
    idt_dis INT AUTO_INCREMENT PRIMARY KEY,
    sgl_dis VARCHAR(10) NOT NULL,
    nme_dis VARCHAR(50) NOT NULL,
    num_ch_dis INT NOT NULL
);
````

**Field Descriptions:**

* `sgl_dis`: Discipline code (e.g., "MAT101")
* `nme_dis`: Discipline name
* `num_ch_dis`: Workload hours

---

## Technologies Used

* **Python** (3.x)
* **MySQL**
* **PrettyTable** for tabular display
* **mysql-connector-python** for database interaction

---

## How to Run

1. Install required Python packages:

   ```bash
   pip install mysql-connector-python prettytable
   ```
2. Configure your MySQL connection in the script:

   ```python
   cnx = mysql.connector.connect(
       user='your_username', 
       password='your_password', 
       host='your_host', 
       database='your_database'
   )
   ```
3. Run the Python script:

   ```bash
   python your_script_name.py
   ```
4. Use the console menu to **Insert, Read, Update, Delete** disciplines.

---

## Contributors

* Arthur Arash Briceño Heidari

---

## License

MIT License


If you want, I can also create a **short, résumé-friendly version** describing this CRUD project for your CV, perfect for your “Projects” section. Do you want me to do that?
```
