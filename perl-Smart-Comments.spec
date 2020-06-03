#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Smart-Comments
Version  : 1.06
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Smart-Comments-1.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Smart-Comments-1.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsmart-comments-perl/libsmart-comments-perl_1.06-1.debian.tar.xz
Summary  : 'Comments that do more than just sit there'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Smart-Comments-license = %{version}-%{release}
Requires: perl-Smart-Comments-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Smart::Comments
Smart comments provide an easy way to insert debugging and tracking code
into a program. They can report the value of a variable, track the
progress of a loop, and verify that particular assertions are true.

%package dev
Summary: dev components for the perl-Smart-Comments package.
Group: Development
Provides: perl-Smart-Comments-devel = %{version}-%{release}
Requires: perl-Smart-Comments = %{version}-%{release}

%description dev
dev components for the perl-Smart-Comments package.


%package license
Summary: license components for the perl-Smart-Comments package.
Group: Default

%description license
license components for the perl-Smart-Comments package.


%package perl
Summary: perl components for the perl-Smart-Comments package.
Group: Default
Requires: perl-Smart-Comments = %{version}-%{release}

%description perl
perl components for the perl-Smart-Comments package.


%prep
%setup -q -n Smart-Comments-1.06
cd %{_builddir}
tar xf %{_sourcedir}/libsmart-comments-perl_1.06-1.debian.tar.xz
cd %{_builddir}/Smart-Comments-1.06
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Smart-Comments-1.06/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Smart-Comments
cp %{_builddir}/Smart-Comments-1.06/LICENSE %{buildroot}/usr/share/package-licenses/perl-Smart-Comments/c930771eee6b5e5a6dbeff04a7820d21f473e079
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Smart-Comments/d72f5c47e19037fb2bc771411fad0f6865ff8a67
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
/usr/share/man/man3/Smart::Comments.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Smart-Comments/c930771eee6b5e5a6dbeff04a7820d21f473e079
/usr/share/package-licenses/perl-Smart-Comments/d72f5c47e19037fb2bc771411fad0f6865ff8a67

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Smart/Comments.pm
