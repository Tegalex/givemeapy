import smtplib
server=smtplib.SMTP('localhost', local_hostname='localhost')
server.sendmail('tegagni@mailup.com', 'alessandro.tegagni@gmail.com', 
                """to: "alessandro.tegagni@gmail.com
                from: tegagni@mailup.com
                
                Beware the ideas of March.
                """)
server.quit()
                