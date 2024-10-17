Summary:	A tool to flush ARP cache entries from devices
Name:		arprelease
Version:	1.2
Release:	6
License:	GPL
Group:		Networking/Other
URL:		https://arprelease.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/arprelease/%{name}-%{version}.tar.bz2
BuildRequires:	net-devel >= 1.1.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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


%changelog
* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2-5mdv2010.0
+ Revision: 382695
- rebuilt against libnet 1.1.3

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.2-4mdv2009.0
+ Revision: 226172
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.2-3mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2-3mdv2008.0
+ Revision: 83858
- rebuild


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdv2007.0
+ Revision: 101567
- Import arprelease

* Fri Mar 17 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdk
- rebuilt against libnet1.1.2

* Mon Oct 17 2005 Olivier Thauvin <nanardon@mandriva.org> 1.2-1mdk
- 1.2

* Fri Oct 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package

