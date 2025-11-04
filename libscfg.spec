%define api 2

%define libname %mklibname scfg
%define devname %mklibname -d scfg

Name:           libscfg
Version:        0.2.0
Release:        1
Summary:        C library for a simple configuration file format
Group:          System/Library
License:        MIT
URL:            https://codeberg.org/emersion/libscfg/
Source0:        https://codeberg.org/emersion/libscfg/archive/v%{name}/%{name}-v%{version}.tar.gz
#Source0:        https://git.sr.ht/~emersion/libscfg/refs/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gnupg2
BuildRequires:  meson

%description
C library for a simple configuration file format

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name} -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libscfg.so.%{api}
%{_libdir}/libscfg.so.%{version}

%files -n %{devname}
%{_includedir}/scfg.h
%{_libdir}/libscfg.so
%{_libdir}/pkgconfig/scfg.pc
