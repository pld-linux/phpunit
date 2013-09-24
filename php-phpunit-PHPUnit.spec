%define		status		stable
%define		pearname	PHPUnit
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{pearname} - zestaw testów regresyjnych
Name:		php-phpunit-%{pearname}
Version:	3.7.27
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
# Source0-md5:	254373321f77807658540c550e13e9e1
URL:		http://www.phpunit.de/
BuildRequires:	php-channel(components.ez.no)
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-channel(pear.symfony-project.com)
BuildRequires:	php-pear >= 4:1.1-2
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
# https://github.com/sebastianbergmann/phpunit/pull/975
Requires:	php(ctype)
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(reflection)
Requires:	php(spl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-phpunit-File_Iterator >= 1.3.1
Requires:	php-phpunit-PHPUnit_MockObject <= 1.2.99
Requires:	php-phpunit-PHPUnit_MockObject >= 1.2.0
Requires:	php-phpunit-PHP_CodeCoverage <= 1.2.99
Requires:	php-phpunit-PHP_CodeCoverage >= 1.2.1
Requires:	php-phpunit-PHP_Timer >= 1.0.4
Requires:	php-phpunit-Text_Template >= 1.1.1
Requires:	php-symfony2-Yaml <= 2.99.99
Requires:	php-symfony2-Yaml >= 2.0
Suggests:	php(json)
Suggests:	php(simplexml)
Suggests:	php(tokenizer)
Suggests:	php-phpunit-PHP_Invoker
Provides:	php-PHPUnit = %{version}
Obsoletes:	php-PHPUnit < 3.5
Obsoletes:	php-PHPUnit-tests
Obsoletes:	php-pear-PHPUnit
Obsoletes:	php-pear-PHPUnit2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHPUnit is a regression testing framework used by the developer who
implements unit tests in PHP. It is based upon JUnit, which can be
found at <http://www.junit.org/>.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
PHPUnit jest zestawem testów regresyjnych używanych przez developerów,
którzy implementują jednostki testowe w PHP. Jest bazowane na JUnit,
który można znaleźć pod adresem <http://www.junit.org/>.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
install -d $RPM_BUILD_ROOT%{_bindir}
install -p usr/bin/phpunit $RPM_BUILD_ROOT%{_bindir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/.channel.pear.phpunit.de/*.reg
%attr(755,root,root) %{_bindir}/phpunit
%{php_pear_dir}/PHPUnit
