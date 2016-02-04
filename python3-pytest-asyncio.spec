%global pypi_name pytest-asyncio
%global srcname pytest_asyncio
%global project_owner pytest-dev
%global github_name pytest-asyncio
%global commit ae9b430a3cd9a78eb14a16f5e82686710028790a
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python3-%{pypi_name}
Version:        0.3.0
Release:        2.git%{shortcommit}%{?dist}
Summary:        Pytest support for asyncio

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description
pytest-asyncio is an Apache2 licensed library, written in Python, for testing
asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes it
slightly more difficult to test using normal testing tools. pytest-asyncio
provides useful fixtures and markers to make testing easier.


%prep
%setup -qn %{github_name}-%{commit}


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}/


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2.gitae9b430
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 Julien Enselme <jujens@jujens.eu> - 0.3.0-1.gitae9b430
- Update to 0.3.0 (bz:1293083)

* Thu Nov 5 2015 Julien Enselme <jujens@jujens.eu> - 0.1.3-3.git2a4c7e6
- Rebuilt for python 3.5

* Sun Aug 2 2015 Julien Enselme <jujens@jujens.eu> - 0.1.3-2.git2a4c7e6
- Add %%python_provide

* Sat Aug 1 2015 Julien Enselme <jujens@jujens.eu> - 0.1.3-1.git2a4c7e6
- Initial package
