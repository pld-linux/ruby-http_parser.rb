#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	http_parser.rb
Summary:	Simple callback-based HTTP request/response parser
Name:		ruby-%{pkgname}
Version:	0.5.3
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7782c17d0c984f33bd82acbe9bcbaec8
URL:		http://github.com/tmm1/http_parser.rb
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
%if %{with tests}
BuildRequires:	ruby-json >= 1.4.6
BuildRequires:	ruby-rake-compiler >= 0.7.9
BuildRequires:	ruby-rspec >= 2.0.1
BuildRequires:	ruby-yajl-ruby >= 0.8.1
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings to <http://github.com/ry/http-parser> and
<https://github.com/http-parser/http-parser.java>

%prep
%setup -q -n %{pkgname}-%{version}

%build
cd ext/ruby_http_parser
%{__ruby} extconf.rb
%{__make} V=1 \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

install -d $RPM_BUILD_ROOT%{ruby_vendorarchdir}
install -p ext/ruby_http_parser/ruby_http_parser.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE-MIT 
%{ruby_vendorlibdir}/http/parser.rb
%{ruby_vendorlibdir}/%{pkgname}
%attr(755,root,root) %{ruby_vendorarchdir}/ruby_http_parser.so
