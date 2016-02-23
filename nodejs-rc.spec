%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name rc

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.1.2
Release:        4%{?dist}
Summary:        Hardwired configuration loader

License:        MIT or BSD or ASL 2.0
URL:            https://github.com/dominictarr/rc
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(ini)
BuildRequires:  %{?scl_prefix}npm(strip-json-comments)
BuildRequires:  %{?scl_prefix}npm(minimist)
BuildRequires:  %{?scl_prefix}npm(deep-extend)
%endif

%description
The non-configurable configuration loader for lazy people.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep deep-extend
%nodejs_fixdep minimist
%nodejs_fixdep strip-json-comments
%nodejs_fixdep ini

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js lib %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
set -e; node test/test.js; node test/ini.js; node test/nested-env-vars.js
%endif

%files
%doc README.md LICENSE.MIT LICENSE.APACHE2 LICENSE.BSD
%{nodejs_sitelib}/%{module_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.2-4
- rebuilt

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.1.2-3
- Enable scl macros

* Fri Dec 18 2015 Troy Dawson <tdawson@redhat.com> - 1.1.2-1
- Update to 1.1.2

* Sat Dec 12 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.6.0-3
- Fixdep updated minimist

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.6.0-1
- update to 0.6.0 upstream release

* Mon Dec 08 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.5.4-2
- Add missing multilicense tag and its text

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.5.4-1
- Initial packaging
