cd frontend
npm run build
cd ..
sudo docker build . -t portal
sudo docker run -p 80:5000 portal
