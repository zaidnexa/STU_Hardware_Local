
import subprocess

password = 'Roboticsandmind123STU'
command = 'python3 stu_face_dizzy'
cmd_list = ['sudo', '-S'] + command.split()

process = subprocess.Popen(cmd_list, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate(password.encode())

print(stdout.decode())
print(stderr.decode())

