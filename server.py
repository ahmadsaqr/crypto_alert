import smtplib


def server(subject,way=""):
    
    
    if way =='email' or way=="":
        toaddrs  =['ahmadsaqr@hotmail.com']   
    else:
        toaddrs  =['0064220398674@sms.clicksend.com','0064220398674@voice.clicksend.com']   

    
    fromaddr = 'arohamart@gmail.com'
    server   =  smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("arohamart@gmail.com", "arohamart4ever")
    print('From: ' + fromaddr)
    print('To: ' + str(toaddrs))
    print('Message: ' )
    server.sendmail(fromaddr, toaddrs,subject)
    server.quit()    
    
