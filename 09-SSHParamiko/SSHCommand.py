from typing import Collection
import paramiko

def execute_command(command, host, user, password, sudo=False):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password, timeout=2)
    stdin,stdout,stderr = client.exec_command(command)
    output=stdout.readlines()
    client.close()
    return output


HOST = '192.168.0.245'
USER = 'root'
PASSWORD = 'Zaragoza2020'
# COMMAND = str("(echo "CPU `LC_ALL=C top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}'`% RAM `free -m | awk '/Mem:/ { printf("%3.1f%%", $3/$2*100) }'` HDD `df -h / | awk '/\// {print $(NF-1)}'`")")
COMMAND = '(ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10)'
# ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10

# awk '/MemTotal/{t=$2}/MemAvailable/{a=$2}END{print 100-100*a/t"%"}' /proc/meminfo
# df | awk '/ \/$/{print "HDD "$5}'
# (grep 'cpu ' /proc/stat;sleep 0.1;grep 'cpu ' /proc/stat)|awk -v RS="" '{print "CPU "($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)"%"}'

output=execute_command(COMMAND,HOST,USER,PASSWORD)

print("Memory output for host" + HOST)


for line in output:
    print(line)
