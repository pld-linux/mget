Summary:	A multithreated command-line download utility
Summary(pl):	Wielow±tkowy klient HTTP/FTP
Name:		mget
Version:	1.3.2.2
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.cse.iitk.ac.in/users/dbera/%{name}-%{version}.tar.gz
URL:		http://www.cse.iitk.ac.in/users/dbera/mget.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a command line download manager. It splits the file into a
number of segments and uses several separate threads to download each
segment. It can handle proxies.

%description -l pl
Wielow±tkowe narzêdzie do ¶ci±gania plików. Potrafi podzieliæ plik na
segmenty i ¶ci±gaæ je kilka na raz w tym samym czasie. Dziêki temu
czas ci±gniêcia pliku skraca siê w niektórych przypadkach
kilkakrotnie. Obs³uguje proxy.

%prep
%setup -q

%build
%{__make} CC="%{__cc} %{rpmcflags}"

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
