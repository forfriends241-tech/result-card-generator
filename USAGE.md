# 📖 Usage Guide - Result Card Generator

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/forfriends241-tech/result-card-generator.git
cd result-card-generator
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- `reportlab` - PDF generation
- `pandas` - CSV processing
- `pillow` - Image handling

## Quick Start

### Generate Result Cards
```bash
python generate_results.py sample_data.csv
```

This will:
1. Read student data from `sample_data.csv`
2. Generate professional PDF result cards
3. Save all PDFs in `output/` folder

### Output Example
```
output/
├── Aman_Sahni_ResultCard.pdf
├── Priya_Singh_ResultCard.pdf
├── Rohan_Kumar_ResultCard.pdf
├── Neha_Sharma_ResultCard.pdf
└── Arjun_Patel_ResultCard.pdf
```

---

## CSV Data Format

### Column Headers Required:
```
Student Name, Father Name, Mother Name, Class, Roll No, 
Hindi1, Hindi2, English1, English2, Math, Science, SST, GK, Drawing, Computer
```

### Example:
```csv
Student Name,Father Name,Mother Name,Class,Roll No,Hindi1,Hindi2,English1,English2,Math,Science,SST,GK,Drawing,Computer
Aman Sahni,Mr. Niscala,Mrs. Rita devi,8th A,15,25,24,25,24,25,25,25,25,25,25
Priya Singh,Mr. Rajesh Singh,Mrs. Anjali Singh,8th A,8,24,23,23,22,24,23,24,22,23,24
```

### Notes:
- All marks should be out of 25
- Student Name is required
- Roll No should be unique

---

## Customization

### Edit School Details
Open `generate_results.py` and modify:
```python
SCHOOL_NAME = "Your School Name"
SCHOOL_ADDRESS = "Your School Address"
SCHOOL_PHONE = "Your Phone Number"
SCHOOL_EMAIL = "Your Email"
```

### Modify Grading Scale
```python
GRADE_SCALE = {
    (91, 100): 'A1',
    (81, 90): 'A2',
    (71, 80): 'B1',
    # ... add/modify as needed
}
```

---

## Features

✅ **Bulk PDF Generation** - Generate multiple PDFs at once  
✅ **Automatic Calculations** - Total, percentage, grade  
✅ **Professional Layout** - School header, marks table, signatures  
✅ **CSV Import** - Easy data import from spreadsheet  
✅ **Customizable** - School details, grading scale  
✅ **Error Handling** - Proper error messages  

---

## Troubleshooting

### Error: "FileNotFoundError: sample_data.csv not found"
**Solution:** Make sure CSV file is in the same directory as the script
```bash
python generate_results.py /path/to/your/data.csv
```

### Error: "ModuleNotFoundError: No module named 'reportlab'"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### PDFs not generated
**Solution:** Check if `output/` folder was created and PDFs are there
```bash
ls output/
```

---

## Advanced Usage

### Generate from Different CSV
```bash
python generate_results.py students_2025.csv
```

### Custom Output Folder
Edit `generate_results.py`:
```python
generate_result_card(student_dict, output_folder='my_results')
```

---

## File Structure

```
result-card-generator/
├── README.md
├── USAGE.md
├── generate_results.py      # Main script
├── requirements.txt         # Dependencies
├── sample_data.csv         # Sample data
├── .gitignore              # Git ignore rules
└── output/                 # Generated PDFs
    ├── Aman_Sahni_ResultCard.pdf
    └── ...
```

---

## PDF Features

Each PDF includes:
- School header with details
- Student information (Name, Father, Mother, Class, Roll No)
- Academic performance table with:
  - Subject names
  - Unit Test 1 marks
  - Half Yearly marks
  - Unit Test 2 marks
  - Annual marks
  - Total and Grade
- Overall percentage and grade
- Promotion status
- Signature spaces for teacher and principal

---

## Grading Scale (Default)

| Marks | Grade |
|-------|-------|
| 91-100 | A1 |
| 81-90 | A2 |
| 71-80 | B1 |
| 61-70 | B2 |
| 51-60 | C1 |
| 41-50 | C2 |
| 33-40 | D |
| 0-32 | E (Fail) |

---

## Support

For issues or questions:
1. Check this USAGE.md file
2. Review the code comments in `generate_results.py`
3. Create an issue on GitHub
4. Check sample_data.csv format

---

## License

MIT License - See repository for details

---

**Happy Generating! 🎓📝**
