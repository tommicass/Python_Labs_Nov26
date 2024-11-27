for line in open(r"C:\Users\tcassidy\Project\Python_Labs_Nov26\labs\messier.txt", encoding='latin_1'):
    if not line:break

    if not line.startswith('M'):
        next
    else:
        m_no = line[0:5].rstrip()
        galaxy_name = line[6:39].rstrip()
        if galaxy_name == '':
            galaxy_name = 'No Name'
        galaxy_type = line[40:63].rstrip()
        constellation = line[64:].rstrip()

        new_line = [m_no, galaxy_name, galaxy_type, constellation]
        print_line = "|".join(new_line)
            
        print(print_line)