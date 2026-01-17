import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# nltk.download('punkt')
nltk.data.path.append('nltk_data')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

csv_data = """Qualifications,category,Fields,Job Titles,Interests,Skills,Goals
12th,law,Lawyer(advocate) with LLB Degree,,"Justice, Legal Rights, Courtroom Advocacy, Legal Research","Argumentation, Communication, Critical Thinking, Research, Persuasion",I want to become a successful Lawyer.
12th,Law,Judge with LLB Degree,,"Law Interpretation, Justice Delivery, Legal Ethics, Decision-making","Legal Knowledge, Impartiality, Analytical Reasoning, Patience, Integrity","I want to become a Judge, lawyer."
12th,Law,Corporate Lawyer with LLB Degree,,"Business Law, Mergers & Acquisitions, Company Regulations","Commercial Awareness, Negotiation, Contract Drafting, Problem-solving, Communication","I want to become a successful lawyer, Corporate Lawyer "
12th,Law,Criminal Lawyer with LLB Degree,,"Crime Cases, Criminal Justice, Defense and Prosecution","Investigation, Argumentation, Analytical Skills, Communication, Resilience",I want to become a Criminal Lawyer.
12th,Engineering,Computer Science and Engineering with BE/B-TECH,,"Web Development, Software Development, Frontend Development, Full stack development, Artificial Intelligence, Machine Learning, Data science, Cyber Security, Data Analytics, cloud Computing.","C, C++, Java, Python, JavaScript, Data structures and algorithms, Database management system, operating systems, Cloud computing, Blockchain Development.","I want to become a successful software developer, software engineer, web developer, Frontend developer, backend developer, full stack developer."
12th,Engineering,Mechanical Engineering with BE/B-TECH,,"Interest in machines, Cars, Engines, Product Design, Automobiles, 3D printing and prototyping, Industrial automation and robotics, Product innovation and design.","Mathematics and Physics, AutoCAD, Engineering fundamentals, Thermodynamics, Fluid Mechanics, Material Science, Manufacturing Processes, Robotics, Problem Solving, HIVAC Systems, Finite Element Analysis,",I want to become a successful
12th,Engineering,Civil Engineering with BE/B-TECH,,"Passion for building structures, Urban development, environmental sustainability, Designing eco-friendly cities, skyscraper and mega-structure projects, Green building technology, Bridge architecture and design.","Structural Analysis, AutoCAD, Construction Management, Surveying, Estimation and costing, Geotechnical Engineering, Building Information Modelling, Urban Planning, Soil Mechanics, Transportation Engineering, Environmental Engineering.","I want to become a successful Lawyer"
12th,Engineering,Electrical Engineering with BE/B-TECH,,"Power Systems, Electrical Machines, Electric innovation, Power generation, Energy conservation, Smart grids, Electronics, Electric vehicles and motors, Power transmission.","Power systems, Electrical Machines, Control systems, Circuit Theory, MATLAB/Simulink, Renewable, Energy, Electronics, Smart Grids Technology, SCADA Systems, High voltage Engineering, Energy Storage Systems.","I want to become a successful Lawyer"
12th,Engineering,Electronics and Telecommunication Engineering with BE/B-TECH,,"Fascination with gadgets, Electronics, Wireless systems, Building Circuits, Internet of Things, Mobile Communication, Embedded Systems, Smart devices and home automation, radio technology, Satellite communication, Tech gadgets teardown, Electronics DIY projects.","Circuit Design, Embedded Systems, VLSI Design, Communication Systems, Signal, Processing, Programming(Verilog, C), PCB Designing, Internet of Things, FPGA Programming, Wireless Communication Protocols, Artificial Neural Networks.",I want to become a successful Lawyer
12th,Engineering,Mining Engineering with BE/B-TECH,,"Interest in Natural resources, Mining technology, Earth science, Environmental impact of mining, Exploring remote areas for resources, Sustainable mining practices, Metallurgy and mineral processing, Geological field work.","Rock Mechanics, Mine Surveying, Mineral Processing, Safety Management, Environmental Engineering, Geology, Mine planning and Design, Drilling and Blasting Techniques, Mineral Economics, Underground and Surface mining techniques, Mine Health and Safety.","I want to become a successful Lawyer"
12th,Medical,MBBS,,"Healthcare, Problem-solving, Surgery, Diagnosis, Medicine","Anatomy, Communication, Critical thinking, Decision-making, Stress Management",I want to become a successful Lawyer
12th,Medical,Dentist with BDS,,"Oral, Hygiene, Procedures, Dentistry, Technology","Manual dexterity, Communication, Diagnosis, Anatomy, Patient care",I want to become a successful Lawyer
12th,Medical,BHMS,,"Alternative medicine, Holistic health, Natural remedies, Patient care","Diagnosis, Homeopathy, Research, Empathy, Analytical skills",I want to become a successful Lawyer
12th,Medical,Pharmacy with B-phram/D-Phram,,"Pharmaceuticals, Drug formulation, Medication, Patient health","Pharmacology, chemistry, Accuracy, Organization, Counseling",I want to become a successful Lawyer
12th,Medical,Gynaecologist with MBBS,,"Reproductive health, Pregnancy, Childbirth, Women's health","Obstetrics, Surgery, Communication, Diagnosis, Patient care",I want to become a successful Lawyer
Graduation,Law,Lawyer(advocate) with LL.M Degree,"Advocate, Legal Advisor, Legal Consultant, Public Prosecutor, Corporate Lawyer, Criminal Lawyer, Civil Lawyer, Tax Lawyer, Family Lawyer, Intellectual Property Lawyer, Litigation Associate, Legal Officer, Legal Analyst, Legal Counsel, Solicitor, Notary","Justice, Legal Rights, Courtroom Advocacy, Legal Research","Argumentation, Communication, Critical Thinking, Research, Persuasion",I want to become a successful Lawyer
Graduation,Law,Judge with LL.M Degree,"Judge, Magistrate, District Judge, Sessions Judge, Chief Justice, High Court Judge, Supreme Court Judge, Tribunal Judge, Judicial Officer, Legal Advisor, Court Registrar, Judicial Clerk, Law Secretary, Public Prosecutor, Legal Consultant","Law Interpretation, Justice Delivery, Legal Ethics, Decision-making","Legal Knowledge, Impartiality, Analytical Reasoning, Patience, Integrity",I want to become a successful Lawyer
Graduation,Law,Corporate Lawyer with LL.M Degree,"Corporate Lawyer, Legal Advisor, Legal Counsel, Corporate Counsel, In-House Counsel, Compliance Officer, Legal Manager, Contract Manager, Mergers and Acquisitions Lawyer, Regulatory Counsel, Legal Associate, General Counsel, Risk Manager, Legal Consultant, Company Secretary","Business Law, Mergers & Acquisitions, Company Regulations","Commercial Awareness, Negotiation, Contract Drafting, Problem-solving, Communication",I want to become a successful Lawyer
Graduation,Law,Criminal Lawyer with LL.M Degree,"Criminal Lawyer, Defense Attorney, Public Prosecutor, Legal Advisor (Criminal Law), Criminal Defense Counsel, Assistant District Attorney, Legal Consultant (Criminal), Trial Lawyer, Litigation Attorney, Legal Associate (Criminal), Criminal Law Advocate, Prosecuting Attorney, Public Defender","Crime Cases, Criminal Justice, Defense and Prosecution","Investigation, Argumentation, Analytical Skills, Communication, Resilience",I want to become a successful Lawyer
Graduation,Law,Family Lawyer with LL.M Degree,"Family Lawyer, Divorce Attorney, Child Custody Lawyer, Legal Advisor (Family Law), Mediation Lawyer, Family Law Advocate, Legal Consultant (Family Matters), Adoption Lawyer, Domestic Violence Attorney, Guardianship Lawyer, Alimony Specialist, Family Court Attorney","Marriage Law, Divorce Cases, Child Custody, Family Disputes","Mediation, Counseling, Negotiation, Patience, Emotional Intelligence",I want to become a successful Lawyer
Graduation,Engineering,Computer Science and Engineering with ME/M-TECH,"Software Engineer, Full Stack Developer, Backend Developer, Frontend Developer, Data Scientist, Machine Learning Engineer, AI Engineer, DevOps Engineer, Systems Analyst, Cloud Engineer, Cybersecurity Analyst, Database Administrator, Network Engineer, Mobile App Developer, Web Developer, Embedded Systems Engineer, Game Developer, QA Engineer, IT Consultant, Research Scientist","Web Development, Software Development, Frontend Development, Full stack development, Artificial Intelligence, Machine Learning, Data science, Cyber Security, Data Analytics, cloud Computing.","C, C++, Java, Python, JavaScript, Data structures and algorithms, Database management system, operating systems, Cloud computing, Blockchain Development."
Graduation,Engineering,Mechanical Engineering with ME/M-TECH,"Mechanical Engineer, Design Engineer, Maintenance Engineer, Production Engineer, Quality Engineer, HVAC Engineer, Automotive Engineer, Aerospace Engineer, Thermal Engineer, Manufacturing Engineer, Project Engineer, R&D Engineer, Mechatronics Engineer, CAD Engineer, Robotics Engineer, Plant Engineer, Tooling Engineer, Marine Engineer","Interest in machines, Cars, Engines, Product Design, Automobiles, 3D printing and prototyping, Industrial automation and robotics, Product innovation and design.","Mathematics and Physics, AutoCAD, Engineering fundamentals, Thermodynamics, Fluid Mechanics, Material Science, Manufacturing Processes, Robotics, Problem Solving, HIVAC Systems, Finite Element Analysis, Energy Systems, Mechatronics."
Graduation,Engineering,Civil Engineering with ME/M-TECH,"Civil Engineer, Site Engineer, Structural Engineer, Project Engineer, Construction Manager, Geotechnical Engineer, Transportation Engineer, Environmental Engineer, Surveyor, Design Engineer, Planning Engineer, Quantity Surveyor, Water Resources Engineer, Urban Planner, Highway Engineer, Building Inspector, Estimation Engineer","Passion for building structures, Urban development, environmental sustainability, Designing eco-friendly cities, skyscraper and mega-structure projects, Green building technology, Bridge architecture and design.","Structural Analysis, AutoCAD, Construction Management, Surveying, Estimation and costing, Geotechnical Engineering, Building Information Modelling, Urban Planning, Soil Mechanics, Transportation Engineering, Environmental Engineering."
Graduation,Engineering,Electrical Engineering with ME/M-TECH,"Electrical Engineer, Power Systems Engineer, Control Systems Engineer, Design Engineer, Electronics Engineer, Instrumentation Engineer, Maintenance Engineer, Project Engineer, Circuit Design Engineer, Test Engineer, Embedded Systems Engineer, Automation Engineer, Energy Consultant, Hardware Engineer, Substation Engineer, Electrical Site Engineer","Power Systems, Electrical Machines, Electric innovation, Power generation, Energy conservation, Smart grids, Electronics, Electric vehicles and motors, Power transmission.","Power systems, Electrical Machines, Control systems, Circuit Theory, MATLAB/Simulink, Renewable, Energy, Electronics, Smart Grids Technology, SCADA Systems, High voltage Engineering, Energy Storage Systems."
Graduation,Engineering,Electronics and Telecommunication Engineering with ME/M-TECH,"Electronics Engineer, Telecommunication Engineer, Network Engineer, RF Engineer, Embedded Systems Engineer, Signal Processing Engineer, VLSI Engineer, IoT Engineer, Hardware Design Engineer, Systems Engineer, Satellite Communication Engineer, Wireless Communication Engineer, Optical Fiber Engineer, Test Engineer, PCB Design Engineer, Telecom Analyst","Fascination with gadgets, Electronics, Wireless systems, Building Circuits, Internet of Things, Mobile Communication, Embedded Systems, Smart devices and home automation, radio technology, Satellite communication, Tech gadgets teardown, Electronics DIY projects.","Circuit Design, Embedded Systems, VLSI Design, Communication Systems, Signal, Processing, Programming(Verilog, C), PCB Designing, Internet of Things, FPGA Programming, Wireless Communication Protocols, Artificial Neural Networks."
Graduation,Engineering,Mining Engineering with ME/M-TECH,"Mining Engineer, Mine Planner, Mine Surveyor, Drilling Engineer, Blasting Engineer, Ventilation Engineer, Safety Officer, Mineral Processing Engineer, Geotechnical Engineer, Quarry Manager, Exploration Geologist, Mine Manager, Underground Mining Engineer, Surface Mining Engineer, Environmental Engineer (Mining), Mining Consultant","Interest in Natural resources, Mining technology, Earth science, Environmental impact of mining, Exploring remote areas for resources, Sustainable mining practices, Metallurgy and mineral processing, Geological field work.","Rock Mechanics, Mine Surveying, Mineral Processing, Safety Management, Environmental Engineering, Geology, Mine planning and Design, Drilling and Blasting Techniques, Mineral Economics, Underground and Surface mining techniques, Mine Health and Safety."
Graduation,Medical,MBBS,"Doctor, General Practitioner, Surgeon, Pediatrician, Cardiologist, Dermatologist, Neurologist, Psychiatrist, Orthopedic Surgeon, Obstetrician, Gynecologist, Anesthesiologist, Ophthalmologist, ENT Specialist, Radiologist, Pathologist, Emergency Medicine Specialist, Family Physician, Medical Consultant","Healthcare, Problem-solving, Surgery, Diagnosis, Medicine","Anatomy, Communication, Critical thinking, Decision-making, Stress Management"
Graduation,Medical,Dentist with BDS,"Dentist, Orthodontist, Periodontist, Endodontist, Oral Surgeon, Pediatric Dentist, Prosthodontist, Dental Hygienist, Dental Assistant, Dental Technician, Cosmetic Dentist, Implantologist, Maxillofacial Surgeon, Forensic Dentist, Public Health Dentist","Oral, Hygiene, Procedures, Dentistry, Technology","Manual dexterity, Communication, Diagnosis, Anatomy, Patient care"
Graduation,Medical,BHMS,"Homeopathic Physician, Clinical Homeopath, Pediatric Homeopath, Dermatology Homeopath, Obstetrics Homeopath, Homeopathic Consultant, Researcher (Homeopathy), Educator (Homeopathy), Hospital Homeopath, Public Health Homeopath, Homeopathic Pharmacist, Wellness Coach, Integrative Medicine Specialist, Homeopathic Practitioner, Telemedicine Homeopath","Alternative medicine, Holistic health, Natural remedies, Patient care","Diagnosis, Homeopathy, Research, Empathy, Analytical skills"
Graduation,Medical,Pharmacy with M-phram,"Pharmacist, Clinical Pharmacist, Pharmaceutical Researcher, Drug Safety Associate, Pharmacy Manager, Regulatory Affairs Specialist, Medicinal Chemist, Pharmaceutical Sales Representative, Pharmacy Technician, Clinical Research Associate","Pharmaceuticals, Drug formulation, Medication, Patient health","Pharmacology, chemistry, Accuracy, Organization, Counseling"
Graduation,Medical,Gynaecologist with MBBS,"Gynecologist, Obstetrician-Gynecologist, Reproductive Endocrinologist, Maternal-Fetal Medicine Specialist, Gynecologic Oncologist, Urogynecologist, Minimally Invasive Gynecologic Surgeon, Infertility Specialist, Perinatologist, Women’s Health Specialist, Academic Gynecologist, Clinical Researcher (Ob/Gyn), Nurse Practitioner (Ob/Gyn), Physician Assistant (Ob/Gyn)","Reproductive health, Pregnancy, Childbirth, Women's health","Obstetrics, Surgery, Communication, Diagnosis, Patient care"
"""

stop_words = set(stopwords.words('english'))
punctuations = set(string.punctuation)

def preprocess_text(text):
    if not text or text.lower() == "nan":
        return set()
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words and t not in punctuations and len(t) > 1]
    return set(tokens)

def parse_csv_data(csv_text):
    lines = csv_text.strip().splitlines()
    reader = csv.DictReader(lines)
    data_list = []
    for row in reader:
        # Strip keys to avoid spaces causing issues
        row = {k.strip(): v.strip() if isinstance(v, str) else v for k, v in row.items()}
        row['qualifications_tokens'] = preprocess_text(row.get('Qualifications', ''))
        row['Skills_tokens'] = preprocess_text(row.get('Skills', ''))
        row['Interests_tokens'] = preprocess_text(row.get('Interests', ''))
        row['Goals_tokens'] = preprocess_text(row.get('Goals', ''))
        data_list.append(row)
    return data_list

def jaccard_similarity(set1, set2):
    if not set1 and not set2:
        return 1.0
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return float(len(intersection)) / len(union)

def suggest_job(user_qualifications, user_skills, user_interests, user_goals, data):
    user_qualifications_tokens = preprocess_text(user_qualifications)
    user_skills_tokens = preprocess_text(user_skills)
    user_interests_tokens = preprocess_text(user_interests)
    user_goals_tokens = preprocess_text(user_goals)

    best_score = -1.0
    best_row = None

    for row in data:
        sim_qualifications = jaccard_similarity(user_qualifications_tokens, row['qualifications_tokens'])
        sim_skills = jaccard_similarity(user_skills_tokens, row['Skills_tokens'])
        sim_interests = jaccard_similarity(user_interests_tokens, row['Interests_tokens'])
        sim_goals = jaccard_similarity(user_goals_tokens, row['Goals_tokens'])
        avg_sim = (sim_qualifications + sim_skills + sim_interests + sim_goals) / 4

        if avg_sim > best_score:
            best_score = avg_sim
            best_row = row

    if best_row:
        return best_row['Fields'], best_row['Job Titles']
    else:
        return None, None

def main():
    data = parse_csv_data(csv_data)
    print("Enter your qualifications (e.g. 12th or Graduation):")
    user_qualifications = input().strip()
    print("Enter your skills (comma separated):")
    user_skills = input().strip()
    print("Enter your interests (comma separated):")
    user_interests = input().strip()
    print("Enter your goals (sentence or keywords):")
    user_goals = input().strip()

    field, job_title = suggest_job(user_qualifications, user_skills, user_interests, user_goals, data)

    if user_qualifications.lower() == "12th":
        if field:
            print("\nSuggested Field:", field)
        else:
            print("Sorry, no matching field found.")
    elif user_qualifications.lower() == "graduation":
        if field and job_title:
            print("\nSuggested Field:", field)
            print("Suggested Job Title(s):", job_title)
        else:
            print("Sorry, no matching job suggestion found.")
    else:
        print("Unsupported qualification. Please enter '12th' or 'Graduation'.")

if __name__ == "__main__":
    main()
