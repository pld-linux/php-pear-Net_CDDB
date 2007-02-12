%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	CDDB
%define		_status		alpha
%define		_pearname	Net_CDDB

Summary:	%{_pearname} - Package to access and query CDDB audio-CD servers
Summary(pl.UTF-8):   %{_pearname} - Pakiet do współpracy z serwerami CDDB
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7ce657b4cb9d847000566e5c76634eb1
URL:		http://pear.php.net/package/Net_CDDB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net_CDDB class is used to access CDDB audio-CD servers via
different protocols. The class can get detailed audio-CD data (track
names, artist names, album name, etc.) from the CDDB server for a
given audio CD.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa Net_CDDB służy do współpracy z serwerami audio-cd CDDB za pomocą
różnych protokołów. Klasa może być użyta do uzyskania szczegółowych
informacji o płycie audio (nazwy utworów, albumu, informacje o
artyście) z serwera CDDB dla danej płyty.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/{docs/CDDB_example_output.txt,docs/CDDB_fileformat.txt,docs/CDDB_notes.txt,docs/CDDB_protocol.txt,docs/CDDB_record.txt}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/CDDB.php
%{php_pear_dir}/Net/CDDB
%{php_pear_dir}/Net/docs/examples/*

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/Net/tests/CDDBTest.php
%{php_pear_dir}/Net/tests/CDDBTest_Filesystem.php
%{php_pear_dir}/Net/tests/CDDBTest_HTTP.php
%{php_pear_dir}/Net/tests/CDDBTest_CDDBP.php
