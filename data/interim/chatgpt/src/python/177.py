import lnkfile

def parse_lnk_file(lnk_file_path):
    lnk = lnkfile.LnkFile(lnk_file_path)
    print("Target Path:", lnk.get_target_path())
    print("Command Arguments:", lnk.get_command_arguments())
    print("Working Directory:", lnk.get_working_directory())
    print("Icon Location:", lnk.get_icon_location())
    # Add more attributes as needed

# Replace 'file.496.0xfffffa80022ac740.resume.pdf.lnk.dat' with the actual path to your .lnk file
parse_lnk_file('file.496.0xfffffa80022ac740.resume.pdf.lnk.dat')
