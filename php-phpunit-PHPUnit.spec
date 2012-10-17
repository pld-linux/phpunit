%define		status		stable
%define		pearname	PHPUnit
%define		php_min_version 5.2.7
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{pearname} - zestaw testów regresyjnych
Name:		php-phpunit-%{pearname}
Version:	3.7.8
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/PHPUnit-%{version}.tgz
# Source0-md5:	b7e40d23e937a116c070dfd16e48e840
URL:		http://www.phpunit.de/
BuildRequires:	php-channel(components.ez.no)
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-channel(pear.symfony-project.com)
BuildRequires:	php-pear >= 4:1.1-2
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(dom)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear >= 4:1.1-2
Requires:	php-phpunit-DbUnit >= 1.0.0
Requires:	php-phpunit-File_Iterator >= 1.3.1
Requires:	php-phpunit-PHPUnit_MockObject <= 1.2.99
Requires:	php-phpunit-PHPUnit_MockObject >= 1.1.0
Requires:	php-phpunit-PHP_CodeCoverage <= 1.2.99
Requires:	php-phpunit-PHP_CodeCoverage >= 1.1.0
Requires:	php-phpunit-PHP_Timer >= 1.0.2
Requires:	php-phpunit-Text_Template >= 1.1.1
Requires:	php-reflection
Requires:	php-symfony-YAML >= 2.1.0
Suggests:	php-curl
Suggests:	php-dbus
Suggests:	php-json
Suggests:	php-pdo
Suggests:	php-phpunit-PHP_Invoker
Suggests:	php-simplexml
Suggests:	php-soap
Suggests:	php-tokenizer
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
