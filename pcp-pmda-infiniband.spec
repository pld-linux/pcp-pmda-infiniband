Summary:	PMDA for collecting statistics from Infiniband HCAs and switches
Summary(pl.UTF-8):	PMDA do zbierania statystyk z HCA i switchy Infiniband
Name:		pcp-pmda-infiniband
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	ftp://oss.sgi.com/projects/pcp/download/%{name}-%{version}.tar.bz2
# Source0-md5:	55f42571dcd057117b670bdd392a9554
Patch0:		%{name}-update.patch
URL:		http://oss.sgi.com/projects/pcp/
BuildRequires:	pcp-devel
BuildRequires:	libibmad-devel
BuildRequires:	libibumad-devel
Requires:	pcp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the PMDA for collecting Infiniband statistics.
By default it monitors only the local HCAs, but can also be configured
to monitor remote GUIDs such as IB switches.

%description -l pl.UTF-8
Ten pakiet zawiera PMDA do zbierania statystyk Infiniband. Domyślnie
monitoruje tylko lokalne HCA, ale może być także skonfigurowany do
monitorowania zdalnych GUID-ów, takich jak switche IB.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	IBLIBS="-libumad -libmad" \
	PCFLAGS="%{rpmcflags} -D_GNU_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir /var/lib/pcp/pmdas/ib
%attr(755,root,root) /var/lib/pcp/pmdas/ib/Install
%attr(755,root,root) /var/lib/pcp/pmdas/ib/Remove
%attr(755,root,root) /var/lib/pcp/pmdas/ib/pmdaib
%attr(755,root,root) /var/lib/pcp/pmdas/ib/pmda_ib.so
/var/lib/pcp/pmdas/ib/domain.h
/var/lib/pcp/pmdas/ib/help
/var/lib/pcp/pmdas/ib/help.dir
/var/lib/pcp/pmdas/ib/help.pag
/var/lib/pcp/pmdas/ib/pmns
/var/lib/pcp/pmdas/ib/root
%{_mandir}/man1/pmdaib.1*
