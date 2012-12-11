%define name	netsniff-ng
%define version 0.5.6
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A high performance network sniffer for packet inspection
License:	GPLv2
Group:		Monitoring
URL:		http://netsniff-ng.org/
Source0:	http://www.netsniff-ng.org/pub/netsniff-ng/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ncurses-devel
BuildRequires:	GeoIP-devel
BuildRequires:	pkgconfig(libnetfilter_conntrack)
BuildRequires:	flex
BuildRequires:	pkgconfig(liburcu)

%description
netsniff-ng is a high performance linux network sniffer for packet inspection.
Basically, it is similar to tcpdump, but it doesn't need one syscall per
packet. Instead, it uses an memory mapped area within kernelspace for accessing
packets without copying them to userspace (zero-copy mechanism).

This tool is useful for debugging your network, measuring performance
throughput or creating network statistics of incoming packets on central
network nodes like routers or firewalls. 

%prep
%setup -q

%build
pushd src
%cmake
%make
popd

%install
pushd src/build
%makeinstall_std
popd

rm -f %{buildroot}%{_mandir}/man8/netsniff-ng.8.gz

%files
%defattr(-,root,root)
%doc AUTHORS PROJECTS README REPORTING-BUGS THANKS VERSION Documentation/*
%{_sbindir}/*
%{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/netsniff-ng/*


%changelog
* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.5.6-2mdv2012.0
+ Revision: 789132
- build with urcu

* Fri Mar 30 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.5.6-1
+ Revision: 788403
- update to 0.5.6

* Sun Oct 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.5.0-1mdv2011.0
+ Revision: 584851
- new version

* Fri Feb 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.4.2-1mdv2010.1
+ Revision: 507997
- update to new version 0.5.4.2

* Sun Jan 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.4.1-1mdv2010.1
+ Revision: 485973
- new version

* Thu Dec 31 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.4-1mdv2010.1
+ Revision: 484525
- new version

* Tue Dec 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-2mdv2010.1
+ Revision: 474936
- add missing man pages and filter rules, as per author suggestion :)

* Mon Dec 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 474582
- import netsniff-ng


* Mon Dec 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.3-1mdv2010.1
- first mdv release
