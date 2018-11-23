#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Compile
Version  : 1.3.0
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-v1.3.0.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-v1.3.0.tar.gz
Summary  : 'Check whether Perl files compile correctly.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(UNIVERSAL::require)

%description
DESCRIPTION
Test::Compile is a Perl module that lets you check whether Perl modules
or scripts compile properly, and report its results in standard
Test::Simple fashion. It can test all Perl files in a distribution, or
individual files.

%package dev
Summary: dev components for the perl-Test-Compile package.
Group: Development
Provides: perl-Test-Compile-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-Compile package.


%prep
%setup -q -n Test-Compile-v1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Test/Compile.pm
/usr/lib/perl5/vendor_perl/5.28.0/Test/Compile/Internal.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Compile.3
/usr/share/man/man3/Test::Compile::Internal.3
