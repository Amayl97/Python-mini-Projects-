# 🎓 Scholarship Dataset Manager

A small Python project that started with a simple question:

> *"What if scholarship data didn't have to be a giant, terrifying spreadsheet?"* 😭

So, I built a little **Scholarship Dataset Manager** using **Python + Pandas** to practice working with real-world-style tabular data.

The project can read scholarship data from CSV, search and filter it, sort it, modify records, calculate statistics, and export the data to JSON.

Nothing fancy. Just me making Pandas do the paperwork. 🐼

---

## ✨ Features

The Scholarship Dataset Manager currently supports:

* 📂 Read scholarship data from CSV
* 🔎 Search scholarships by name, country, degree, or field
* 🎯 Filter scholarships based on specific criteria
* ↕️ Sort scholarships by different columns
* ➕ Add new scholarships
* ✏️ Update existing scholarship information
* 🗑️ Delete scholarships
* 📊 Generate basic dataset statistics
* 💾 Save updated data back to CSV
* 📦 Export scholarship data to JSON

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **CSV**
* **JSON**

No giant frameworks. No mysterious black boxes.

Just Python doing its thing. 🐍

---

## 📁 Project Structure

```text
ScholarshipDatasetManager/
│
├── data/
│   ├── scholarships.csv
│   ├── cleaned_scholarships.csv
│   └── scholarships.json
│
├── modules/
│   ├── search.py
│   ├── filter.py
│   ├── sort.py
│   ├── add.py
│   ├── delete.py
│   ├── update.py
│   ├── statistics.py
│   └── exporter.py
│
├── main.py
├── .gitignore
└── README.md
```

Each feature lives in its own module so the project doesn't turn into one enormous `main.py` file of doom. 🫠

---

## 🧠 What I Learned

This project was built as a hands-on way to practice **Pandas and Python**, rather than just watching tutorials and hoping knowledge magically appears.

### Python

* Functions
* Modules
* Imports
* Dictionaries
* Conditional statements
* User input
* Basic error handling

### Pandas

* Creating and working with DataFrames
* Reading CSV files with `read_csv()`
* Filtering rows
* Searching with `str.contains()`
* Sorting with `sort_values()`
* Updating rows with `loc`
* Adding rows
* Deleting rows
* Calculating statistics with methods such as `mean()`
* Counting values with `value_counts()`
* Exporting DataFrames

### Data Formats

* CSV
* JSON

---

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Move into the project

```bash
cd ScholarshipDatasetManager
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run the program

```bash
python main.py
```

---

## 🎯 Why I Built This

This isn't meant to be a production scholarship platform.

It's a **learning project**.

The goal was to take what I had learned about Python and Pandas and actually build something instead of collecting another tutorial under the extremely large pile of:

> *"I'll build this someday."* 😭

The scholarship theme was chosen because it also connects to a larger project I'm working toward: building systems that can help students discover and understand scholarship opportunities.

---

## 🔮 What's Next?

This project is intentionally small, but it could eventually evolve into something more interesting:

* 🌐 Collect scholarship data from websites
* 🤖 Automatically clean scraped data
* 🔍 More advanced scholarship matching
* 🗄️ Store scholarships in a database
* 🌐 Build an API
* 🧠 Add AI-powered scholarship recommendations

For now, though...

**one DataFrame at a time.** 🐼
