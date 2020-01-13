#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : msm
Version  : 0.8.5
Release  : 23
URL      : https://files.pythonhosted.org/packages/91/a0/98d07b9c5b45fd2ec42fe202722f76bc3cab902ca371474eb3d9a82758e5/msm-0.8.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/91/a0/98d07b9c5b45fd2ec42fe202722f76bc3cab902ca371474eb3d9a82758e5/msm-0.8.5.tar.gz
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
No detailed description available

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

%description python3
python3 components for the msm package.


%prep
%setup -q -n msm-0.8.5
cd %{_builddir}/msm-0.8.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578940742
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/msm
cp %{_builddir}/msm-0.8.5/LICENSE %{buildroot}/usr/share/package-licenses/msm/a6a5418b4d67d9f3a33cbf184b25ac7f9fa87d33
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)
/usr/msm/LICENSE

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
