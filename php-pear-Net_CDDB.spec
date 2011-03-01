%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	CDDB
%define		_status		alpha
%define		_pearname	Net_CDDB

Summary:	%{_pearname} - Package to access and query CDDB audio-CD servers
Summary(pl.UTF-8):	%{_pearname} - Pakiet do współpracy z serwerami CDDB
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	3
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c174cd8ed66c81292d627d0ba5c7d1ba
URL:		http://pear.php.net/package/Net_CDDB/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.3.0
Requires:	php-pear-MDB2 >= 1:2.2.2
Requires:	php-pear-Net_Socket >= 1.0.6
Obsoletes:	php-pear-Net_CDDB-tests
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

%prep
%pear_package_setup
# class/test -> tests
install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/tests/*,tests/%{_pearname}}

# class/docs -> docs
install -d docs/%{_pearname}/docs
mv ./%{php_pear_dir}/%{_class}/docs/* docs/%{_pearname}/docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/CDDB.php
%{php_pear_dir}/Net/CDDB
