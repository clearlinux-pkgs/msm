#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msm
Version  : 0.8.8
Release  : 29
URL      : https://files.pythonhosted.org/packages/7e/42/66f2d39be2767b064d0c384b764ef18aae11344e618287f40fea5c84c866/msm-0.8.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/7e/42/66f2d39be2767b064d0c384b764ef18aae11344e618287f40fea5c84c866/msm-0.8.8.tar.gz
Summary  : Mycroft Skills Manager
Group    : Development/Tools
License  : Apache-2.0
Requires: msm-bin = %{version}-%{release}
Requires: msm-license = %{version}-%{release}
Requires: msm-python = %{version}-%{release}
Requires: msm-python3 = %{version}-%{release}
Requires: GitPython
Requires: PyYAML
Requires: fasteners
Requires: lazy
Requires: pako
BuildRequires : GitPython
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : fasteners
BuildRequires : lazy
BuildRequires : pako

%description
## Mycroft Skills Manager
Mycroft Skills Manager is a command line tool and a python module for interacting with the mycroft-skills repository. It allows querying the repository for information (skill listings, skill meta data, etc) and of course installing and removing skills from the system.

%package bin
Summary: bin components for the msm package.
Group: Binaries
Requires: msm-license = %{version}-%{release}

%description bin
bin components for the msm package.


%package license
Summary: license components for the msm package.
Group: Default

%description license
license components for the msm package.


%package python
Summary: python components for the msm package.
Group: Default
Requires: msm-python3 = %{version}-%{release}

%description python
python components for the msm package.


%package python3
Summary: python3 components for the msm package.
Group: Default
Requires: python3-core
Provides: pypi(msm)
Requires: pypi(fasteners)
Requires: pypi(gitpython)
Requires: pypi(lazy)
Requires: pypi(pako)
Requires: pypi(pyyaml)

%description python3
python3 components for the msm package.


%prep
%setup -q -n msm-0.8.8
cd %{_builddir}/msm-0.8.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598284299
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/msm
cp %{_builddir}/msm-0.8.8/LICENSE %{buildroot}/usr/share/package-licenses/msm/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/msm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/msm/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
