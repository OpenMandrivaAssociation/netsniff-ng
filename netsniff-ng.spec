Name:		netsniff-ng
Version:	0.5.8
Release:	1
Summary:	A high performance network sniffer for packet inspection
License:	GPLv2
Group:		Networking/Other
URL:		http://netsniff-ng.org/
Source:		http://www.netsniff-ng.org/pub/netsniff-ng/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  ncurses-devel
BuildRequires:  libnl3-devel
BuildRequires:  libz-devel
BuildRequires:	pcap-devel
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  geoip-devel
BuildRequires:  netfilter_conntrack-devel

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
%setup_compile_flags
./configure
%make PREFIX=%{_prefix} CFLAGS="$CFLAGS" LDFLAGS="$LDFLAGS" DISTRO=1 ETCDIR=%{_sysconfdir}

%install
%makeinstall_std PREFIX=%{_prefix} ETCDIR=%{_sysconfdir}

%files
%doc AUTHORS COPYING README REPORTING-BUGS
%{_sbindir}/netsniff-ng
%{_sbindir}/bpfc
%{_sbindir}/ifpps
%{_sbindir}/astraceroute
%{_sbindir}/trafgen
%{_mandir}/man8/*.8*
%dir %{_sysconfdir}/netsniff-ng
%config(noreplace) %{_sysconfdir}/netsniff-ng/*


