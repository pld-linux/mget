Summary:	A multithreated command-line download utility
Summary(pl.UTF-8):	Wielowątkowy klient HTTP/FTP
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

%description -l pl.UTF-8
Wielowątkowe narzędzie do ściągania plików. Potrafi podzielić plik na
segmenty i ściągać je kilka na raz w tym samym czasie. Dzięki temu
czas ciągnięcia pliku skraca się w niektórych przypadkach
kilkakrotnie. Obsługuje proxy.

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
