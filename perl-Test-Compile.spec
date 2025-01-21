#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v10
# autospec commit: 5905be9
#
Name     : perl-Test-Compile
Version  : 3.3.3
Release  : 54
URL      : https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-v3.3.3.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EG/EGILES/Test-Compile-v3.3.3.tar.gz
Summary  : 'Assert that your Perl files compile OK.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-Compile-license = %{version}-%{release}
Requires: perl-Test-Compile-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n Test-Compile-v3.3.3
cd %{_builddir}/Test-Compile-v3.3.3
pushd ..
cp -a Test-Compile-v3.3.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
cp %{_builddir}/Test-Compile-v%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-Compile/ca04e67360ff58b1f1099f198aead90c130ddd4e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib/perl5/*
