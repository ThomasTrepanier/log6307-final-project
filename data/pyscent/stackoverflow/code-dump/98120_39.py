def fix_xlsx(file_name):
    with zipfile.ZipFile(file_name) as input_file, zipfile.ZipFile(file_name + ".out", "w") as output_file:
         # Iterate over files
         for inzipinfo in input_file.infolist():
            with input_file.open(inzipinfo) as infile:
                if "xl/styles.xml" in inzipinfo.filename:
                    # Read, Process & Write
                    lines = infile.readlines()
                    new_lines = b"\n".join([line.replace(b'indent="-1"', b'indent="0"') for line in lines])
                    output_file.writestr(inzipinfo.filename, new_lines)
                else:
                    # Read & Write
                    output_file.writestr(inzipinfo.filename, b"\n".join([line for line in infile.readlines()]))
    # Replace file
    os.replace(file_name + ".out", file_name)
