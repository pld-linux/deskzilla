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
Requires:	jakarta-commons-codec >= 1.3
Requires:	jakarta-commons-logging >= 1.0.4
Requires:	javolution >= 4.0.2
Requires:	jdom >= 1.0
Requires:	jgoodies-forms >= 1.0.7
Requires:	jre >= 1.5
Requires:	nekohtml >= 0.9.5
Requires:	picocontainer >= 1.1
Requires:	java-xmlrpc >= 2.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deskzilla is a desktop client for Mozilla's Bugzilla's bug tracking
system. It provides Bugzilla users with an interactive working
environment and extra features, serving as a valuable tool for every
project participant.

%prep
%setup -q -n %{name}-%{_ver}

# Remove public bundled jars
lib="lib"
liborig="lib.orig"
mv $lib $liborig
mkdir $lib
# They've patched commons-httpclient (was version 3.0)
mv $liborig/commons-httpclient.jar $lib
# Almworks proprietary lib
mv $liborig/almworks-tracker-api.jar $lib
# IntelliJ IDEA proprietary lib
mv $liborig/forms_rt.jar $lib
# God knows what's this. Anyway, proprietary.
mv $liborig/twocents.jar $lib
rm -rf $liborig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt RELEASE.txt license.html
