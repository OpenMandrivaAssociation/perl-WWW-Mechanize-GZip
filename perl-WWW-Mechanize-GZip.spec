%define upstream_name    WWW-Mechanize-GZip
Name:		perl-%{upstream_name}
Version:	0.14
Release:	2

Summary:	Tries to fetch webpages with gzip-compression
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/WWW-Mechanize-GZip
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PEGI/WWW-Mechanize-GZip-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(WWW::Mechanize)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/WWW/

%changelog
* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 541158
- import perl-WWW-Mechanize-GZip


* Fri Apr 30 2010 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
