%define		_ver	%(echo %{version} | tr . _)
Summary:	Desktop client for Mozilla's Bugzilla's bug tracking system
Name:		deskzilla
Version:	1.4.1
Release:	0.1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://d1.almworks.com/.files/%{name}-%{_ver}.tar.gz
# NoSource0-md5:	07bbc361e330d3f9ab044b6b9a085736
NoSource:	0
URL:		http://www.almworks.com/deskzilla/overview.html
BuildArch:	noarch
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deskzilla is a desktop client for Mozilla's Bugzilla's bug tracking
system. It provides Bugzilla users with an interactive working
environment and extra features, serving as a valuable tool for every
project participant.

%prep
%setup -q -n %{name}-%{_ver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE.txt license.html
