# Generated from uuidtools-2.1.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	uuidtools

Summary:	UUID generator
Name:		rubygem-%{rbname}

Version:	2.1.2
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://uuidtools.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
A simple universally unique ID generation library.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/compat
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/compat/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/uuidtools
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/uuidtools/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/README
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
