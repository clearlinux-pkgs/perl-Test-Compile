#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Compile
Version  : 2.3.1
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-v2.3.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-v2.3.1.tar.gz
Summary  : 'Check whether Perl files compile correctly.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Compile-license = %{version}-%{release}
Requires: perl-Test-Compile-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(UNIVERSAL::require)
BuildRequires : util-linux

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
Requires: perl-Test-Compile = %{version}-%{release}

%description dev
dev components for the perl-Test-Compile package.


%package license
Summary: license components for the perl-Test-Compile package.
Group: Default

%description license
license components for the perl-Test-Compile package.


%package perl
Summary: perl components for the perl-Test-Compile package.
Group: Default
Requires: perl-Test-Compile = %{version}-%{release}

%description perl
perl components for the perl-Test-Compile package.


%prep
%setup -q -n Test-Compile-v2.3.1
cd %{_builddir}/Test-Compile-v2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-Compile
cp %{_builddir}/Test-Compile-v2.3.1/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Compile/ca04e67360ff58b1f1099f198aead90c130ddd4e
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Compile.3
/usr/share/man/man3/Test::Compile::Internal.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-Compile/ca04e67360ff58b1f1099f198aead90c130ddd4e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Test/Compile.pm
/usr/lib/perl5/vendor_perl/5.30.2/Test/Compile/Internal.pm
