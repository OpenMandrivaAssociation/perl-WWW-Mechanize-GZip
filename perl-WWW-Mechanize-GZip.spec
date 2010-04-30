%define upstream_name    WWW-Mechanize-GZip
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Tries to fetch webpages with gzip-compression
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Test::More)
BuildRequires: perl(WWW::Mechanize)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The the WWW::Mechanize::GZip manpage module tries to fetch a URL by
requesting gzip-compression from the webserver.

If the response contains a header with 'Content-Encoding: gzip', it
decompresses the response in order to get the original (uncompressed)
content.

This module will help to reduce bandwith fetching webpages, if supported by
the webeserver. If the webserver does not support gzip-compression, no
decompression will be made.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/WWW/


