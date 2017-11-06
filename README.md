# track-ivc
IVC Budget tracking website

Commands:

  Initial Setup:
  `docker-compose up --build`
  
  If initial setup not needed: `docker-compose up`
  
  Stop: ctrl+c first then `docker-compose stop`
  
  Remove stopped containers: `docker-compose rm -f`
  
  Remove dangling images: `docker rmi -f $(docker images-qf dangling=true)`
  
  Reseed db if not working properly: `docker-compose exec website track db reset --with-testdb`
	

Access to application:

	Mac: Enter `local.docker:8000` in address bar
	
	Windows:
	
		1. Go to instance/settings.py
		
		2. Comment out `SERVER_NAME = 'local.docker:8000'` by putting a `#` in front of it
		
		3. Input `localhost:8000` in address bar
