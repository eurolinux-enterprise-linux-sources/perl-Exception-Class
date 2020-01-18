Name:           perl-Exception-Class
Version:        1.37
Release:        2%{?dist}
Summary:        Module that allows you to declare real exception classes in Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Exception-Class/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/Exception-Class-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(base)
BuildRequires:  perl(Class::Data::Inheritable) >= 0.02
BuildRequires:  perl(Devel::StackTrace) >= 1.20
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.46
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Exception::Class allows you to declare exception hierarchies in your
modules in a "Java-esque" manner.

%prep
%setup -q -n Exception-Class-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendorlib}/Exception/
%{_mandir}/man3/Exception::Class.3pm*
%{_mandir}/man3/Exception::Class::Base.3pm*

%changelog
* Wed Jun 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-2
- License is GPL+ or Artistic now
- Specify all dependencies

* Sun Feb 24 2013 Paul Howarth <paul@city-fan.org> - 1.37-1
- Update to 1.37
  - I now recommend you use Throwable instead of this module; it has a nicer,
    more modern interface
  - Fixed warning from basic.t on 5.17.x (CPAN RT#79121)
  - 1.33 did not declare any prereqs (CPAN RT#79677)
  - Require Class::Data::Inheritable ≥ 0.02
  - Fixed some stupidity in the tests that appears to have been highlighted by
    recent changes to Devel::StackTrace (CPAN RT#81245)
  - Fixed various bugs and confusion in the docs
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands
- Make the %%files list more explicit
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Drop release testing (now more extensive and would fail anyway)
- Drop support for distributions older than EL-6 (test suite would need
  patching for EL-5 anyway)


* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 15 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-7
- Update dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.32-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.32-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Steven Pritchard <steve@kspei.com> 1.32-1
- Update to 1.32.
- License is now Artistic 2.0.
- Switch back to building with ExtUtils::MakeMaker/Makefile.PL.  (Dave
  Rolsky needs to make up his mind.)
- Add README to docs.

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29-5
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sat May 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29-4
- Mass rebuild with perl-5.12.0

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.29-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.29-2
- rebuild against perl 5.10.1

* Thu Jul 30 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.29-1
- Upstream update (Required by other packages, fix mass rebuild breakdowns).

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Steven Pritchard <steve@kspei.com> 1.26-1
- Update to 1.26.
- Bump Devel::StackTrace dependency to 1.20.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 1.24-1
- Update to 1.24.
- Bump Devel::StackTrace dependency to 1.17.
- Clean up to match current cpanspec output.
- Improve Summary and description.
- Build with Module::Build.
- BR Test::Pod and Test::Pod::Coverage and define IS_MAINTAINER.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.23-6
- Rebuild for perl 5.10 (again)

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.23-5
- rebuild against new perl

* Sat Dec 29 2007 Ralf Corsépius 1.23-4
- BR: perl(Test::More) (BZ 419631).
- Adjust License-tag.

* Tue Apr 17 2007 Steven Pritchard <steve@kspei.com> 1.23-3
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 1.23-2
- Canonicalize Source0 URL.
- Fix find option order.
- Drop executable bit from Exception/Class.pm to avoid a rpmlint warning.

* Fri Feb 03 2006 Steven Pritchard <steve@kspei.com> 1.23-1
- Update to 1.23

* Tue Jan 10 2006 Steven Pritchard <steve@kspei.com> 1.22-1
- Update to 1.22

* Mon Sep 05 2005 Steven Pritchard <steve@kspei.com> 1.21-3
- Remove explicit core module dependencies
- Add COPYING and Artistic

* Wed Aug 17 2005 Steven Pritchard <steve@kspei.com> 1.21-2
- Minor spec cleanup

* Tue Aug 16 2005 Steven Pritchard <steve@kspei.com> 1.21-1
- Specfile autogenerated.
