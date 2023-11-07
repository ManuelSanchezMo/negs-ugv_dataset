#!/bin/bash

# Update
sudo apt-get update

# Install dependencies
echo "Installing dependencies..."
sudo apt-get install apt-transport-https \
                     ca-certificates \
                     curl             \
                     software-properties-common -y

# Add Docker's GPG Key
echo "Add Docker's GPG Key..."
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker's stable repository
echo "Add Docker's stable repository..."
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update
sudo apt-get update

# Install latest version of Docker CE (Community Edition)
echo "Install latest version of Docker CE (Community Edition)"
sudo apt-get install docker-ce -y

echo "Installation Complete"

echo "Checking for NVIDIA drivers..."

if test -c /dev/nvidia0
then
   echo "Installing NVIDIA Docker..."
   # If you have nvidia-docker 1.0 installed: we need to remove it and all existing GPU containers
    docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
    sudo apt-get purge -y nvidia-docker

    # Add the package repositories
    curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | \
    sudo apt-key add -
    curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
    sudo tee /etc/apt/sources.list.d/nvidia-docker.list
    sudo apt-get update

    # Install nvidia-docker2 and reload the Docker daemon configuration
    sudo apt-get install -y nvidia-docker2
    sudo pkill -SIGHUP dockerd

    # Test nvidia-smi with the latest official CUDA image
    docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi

fi
 
