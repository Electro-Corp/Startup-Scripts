# Pretty print who command output
import subprocess

result = subprocess.run(["who"], stdout=subprocess.PIPE)
result = result.stdout.decode('utf-8')

users = []
for line in result.splitlines():
    users.append(line.split()[0])

final = ""
for i in range(len(users)):
  if i != len(users) - 1:
    final += users[i] + ", "
  else:
    final += "and " + users[i]

print(f"[INFO] {final} are logged in currently.")
