%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm_Rule_Spelling
%define		_status		alpha
%define		_pearname	HTML_QuickForm_Rule_Spelling
Summary:	%{_pearname} - A HTML_QuickForm rule plugin that checks the spelling of its values
Summary(pl.UTF-8):	%{_pearname} - wtyczka HTML_QuickForm sprawdzająca pisownie słów
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f792d38c7f90c932f99f0c87cc76d970
URL:		http://pear.php.net/package/HTML_QuickForm_Rule_Spelling/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm
Requires:	php-pear-PEAR >= 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Although browsers now have builtin spellcheckers,
HTML_QuickForm_Rule_Spelling allows you to control the quality of text
data submitted.

The frontend is a clientside javascript dialog that goes through the
misspelt words, giving the user the option to ignore the word, add it
to the dictionary or change the word given a list of suggestions.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Chociaż przeglądarki nie posiadają wbudowanej funkcjonalności
sprawdzania pisowni, HTML_QuickForm_Rule_Spelling pozwala na kontrolę
jakości wpisanego tekstu.

Frontend to wyświetlane przez kod javascript okno wyświetlające
błędnie wpisane słowa, dając użytkownikowi możliwość zignorowania
danego słowa, dodania go do słownika bądź jego zmiany z listy
proponowanych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/HTML_QuickForm_Rule_Spelling/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/Rule/Spelling
%{php_pear_dir}/HTML/QuickForm/Rule/Spelling.php
