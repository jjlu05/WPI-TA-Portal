docker build -t gitgurus . 
docker tag gitgurus adequatej/gitgurus
docker push adequatej/gitgurus

# don't forget to pull in ssh EC2 instance after making changes to code and rebuilding container