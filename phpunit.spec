%define		status		stable
%define		pearname	PHPUnit
%define		php_min_version 5.3.3
Summary:	%{pearname} - regression testing framework for unit tests
Summary(pl.UTF-8):	%{pearname} - zestaw testów regresyjnych
Name:		phpunit
# we use 3.7-lts version
Version:	3.7.38
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/sebastianbergmann/phpunit/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d7452511b562cc582f204da0b180ff42
Patch0:		autoload.patch
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
Provides:	php-phpunit-PHPUnit = %{version}
Obsoletes:	php-PHPUnit < 3.5
Obsoletes:	php-PHPUnit-tests
Obsoletes:	php-pear-PHPUnit
Obsoletes:	php-pear-PHPUnit2
Obsoletes:	php-phpunit-PHPUnit
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
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
cp -a PHPUnit $RPM_BUILD_ROOT%{php_pear_dir}
install -p phpunit.php $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/phpunit
%{php_pear_dir}/PHPUnit
