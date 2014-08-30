echo bootstrapping packman...

# update
sudo apt-get -y update &&
# install prereqs
sudo apt-get install -y curl python-setuptools python-dev rubygems &&
# install docker dependencies
sudo apt-get install -y linux-image-generic-lts-raring linux-headers-generic-lts-raring
[ -e /usr/lib/apt/methods/https ] || {
  apt-get update
  apt-get install apt-transport-https
}
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
# install docker
$ curl -sSL https://get.docker.io/ubuntu/ | sudo sh

# install fpm
sudo gem install fpm --no-ri --no-rdoc &&
# configure gem and bundler
echo -e 'gem: --no-ri --no-rdoc\ninstall: --no-rdoc --no-ri\nupdate:  --no-rdoc --no-ri' >> ~/.gemrc
# install pip
curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python
# install virtualenv
sudo pip install virtualenv==1.11.4 &&
# install packman
sudo pip install packman
# TODO: add virtualenv to provisioning process
# sudo pip install virtualenvwrapper
# mkvirtualenv packman
# TODO: add bash completion support using docopt-completion
# docopt-completion #VIRTUALENV#...pkm.py

echo bootstrap done
echo NOTE: currently, using some of the packman's features requires that it's run as sudo.