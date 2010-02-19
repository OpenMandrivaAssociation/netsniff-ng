%define name	netsniff-ng
%define version 0.5.4.2
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A high performance network sniffer for packet inspection
License:	GPL
Group:		Monitoring
URL:		http://code.google.com/p/netsniff-ng/
Source:     http://netsniff-ng.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
netsniff-ng is a high performance linux network sniffer for packet inspection.
Basically, it is similar to tcpdump, but it doesn't need one syscall per
packet. Instead, it uses an memory mapped area within kernelspace for accessing
packets without copying them to userspace (zero-copy mechanism).

This tool is useful for debugging your network, measuring performance
throughput or creating network statistics of incoming packets on central
network nodes like routers or firewalls. 

%prep
%setup -q -n %{name}_%{version}
cd src
make clean

%build
cd src
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
install -d -m  755 %{buildroot}%{_sbindir}
install -m 755 src/netsniff-ng %{buildroot}%{_sbindir}
install -d -m  755 %{buildroot}%{_mandir}/man8
install -m 644 src/doc/netsniff-ng.8 %{buildroot}%{_mandir}/man8
install -d -m  755 %{buildroot}%{_sysconfdir}/netsniff-ng/rules
install -m 644 src/rules/* %{buildroot}%{_sysconfdir}/netsniff-ng/rules

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changelog COPYING README TODO VERSION
%{_sbindir}/%{name}
%{_mandir}/man8/netsniff-ng.8*
%config(noreplace) %{_sysconfdir}/netsniff-ng/rules
