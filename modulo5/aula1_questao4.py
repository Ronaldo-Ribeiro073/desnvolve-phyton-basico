import datetime

# Recebe a data e hora atuais
now = datetime.datetime.now()

# Formata data
data_formatada = f"{now.day:02}/{now.month:02}/{now.year}"

# Formata hora
hora_formatada = f"{now.hour:02}:{now.minute:02}"

print(f"Data: {data_formatada}")
print(f"Hora: {hora_formatada}")
