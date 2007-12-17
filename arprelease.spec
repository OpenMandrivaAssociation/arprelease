Summary:	A tool to flush ARP cache entries from devices
Name:		arprelease
Version:	1.2
Release:	%mkrel 3
License:	GPL
Group:		Networking/Other
URL:		http://arprelease.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/arprelease/%{name}-%{version}.tar.bz2
BuildRequires:	libnet1.1.2-devel

%description
arprelease is a small libnet-based tool to flush ARP cache entries
from devices like Cisco routers to move an IP from one Linux box
to another.

%prep

%setup -q -n %{name}

%build

gcc %{optflags} `libnet-config --defines` arprelease.c -o arprelease `libnet-config --libs`

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -m0755 arprelease  %{buildroot}%{_sbindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/arprelease
