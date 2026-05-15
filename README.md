# 📊 School Result Card Generator

Generate professional student result cards in PDF format from CSV data.

## Features

✅ Generate multiple PDFs at once  
✅ Auto-calculate totals, percentages, grades  
✅ Professional school header layout  
✅ Bulk import from CSV  
✅ Customizable school details  
✅ Automatic grading scale  

## Quick Start

### 1. Install
```bash
pip install -r requirements.txt
```

### 2. Prepare Data (CSV format)
- See `sample_data.csv` for format
- Add your students' data

### 3. Generate PDFs
```bash
python generate_results.py sample_data.csv
```

### 4. Check Output
- All PDFs in `output/` folder

## CSV Format

```
Student Name,Father Name,Mother Name,Class,Roll No,Hindi1,Hindi2,English1,English2,Math,Science,SST,GK,Drawing,Computer
Aman Sahni,Mr. Niscala,Mrs. Rita devi,8th A,15,25,24,25,24,25,25,25,25,25,25
```

## Customize School Details

Edit `config.py`:
- School name, address, phone
- Logo path
- Grading scale
- Header colors

## Requirements

- Python 3.7+
- reportlab
- pandas
- pillow

## License

MIT
