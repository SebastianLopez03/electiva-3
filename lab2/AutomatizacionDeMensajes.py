import pywhatkit

pywhatkit.sendwhatmsg_instantly(phone_no='+573176170360',
                                message='Automating message whit PywhatKit',
                                tab_close=True)


pywhatkit.sendwhatmsg_to_group_instantly(group_id='Electiva 111 AR', 
                                         message='Automating message whit Pywhatkit', 
                                         tab_close=True
                                         )

pywhatkit.sendwhatmsg_to_group(group_id ='Electiva 111 AR',
                               message='Automating message whit PywhatKit',
                               time_hour=11,time_min=3, 
                               tab_close=True)