# How to make your own extension

I have supplied the rpmbuild directory structure for my Extension where the source code and RPM spec files are located. In SOURCES is where you'll put your code, zip it up and write an RPM spec for it in order to do an rpmbuild.

## Create your rpmbuild directory

Create it in your home dir with this command:

    mkdir -p $HOME/rpmbuild/{SOURCES,SPECS,BUILD,RPMS,SRPMS}
    cd ~/rpmbuild
 
Verify some variables:

    rpm --eval '%{_rpmdir}'
    /home/youruser/rpmbuild/RPMS
    rpm --eval '%{_tmppath}'

## Add your code

cd into the SOURCES subdir and create a folder for your project:

    cd ~/rpmbuild/SOURCES
    mkdir MyProject
    cd MyProject
    mkdir bin
    
Copy your scripts or whatever into the bin folder you just created.
    
## Write your RPM spec

You need to write a spec for your RPM and put it in the SPECS subfolder of rpmbuild. Writing specs is a little bit involved and I am by no means an expert. Just look at the one i wrote for my extension. If you want to explore it further there's probably a ton of info on writing specs on the interwebs.

## Zip your scripts

IMPORTANT!! The name of the tarball you create must reflect the name you reference in your rpm spec file. 

    cd ~/rpmbuild/SOURCES
    tar -zcvf MyProject-1-0.gz MyProject/

## Build your RPM

Build your RPM with rpmbuild command, you may need to install some packages for it to work.

    rpmbuild -bb -v --target=noarch ~/rpmbuild/SPECS/MyProject-1-0.spec
    
Make sure it completes without errors.

## You're done!

The newly created RPM will be located in ~/rpmbuild/RPMS/noarch directory. Just follow the main README.md of this repo to copy and install it to your EOS devices.

