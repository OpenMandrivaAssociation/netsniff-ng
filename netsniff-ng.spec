Name:		netsniff-ng
Version:	0.5.8
Release:	1
Summary:	A high performance network sniffer for packet inspection
License:	GPLv2
Group:		Monitoring
URL:		http://netsniff-ng.org/
Source0:	http://www.netsniff-ng.org/pub/netsniff-ng/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig(geoip)
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
%doc AUTHORS README REPORTING-BUGS VERSION Documentation/*
%{_sbindir}/*
%{_mandir}/man8/*.8*
%config(noreplace) %{_sysconfdir}/netsniff-ng/*
