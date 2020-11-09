%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

# RPM preamble
Name: EnhancedSession
Version: 1
Release: 0
License: Creative Commons
Summary: Enhanced Session Handling
BuildArch: noarch
Source0: %{name}-%{version}-%{release}.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: /usr/bin/python

%description
The purpose of this extension is to create an easy way to commit a timered config session

%prep
%setup -c

%build

%install
rm -rf %{buildroot}/
mkdir -p %{buildroot}%{_optdir}
cp -Rp * %{buildroot}%{_optdir}

%clean
rm -rf %{buildroot}

%files
%defattr(777,root,root,777)
# Specifying the directories individually # gives them the right mod
%dir %{_optdir}/%{name}/
%dir %{_optdir}/%{name}/bin/ 
%{_optdir}/%{name}/bin/EnhancedSession.py 
%{_optdir}/%{name}/bin/install.sh

%post
%{_optdir}/%{name}/bin/install.sh

%changelog
* Fri Apr 13 2018 Emil <emil@arista.com> - %{version}-1
- Initial RPM build
