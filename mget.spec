Summary:	A multithreated command-line download utility
Summary(pl):	Wielow�tkowy klient HTTP/FTP
Name:		mget
Version:	1.4.1
Release:	1
License:	GPL
Group:		Networking/Utilities
#Source0Download: http://www.cse.iitk.ac.in/users/dbera/mget.php
Source0:	http://www.cse.iitk.ac.in/users/dbera/%{name}-%{version}.tar.gz
# Source0-md5:	224a5e149098274313009fb660b566dd
Patch0:		%{name}-gcc33.patch
URL:		http://www.cse.iitk.ac.in/users/dbera/mget.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a command line download manager. It splits the file into a
number of segments and uses several separate threads to download each
segment. It can handle proxies.

%description -l pl
Wielow�tkowe narz�dzie do �ci�gania plik�w. Potrafi podzieli� plik na
segmenty i �ci�ga� je kilka na raz w tym samym czasie. Dzi�ki temu
czas ci�gni�cia pliku skraca si� w niekt�rych przypadkach
kilkakrotnie. Obs�uguje proxy.

%prep
%setup -q
%patch0 -p1

%build
./genmake
%{__make} \
	CC="%{__cc}" \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mget $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
