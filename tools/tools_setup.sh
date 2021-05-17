echo '--------------------------------------'
echo 'installing cherrypy pyzbar Pillow nano progress matplotlib'
sudo apt-get update
sudo apt-get install python3-pip
source ~/.bashrc
yes | pip3 install Cython
yes | pip3 install cherrypy pyzbar
sudo apt-get -y install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
yes | pip3 install Pillow
sudo apt-get -y install nano
yes | pip3 install progress matplotlib

echo '--------------------------------------'
echo 'installing pycuda'
echo 'export CUDA_HOME=/usr/local/cuda' >> ~/.bashrc 
echo 'export PATH=$CUDA_HOME/bin:$PATH' >> ~/.bashrc 
echo 'LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc 
source ~/.bashrc
nvcc --version
pip3 install pycuda
echo 'export PYTHONPATH=/usr/lib/python3.6/dist-packages:$PYTHONPATH' >> ~/.bashrc
source ~/.bashrc

echo '--------------------------------------'
echo 'installing Cython pytorch torchvision'
wget https://nvidia.box.com/shared/static/cs3xn3td6sfgtene6jdvsxlr366m2dhq.whl -O torch-1.6.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get -y install libopenblas-base libopenmpi-dev 
yes | pip3 install numpy torch-1.6.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get -y install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
git clone --branch v0.7.0 https://github.com/pytorch/vision torchvision
cd torchvision
export BUILD_VERSION=0.7.0  # where 0.x.0 is the torchvision version  
python3 setup.py install --user
cd ../  # attempting to load torchvision from build dir will result in import error

echo '--------------------------------------'
yes | pip3 install Jinja2 simplejson ws4py netifaces tqdm imutils pylibdmtx
sudo apt-get -y install libdmtx0a


