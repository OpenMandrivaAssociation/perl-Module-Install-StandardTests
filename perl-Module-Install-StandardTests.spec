%define upstream_name    Module-Install-StandardTests
Name:		perl-%{upstream_name}
Version:	0.05
Release:	6

Summary:	Generate standard tests for installation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	noarch

%description
Writes a few standard test files to the test directory 't/'.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 655055
- rebuild for updated spec-helper

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 559512
- import perl-Module-Install-StandardTests


* Sun Jul 25 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
