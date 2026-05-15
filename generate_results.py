"""
School Result Card Generator
Generates professional PDF result cards from CSV data
"""

import csv
import os
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import pandas as pd

# Configuration
SCHOOL_NAME = "R.K. ACADEMY"
SCHOOL_ADDRESS = "DHARMPUR BHITAULI MAHARAJGANJ"
SCHOOL_PHONE = "91-7308162120"
SCHOOL_EMAIL = "rkaacademy@gmail.com"
AFFILIATION_NO = "0105-1"

# Grading Scale
GRADE_SCALE = {
    (91, 100): 'A1',
    (81, 90): 'A2',
    (71, 80): 'B1',
    (61, 70): 'B2',
    (51, 60): 'C1',
    (41, 50): 'C2',
    (33, 40): 'D',
    (0, 32): 'E (Fail)'
}

def get_grade(marks):
    """Calculate grade based on marks"""
    for (low, high), grade in GRADE_SCALE.items():
        if low <= marks <= high:
            return grade
    return 'E (Fail)'

def generate_result_card(student_data, output_folder='output'):
    """Generate PDF result card for a student"""
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract data
    name = student_data['Student Name']
    father_name = student_data.get('Father Name', 'N/A')
    mother_name = student_data.get('Mother Name', 'N/A')
    class_name = student_data.get('Class', 'N/A')
    roll_no = student_data.get('Roll No', 'N/A')
    
    # Create PDF
    filename = f"{output_folder}/{name.replace(' ', '_')}_ResultCard.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Title Style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1a1a4d'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#333333'),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    
    # Header
    elements.append(Paragraph(SCHOOL_NAME, title_style))
    elements.append(Paragraph(SCHOOL_ADDRESS, subtitle_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Student Info
    info_data = [
        ['Scholar\'s Name', name, '', 'Affiliation No.', AFFILIATION_NO],
        ['Mother\'s Name', mother_name, '', 'Phone No.', SCHOOL_PHONE],
        ['Father\'s Name', father_name, '', 'Email', SCHOOL_EMAIL],
        ['Class', class_name, '', 'Roll No.', roll_no],
    ]
    
    info_table = Table(info_data, colWidths=[1.5*inch, 2*inch, 0.5*inch, 1.5*inch, 1.5*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8e8f0')),
        ('BACKGROUND', (3, 0), (3, -1), colors.HexColor('#e8e8f0')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (3, 0), (3, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    elements.append(info_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # Marks Table Header
    elements.append(Paragraph("Academic Performance 2025-26", styles['Heading3']))
    elements.append(Spacer(1, 0.1*inch))
    
    # Extract marks
    subjects = ['Hindi1', 'Hindi2', 'English1', 'English2', 'Math', 'Science', 'SST', 'GK', 'Drawing', 'Computer']
    
    marks_data = [['S.No.', 'Subject', 'Unit Test 1', 'Half Yearly', 'Unit Test 2', 'Annual', 'Total', 'Grade']]
    
    total_marks = 0
    total_max_marks = 0
    
    for idx, subject in enumerate(subjects, 1):
        if subject in student_data:
            mark = float(student_data[subject])
            grade = get_grade(mark)
            total_marks += mark
            total_max_marks += 100
            
            marks_data.append([
                str(idx),
                subject.replace('1', ' I').replace('2', ' II'),
                str(mark),
                str(mark),
                str(mark),
                str(mark),
                str(int(mark * 1.5)),
                grade
            ])
    
    # Calculate percentage
    percentage = (total_marks / total_max_marks * 100) if total_max_marks > 0 else 0
    overall_grade = get_grade(percentage)
    
    marks_data.append(['', 'TOTAL', '', '', '', '', str(int(total_marks)), overall_grade])
    
    marks_table = Table(marks_data, colWidths=[0.6*inch, 1.2*inch, 0.9*inch, 1*inch, 0.9*inch, 0.9*inch, 0.7*inch, 0.7*inch])
    marks_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#8b7355')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))
    
    elements.append(marks_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # Summary
    summary_data = [
        ['Percentage of Marks', f'{percentage:.2f}%'],
        ['Overall Grade', overall_grade],
        ['Promoted To Class', 'Next Class' if percentage >= 50 else 'Repeat'],
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 3*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8e8f0')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    
    elements.append(summary_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Signatures
    sig_data = [['Class Teacher\'s Sign.', 'Date: Jun, 20 2026', 'Principal\'s Sign.']]
    sig_table = Table(sig_data, colWidths=[2*inch, 2*inch, 2*inch])
    sig_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 40),
    ]))
    
    elements.append(sig_table)
    
    # Build PDF
    doc.build(elements)
    print(f"✅ Created: {filename}")

def main(csv_file):
    """Main function to process CSV and generate PDFs"""
    
    try:
        df = pd.read_csv(csv_file)
        
        print(f"\n📊 Processing {len(df)} students from {csv_file}...\n")
        
        for idx, row in df.iterrows():
            student_dict = row.to_dict()
            generate_result_card(student_dict)
        
        print(f"\n✨ All {len(df)} result cards generated successfully!")
        print("📁 Check 'output' folder for PDF files\n")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{csv_file}' not found")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = "sample_data.csv"
    
    main(csv_file)
