#!/usr/bin/python3
import gitlab
import sys


def download_file(host, token, project_name, branch_name, file_path, output):
    try:
        gl = gitlab.Gitlab(host, private_token=token)
        pl = gl.projects.list(search=project_name)
        for p in pl:
            if p.name == project_name:
                project = p
                break
        with open(output, 'wb') as f:
            project.files.raw(file_path=file_path, ref=branch_name, streamed=True, action=f.write)
    except Exception as e:
        print("Error:", e)


num_arguments = len(sys.argv)
if num_arguments < 6:
    print('Usage: ./download-gitlab-file.py host token project_name branch_name file_path output')
else:
    download_file(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
        sys.argv[5],
        sys.argv[6]
    )
