import shutil

read_url = 'save_file/20180920.txt'
write_url = 'save_file/20180920.txt'

lines_seen = set()
out_file = open(write_url, 'w')
file = open(read_url, 'r')
for line in file:
    if line not in lines_seen:
        out_file.write(line)
        lines_seen.add(line)
out_file.close()

