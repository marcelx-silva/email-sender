from datetime import datetime as dt
import sys 
import yagmail as ya


email_receiver= "yourgmail@gmail.com"
email_sender="anothergmail@gmail.com"
email_sender_password="your_email_sender_password"

content = [
    "Enviando email para"+email_receiver,
    "Data: "+dt.utcnow().strftime("%d/%m/%Y"),
    "Horário Local: "+dt.utcnow().strftime("%H:%M:%S"),
    "Exercicio do Curso de Docker"
]

try:
    yag = ya.SMTP(email_sender,email_sender_password)
    
    yag.send(
        to=email_receiver,
        subject="Yagmail test with attachment",
        contents=content, 
    )
    print("Email enviado para: "+email_receiver)
except Exception as e:
    print("Erro, não foi possível enviar a sua mensagem!")
finally:
    print("Encerrando...")    
