## ReadMe

>This is the basic instrument of my IOT management system.  And hopes it will be useful for Mr. Zhang.


### How To Use it

1. Enter the project folder, and find `manage.py` file in the root directory, then start the Django Web Server, using command:

 > python3 manage.py runserver
	
2. Start `client_model.py` file to simulate remote IOT system, using command:

 > python3 client_model.py
 
3. Then you can start use IOT management system. Here is the one notice, this system has email alert function, it is implemented in `email.py` file, you can edit the receiver and the content. You must provide a email accout to this system as sender, and you should set them in `control_app/setting.py` file, in the final 4 lines:

		EMAIL_HOST = 'mail.bupt.edu.cn' 
		EMAIL_PORT = 25
		EMAIL_HOST_USER = 'mryuan@bupt.edu.cn'
		EMAIL_HOST_PASSWORD = '****' 
		# set your password below
		DEFAULT_FROM_EMAIL = 'System<mryuan@bupt.edu.cn>'  
		
**In the end, Have fun in coding, bro. :->**